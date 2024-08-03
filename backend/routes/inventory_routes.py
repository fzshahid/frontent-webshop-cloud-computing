# routes/inventory_routes.py

from flask import Blueprint, jsonify
from models import Product

bp = Blueprint('inventory_routes', __name__, url_prefix='/inventory')

@bp.route('/check', methods=['GET'])
def check_inventory():
    low_stock_products = Product.query.filter(Product.stock < 10).all()
    return jsonify([{'id': p.id, 'name': p.name, 'stock': p.stock} for p in low_stock_products])
