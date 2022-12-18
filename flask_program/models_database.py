# A file to code the database models, creating models to store login, images, descriptions, passwords, etc...
from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


# importing the database from the __init__.py, the "from ." means we will import from a file locates at this same folder
class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    carousel = db.Column(db.Integer, nullable=False) # Carousel = 1 means it's to use at carousel, can only be added by adm's not regular users. Carousel = 0 means regular posts from the users.
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    filename = db.Column(db.Text, nullable=False)
    img_path = db.Column(db.Text, nullable=False, unique=True)
    mimetype = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin): #user information
    id = db.Column(db.Integer, primary_key=True)
    adm_bool = db.Column(db.Integer) #For security reasons an Admin can only be added manually at the db. One ADM can add another ADM via website, otherwise it's not possible to create a adm account via register. ADM = 0 means it's adm, ADM = 1 means it's adm
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post')

