import os

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASEURL')
    SECRET_KEY = os.environ.get("SECRETKEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False