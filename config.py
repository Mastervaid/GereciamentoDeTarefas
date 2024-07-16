import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'  # Ou outro banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False
