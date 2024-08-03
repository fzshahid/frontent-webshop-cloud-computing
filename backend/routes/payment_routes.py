# routes/payment_routes.py

from flask import Blueprint, request, jsonify
from services.payment_service import process_payment

bp = Blueprint('payment_routes', __name__, url_prefix='/payments')

@bp.route('/process', methods=['POST'])
def process_payment_route():
    data = request.get_json()
    order_id = data['order_id']
    amount = data['amount']
    payment_method = data['payment_method']
    result = process_payment(order_id, amount, payment_method)
    return jsonify(result)
