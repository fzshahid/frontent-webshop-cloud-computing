# routes/product_routes.py

from flask import Blueprint, request, jsonify
from extensions import db
from models import Product

bp = Blueprint('product_routes', __name__, url_prefix='/products')

@bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created'}), 201

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products])
    
@bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock})


@bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})
