from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

"""Inicialização do Objeto que tratará as ORMs no Flask."""
db = SQLAlchemy(app)
