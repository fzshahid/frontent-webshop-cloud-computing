from flask import Blueprint, request, jsonify
from models import Order
from extensions import db
from services.email_service import send_email
from services.payment_service import create_payment

bp = Blueprint('payment_routes', __name__, url_prefix='/payments')

@bp.route('/create', methods=['POST'])
def create_payment_route():
  data = request.json
  order_id = data.get('order_id')
  amount = data.get('amount')
  description = data.get('description', f'Payment for order {order_id}')

  if not order_id or not amount:
    return jsonify({'error': 'Missing required parameters'}), 400

  order = Order.query.get(order_id)
  if not order:
    return jsonify({'error': 'Order not found'}), 404

  result = create_payment(amount, description=description)
  if result['status'] == 'success':
    order.payment_id = result['paymentID']
    order.status = 'Paid'
    db.session.commit()

    # Send confirmation email
    email_sent = send_email(
      'Payment Confirmation',
      order.email,
      f'Your payment for order {order.id} has been successfully processed.'
    )
    if not email_sent:
      return jsonify({'error': 'Payment processed but failed to send email'}), 500

    return jsonify(result)
  else:
    return jsonify(result), 500
