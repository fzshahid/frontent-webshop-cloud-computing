from flask import Flask
from extensions import db, mail, login_manager, init_app
from config import Config
from flask_migrate import Migrate
from routes import product_routes, order_routes, payment_routes, inventory_routes, auth_routes
from flask_cors import CORS

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  # Initialize app extensions
  init_app(app)

  # Configure CORS
  CORS(app, resources={r"/api*": {"origins": "*"}},
       supports_credentials=True,
       allow_headers=["Content-Type", "Authorization"],
       expose_headers=["Content-Type", "Authorization"],
       methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

  migrate = Migrate(app, db)

  with app.app_context():
    db.create_all()

  # Register blueprints
  app.register_blueprint(product_routes.bp)
  app.register_blueprint(order_routes.bp)
  app.register_blueprint(payment_routes.bp)
  app.register_blueprint(inventory_routes.bp)
  app.register_blueprint(auth_routes.bp)

  return app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)
