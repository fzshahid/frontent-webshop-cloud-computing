import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:CloudComputing2024@mydatabase.cvca4k4ky46o.us-east-1.rds.amazonaws.com:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    BCRYPT_LOG_ROUNDS = 12
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '47a9c9d4058dff'
    MAIL_PASSWORD = 'f2d3fa99cc42a3'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # S3 Configuration
    S3_BUCKET = os.environ.get('bucketname')
    S3_KEY = os.environ.get('key')
    S3_SECRET = os.environ.get('secret')
    S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'

