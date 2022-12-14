#File to code authentication files routes, such as login and register.
from flask import (  # Blueprint allow to code the views, or @app.routes, in multiple files
    Blueprint, flash, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models_database import User

#Blueprint allow to code the views, or @app.routes, in multiple files

auth = Blueprint('auth', __name__) #setting the Blueprint variable name.

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        username = request.form('username')
        password = request.form('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if not check_password_hash(user.password, password):
                flash('Invalid password and username combination. Please try again.', category='error')
        else:
            flash('Invalid Username. Please try again or register a new account.', category='error')
    return render_template('login.html')