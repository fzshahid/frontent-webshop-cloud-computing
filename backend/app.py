# app.py

from flask import Flask
from extensions import db, mail, login_manager
from routes import product_routes, order_routes, payment_routes, inventory_routes, auth_routes
from models import User, Product, Order
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth_routes.login'

app.register_blueprint(product_routes.bp)
app.register_blueprint(order_routes.bp)
app.register_blueprint(payment_routes.bp)
app.register_blueprint(inventory_routes.bp)
app.register_blueprint(auth_routes.bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
