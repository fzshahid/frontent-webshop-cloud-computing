# routes/order_routes.py

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from models import Order
from services.email_service import send_email

bp = Blueprint('order_routes', __name__, url_prefix='/orders')

@bp.route('/', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()
    new_order = Order(product_id=data['product_id'], user_id=current_user.id, quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    send_email('Order Confirmation', current_user.email, 'Your order has been created')
    return jsonify({'message': 'Order created'}), 201

@bp.route('/', methods=['GET'])
@login_required
def get_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': o.id, 'product_id': o.product_id, 'quantity': o.quantity, 'status': o.status} for o in orders])

@bp.route('/<int:id>', methods=['PUT'])
@login_required
def update_order(id):
    data = request.get_json()
    order = Order.query.get_or_404(id)
    if order.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized'}), 403
    order.status = data.get('status', order.status)
    db.session.commit()
    send_email('Order Update', current_user.email, 'Your order status has been updated')
    return jsonify({'message': 'Order updated'})
