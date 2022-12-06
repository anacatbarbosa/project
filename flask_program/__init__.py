import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session


def creat_app():
    #configure app name
    app = Flask(__name__)

    #template auto-reload
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Setting session to use filesystem 
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    Session(app)

    #importing the blueprint views to register into our flask app
    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
