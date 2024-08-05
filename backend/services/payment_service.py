import random

def process_payment(amount, currency='EUR', payment_method=None, description=None):
    # Mock PayPal payment process
    if payment_method == 'paypal':
        # Simulate a payment success or failure
        success = random.choice([True, False])
        if success:
            return {'status': 'success', 'transaction_id': f'TRANS-{random.randint(1000, 9999)}'}
        else:
            return {'status': 'failure', 'error': 'Mock payment failure'}
    return {'status': 'failure', 'error': 'Invalid payment method'}
