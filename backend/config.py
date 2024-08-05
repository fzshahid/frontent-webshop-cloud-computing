import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('emailid')
    MAIL_PASSWORD = os.environ.get('password')
    BCRYPT_LOG_ROUNDS = 12
    PAYPAL_CLIENT_ID = os.environ.get('AXURJtLil9b5BuDZ47xdEY8yC4YajOfga6y-UhsdrDQWejzAJp2uMtYCTzq47bJpJibJXyBKekxs_Pfv')
    PAYPAL_CLIENT_SECRET = os.environ.get('EAelqwGufFWrjZCtKcv8gTUrB-pEo98Bz49IjszNBSbkFO5qubXo-0qn58vn0D9krX6Qxk6gpeJzjtEJ')

