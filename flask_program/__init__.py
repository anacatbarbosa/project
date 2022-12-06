import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def creat_app():
    #configure app name
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ashdkasjd asdlkjasdl' #here while its not going to production.
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

    return app

