from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsdb.db'
db = SQLAlchemy(app)

from app import routes
