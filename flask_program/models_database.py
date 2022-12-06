# A file to code the database models, creating models to store login, images, descriptions, passwords, etc...
from flask_login import UserMixin

from . import db

# importing the database from the __init__.py, the "from ." means we will import from a file locates at this same folder

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Columun(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(10000), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)