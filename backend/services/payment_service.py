import paypalrestsdk
import os
import requests
from requests.exceptions import RequestException

paypalrestsdk.configure({
  "mode": "sandbox",
  "client_id": os.environ.get('PAYPAL_CLIENT_ID'),
  "client_secret": os.environ.get('PAYPAL_CLIENT_SECRET')
})

# Updated sandbox buyer email and password
SANDBOX_BUYER_EMAIL = 'sb-943roo32026153@personal.example.com'
SANDBOX_BUYER_PASSWORD = 'j)Rc6U3-'  # Replace with the new verified password

def create_payment(amount, currency='EUR', description=None):
  payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
      "payment_method": "paypal"
    },
    "transactions": [{
      "amount": {
        "total": f"{amount / 100:.2f}",
        "currency": currency
      },
      "description": description
    }],
    "redirect_urls": {
      "return_url": "http://localhost:5000/payments/execute",
      "cancel_url": "http://localhost:5000/payments/cancel"
    }
  })

  if payment.create():
    print("Payment created successfully:", payment)
    approval_url = None
    for link in payment.links:
      if link.rel == 'approval_url':
        approval_url = link.href
        break

    if not approval_url:
      return {"status": "failure", "error": "No approval URL found"}

    # Simulate payment approval
    session = requests.Session()
    login_url = "https://www.sandbox.paypal.com/signin"

    try:
      # First, get the login page to establish a session and get any necessary cookies
      login_page = session.get(login_url)
      print("Login page status:", login_page.status_code)
      if login_page.status_code != 200:
        return {"status": "failure", "error": "Failed to get PayPal login page"}

      # Prepare login data
      login_data = {
        "login_email": SANDBOX_BUYER_EMAIL,
        "login_password": SANDBOX_BUYER_PASSWORD,
        "submit.x": "Log In"
      }

      # Perform login
      login_response = session.post(login_url, data=login_data, headers={
        "Content-Type": "application/x-www-form-urlencoded"
      })
      print("Login response status:", login_response.status_code)
      print("Login response text:", login_response.text)
      if login_response.status_code != 200 or "login_password" in login_response.text:
        return {"status": "failure", "error": "Failed to log in to PayPal sandbox"}

      # Follow redirects if necessary
      approval_response = session.get(approval_url, allow_redirects=True)
      print("Approval response status:", approval_response.status_code)
      print("Approval response text:", approval_response.text)
      if approval_response.status_code != 200:
        return {"status": "failure", "error": "Failed to access approval URL"}

      # Execute the payment
      payment = paypalrestsdk.Payment.find(payment.id)
      print("Payment found for execution:", payment)  # Debug: Print the payment object to inspect it

      if payment.payer and payment.payer.payer_info:
        payer_id = payment.payer.payer_info.payer_id
        if payment.execute({"payer_id": payer_id}):
          return {"status": "success", "paymentID": payment.id, "transaction_id": payment.id}
        else:
          print("Payment execution error:", payment.error)
          return {"status": "failure", "error": payment.error}
      else:
        print("Payment object missing payer info:", payment)
        return {"status": "failure", "error": "Payer information not available"}
    except RequestException as e:
      print("Request exception:", e)
      return {"status": "failure", "error": f"Request exception: {str(e)}"}
  else:
    print("Payment creation error:", payment.error)
    return {"status": "failure", "error": payment.error}
