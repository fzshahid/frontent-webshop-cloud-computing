from flask_mail import Message
from extensions import mail

def send_email(subject, recipients, body):
  try:
    if not isinstance(recipients, list):
      recipients = [recipients]
    msg = Message(subject, sender='p08228412@gmail.com', recipients=recipients)
    msg.body = body
    mail.send(msg)
    print(f"Email sent successfully to {recipients}")
    return True
  except Exception as e:
    print(f"Failed to send email: {str(e)}")
    return False
