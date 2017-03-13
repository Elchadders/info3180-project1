from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

UPLOAD_FOLDER = '/app/static/uploads'
app.config['SECRET_KEY'] = 'password123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/db_app'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.debug = True
db = SQLAlchemy(app)

from app import views, models 

app.config.from_object(__name__)
from app import views
