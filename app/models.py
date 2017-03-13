import datetime
from flask import Markup, url_for
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app import db
from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder import Model
from flask.ext.sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer(3))
    gender = db.Column(db.String(80), unique=True)
    biography = db.Column(db.String(300), unique=True)
    image = db.Column(db.String(100), unique=True)
    

    def __init__(self, firstname, lastname, age, gender, biography):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.biography = biography
        
        
        
        
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
            
    
    def __repr__(self):
        return '<User %r>' % (self.username)
    
    def to_json(self):
        return jsonify({
            "userid": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "gender": self.gender,
            "age": self.age,
            "profile_created_on": self.added_on.strftime("%Y-%m-%d"),
            "biography": self.biography,
            "image": ".."
            })
        
        
        



   