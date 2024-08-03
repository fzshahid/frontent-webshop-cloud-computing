# services/email_service.py

from flask_mail import Message
from extensions import mail

def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)
