import os
SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///task_manager.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_secret_key'
LOGGING_LEVEL = 'DEBUG'