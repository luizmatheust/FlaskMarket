from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '0fa5571fb03c29c8a0b22057'

"""Inicialização do Objeto que tratará as ORMs no Flask."""
db = SQLAlchemy(app)

from market import routes
