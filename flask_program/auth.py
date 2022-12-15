#File to code authentication files routes, such as login and register.
import re

from flask import (  # Blueprint allow to code the views, or @app.routes, in multiple files
    Blueprint, flash, redirect, render_template, request, session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
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
        email = request.form.get('email')
        password = request.form.get('password')

        # load the user information at user variable
        user = User.query.filter_by(email=email).first()
        
        # check if it's or not an user
        if user:
            if not check_password_hash(user.password, password):
                flash('Invalid password and e-mail combination. Please try again.', category='error')
            else:
                 # if the user and password match, send to the index page
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
        else:
            # if it's not an user, flash and error message
            flash('Invalid e-mail. Please try again or register a new account.', category='error')
    return render_template('login.html', user=current_user)

# logout function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))


# Register function
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Getting all the form information from the login.html register Form
        name = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Creating an user variable to check if the e-mail already in use.
        user = User.query.filter_by(email=email).first()
        if user:
            if user.email == email:
                flash('E-mail already in use. Please try another one.', category='error')
                return render_template('login.html', user=current_user)

        # Check_errors will check the email, password and user name, if finds any kind of erros will return the number of erros found, otherwise will return 0. Check more at helpers.py
        if check_errors(name, email, password1, password2) > 0:
            return render_template('login.html', user=current_user)
        else:
            # To get here no error was detected, after that it will add the user to the db and redirect to the main page, the index.html 
            new_user = User(email=email, password=generate_password_hash(password1), name=name, adm_bool=0) #adm_bool = 0 means not and adm_bool = 1 means it's an adm
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.index'))

    return render_template('login.html', user=current_user)