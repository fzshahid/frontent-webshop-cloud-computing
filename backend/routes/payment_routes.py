from flask import Blueprint, request, jsonify
from services.payment_service import process_payment
from models import Order

bp = Blueprint('payment_routes', __name__, url_prefix='/api/payments')

@bp.route('/process', methods=['POST'])
def process_payment_route():
  data = request.json
  order_id = data.get('order_id')
  amount = data.get('amount')
  description = data.get('description', f'Payment for order {order_id}')

  if not order_id or not amount:
    return jsonify({'error': 'Missing required parameters'}), 400

  order = Order.query.get(order_id)
  if not order:
    return jsonify({'error': 'Order not found'}), 404

  if amount < order.amount:
    return jsonify({'error': 'Payment amount is less than the order total'}), 400

  result = process_payment(order_id, amount, description=description)
  return jsonify(result)
