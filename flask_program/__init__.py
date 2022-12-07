import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def creat_app():
    #configure app name
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ashdkasjd asdlkjasdl' #here while its not going to production.

    # Setting the upload pictures folder
    picFolder = 'flask_program/static/uploaded_files'
    app.config['UPLOAD_FOLDER'] = picFolder
    # template auto-reload
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Setting database according to https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#configure-the-extension
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'

    # Initializing the database, all DOC here: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
    db.init_app(app)

    # Setting session
    app.config["SESSION_PERMANENT"] = False

    #importing the blueprint views to register into our flask app
    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Creating the database
    from .models_database import Note, Post, User 

    creat_database(app) #only creates a database if it doesn't exist

    return app


def creat_database(app):
    if not os.path.exists('./instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database Created!!")
