# services/mock_payment_gateways.py

def mock_stripe_payment(order_id, amount):
    # Simulate Stripe payment processing
    return {
        'status': 'success',
        'order_id': order_id,
        'amount': amount,
        'payment_method': 'Stripe',
        'transaction_id': 'mock-stripe-transaction-id'
    }
