from flask_mail import Message
from extensions import mail

def send_email(subject, recipient, body):
    try:
        msg = Message(subject, sender='kspooja5699@gmail.com', recipients=[recipient])
        msg.body = body
        mail.send(msg)
        print(f"Email sent successfully to {recipient}")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False
