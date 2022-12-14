# A file to code the database models, creating models to store login, images, descriptions, passwords, etc...
from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


# importing the database from the __init__.py, the "from ." means we will import from a file locates at this same folder
class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    img_path = db.Column(db.Text, nullable=False, unique=True)
    filename = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Note(db.Model): #to store when something was posted
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


class User(db.Model, UserMixin): #user information
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post')