import os
#db directory
basedir = os.path.abspath(os.path.dirname(__file__))
#config class
class Config:
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False