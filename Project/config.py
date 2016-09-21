import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_SSL = False
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'eduardo@codigofacilito.com'
	MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
