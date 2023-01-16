from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
#import routes from routes.py
from . import routes