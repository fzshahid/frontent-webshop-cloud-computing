from flask import Flask
from extensions import db, mail, login_manager
from routes import product_routes, order_routes, inventory_routes, payment_routes, auth_routes
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(product_routes.bp)
app.register_blueprint(order_routes.bp)
app.register_blueprint(inventory_routes.bp)
app.register_blueprint(payment_routes.bp, name='payment_routes_unique')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
