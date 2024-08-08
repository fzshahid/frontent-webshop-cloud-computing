from flask import Flask
from extensions import db, mail, login_manager, init_app
from config import Config
from flask_migrate import Migrate
from routes import product_routes, order_routes, payment_routes, inventory_routes, auth_routes
from flask_cors import CORS
from flask import Blueprint
import boto3
from werkzeug.utils import secure_filename

blueprint = Blueprint('blueprint', __name__)

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  # Initialize app extensions
  init_app(app)

  # Configure CORS
  CORS(app, resources={r"/*": {"origins": "*"}},
       supports_credentials=True,
       allow_headers=["Content-Type", "Authorization"],
       expose_headers=["Content-Type", "Authorization"],
       methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

  migrate = Migrate(app, db)

  with app.app_context():
    db.create_all()

  @blueprint.after_request 
  def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers']='Content-Type'
    # Other headers can be added here if needed

  # Register blueprints
  app.register_blueprint(product_routes.bp)
  app.register_blueprint(order_routes.bp)
  app.register_blueprint(payment_routes.bp)
  app.register_blueprint(inventory_routes.bp)
  app.register_blueprint(auth_routes.bp)
  
  # Initialize Boto3 S3 client
  s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET']
  )

  # Helper function to upload files to S3
  def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
      s3.upload_fileobj(
        file,
        bucket_name,
        file.filename,
        ExtraArgs={
          "ACL": acl,
          "ContentType": file.content_type
        }
      )
    except Exception as e:
      print("Something Happened: ", e)
      return e
    return f"{app.config['S3_LOCATION']}{file.filename}"

  # Route to handle file upload
  @app.route("/upload", methods=["POST"])
  def upload_file():
    if "file" not in request.files:
      return "No file part", 400

    file = request.files["file"]

    if file.filename == "":
      return "No selected file", 400

    if file:
      file.filename = secure_filename(file.filename)
      output = upload_file_to_s3(file, app.config["S3_BUCKET"])
      return jsonify({"file_url": output}), 200

  return app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)
