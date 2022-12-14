#File to code authentication files routes, such as login and register.
import re

from flask import (  # Blueprint allow to code the views, or @app.routes, in multiple files
    Blueprint, flash, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .helpers import check_errors
from .models_database import User

# Blueprint allow to code the views, or @app.routes, in multiple files

auth = Blueprint('auth', __name__) #setting the Blueprint variable name.

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        # get user inputs
        username = request.form.get('username')
        password = request.form.get('password')

        # load the user information at user variable
        user = User.query.filter_by(username=username).first()

        if user:
            # if the user exist, confirm the password.
            if not check_password_hash(user.password, password):
                flash('Invalid password and username combination. Please try again.', category='error')
            else:
                # if the user and password match, send to the index page
                return redirect('/')
        else:
            # if the user doesn't exist, flashes an error message
            flash('Invalid Username. Please try again or register a new account.', category='error')
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #check_errors will check the email, password and username, if finds any kind of erros will return the number of erros found, otherwise will return 0. Check more at helpers.py
        if check_errors(username, email, password1, password2) > 0:
            return render_template('login.html')
        else:
            new_user = User(email=email, password=generate_password_hash(password1), username=username)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.index'))
    return render_template('login.html')