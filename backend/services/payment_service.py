# services/payment_service.py

from services.mock_payment_gateways import mock_stripe_payment

def process_payment(order_id, amount, payment_method):
    if payment_method == 'Stripe':
        return mock_stripe_payment(order_id, amount)
    else:
        return {
            'status': 'failure',
            'message': 'Unsupported payment method'
        }
