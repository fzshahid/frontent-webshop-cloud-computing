from flask import Blueprint, request, jsonify
from models import Order, Inventory
from extensions import db
from services.email_service import send_email
import uuid

bp = Blueprint('order_routes', __name__, url_prefix='/orders')

@bp.route('/', methods=['POST'])
def create_order():
    order_data = request.json
    if not order_data or 'items' not in order_data or 'email' not in order_data:
        return jsonify({'error': 'Invalid order data'}), 400

    for item in order_data['items']:
        product_id = item['product_id']
        quantity = item['quantity']

        inventory = Inventory.query.get(product_id)
        if not inventory or inventory.stock < quantity:
            return jsonify({'error': f'Not enough stock for product: {product_id}'}), 400
        
        inventory.stock -= quantity
        if inventory.stock < 10:
            send_email(
                f'Stock Alert for product: {product_id}',
                ['kspooja5699@gmail.com'],
                f'The stock for product {product_id} is below 10. Current stock: {inventory.stock}'
            )

    order_id = str(uuid.uuid4())
    new_order = Order(id=order_id, email=order_data['email'], items=order_data['items'])
    db.session.add(new_order)
    db.session.commit()

    send_email(
        'Order Confirmation',
        [order_data['email']],
        f'Your order (ID: {order_id}) has been received and is being processed.'
    )

    return jsonify({'message': 'Order created successfully', 'order': new_order.to_dict()}), 201

@bp.route('/<string:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.to_dict()), 200
    return jsonify({'error': 'Order not found'}), 404

@bp.route('/<string:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    data = request.json
    order.status = data.get('status', order.status)
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'}), 200

@bp.route('/<string:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@bp.route('/search', methods=['GET'])
def search_orders_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email parameter is required'}), 400

    orders = Order.query.filter_by(email=email).all()
    return jsonify([order.to_dict() for order in orders]), 200
