#File to code @app.route files, but not authentication files routes, such as login and register.
from flask import Blueprint, flash, redirect, render_template, request, session, url_for#Blueprint allow to code the views, or @app.routes, in multiple files

views = Blueprint('views', __name__) #setting the Blueprint variable name.

@views.route('/')
def index():
    return render_template('index.html') 