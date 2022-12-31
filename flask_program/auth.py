#File to code authentication files routes, such as login and register.
import re

from flask import (  # Blueprint allow to code the views, or @app.routes, in multiple files
    Blueprint, flash, redirect, render_template, request, session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .helpers import check_errors, str_to_list
from .models_database import Post, User

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
@auth.route('/register/<string:type_of_user>', methods=['POST'])
def register(type_of_user):
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
                if type_of_user == 'regular_user':
                    return render_template('login.html', user=current_user)
                elif type_of_user == 'adm_user':
                    return render_template('profile.html', user=current_user)

        # Check_errors will check the email, password and user name, if finds any kind of erros will return the number of erros found, otherwise will return 0. Check more at helpers.py
        if check_errors(name, email, password1, password2) > 0:
            if type_of_user == 'regular_user':
                return render_template('login.html', user=current_user)
            elif type_of_user == 'adm_user':
                return render_template('profile.html', user=current_user)
        else:
            # To get here no error was detected, after that it will add the user to the db and redirect to the main page, the index.html 
            if type_of_user == 'regular_user':
                new_user = User(email=email, password=generate_password_hash(password1), name=name, adm_bool=0) #adm_bool = 0 means not and adm_bool = 1 means it's an adm
            elif type_of_user == 'adm_user':
                new_user = User(email=email, password=generate_password_hash(password1), name=name, adm_bool=1) #adm_bool = 0 means not and adm_bool = 1 means it's an adm
            
            db.session.add(new_user)
            db.session.commit()
            
            if type_of_user == 'regular_user':
                flash('Account created!', category='success')
            elif type_of_user == 'adm_user':
               flash('Admin account created!', category='success')
    
            login_user(new_user, remember=True)
            return redirect(url_for('views.index'))

    return render_template('login.html', user=current_user)


# Route to profile page, it will contain, all the user recipes, options like: Change password, change username, change e-mail, if the ...
# ... user is and adm, will contain the option to add another adm
@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    # Get user information
    id = current_user.id
    user_info = User.query.filter(User.id == id).first()

    # Check if the user is an adm
    is_adm = user_info.adm_bool
    # Post_info = recipes titles and descriptions
    post_info = Post.query.filter(Post.user_id == id).all()
    
    # Post_thumb = first image from the uploads to use as a thumbnail
    post_thumb = []

    for i in post_info:
        hold = str_to_list(i.filename)
        post_thumb.append(hold[0])

    return render_template('profile.html', user=current_user, user_name=user_info.name, user_email=user_info.email ,my_recipes=post_thumb, is_adm=is_adm)

@auth.route('/profile/<string:item>', methods=['POST'])
@login_required
def change(item):
    user = User.query.filter(User.id == current_user.id).first()
    current_pw = request.form.get("password")

    if not check_password_hash(user.password, current_pw):
            flash('Invalid password. Please try again.', category='error')
            return redirect(url_for('auth.profile'))

    if item == "name":
        new_name = request.form.get("newName")
        if check_errors(new_name, False, False, False) > 0:
            return redirect(url_for('auth.profile'))
        user.name = new_name
        flash('Name Changed!', category='success')

    elif item == "email":
        new_email = request.form.get("newEmail")
        email_verification = User.query.filter_by(email=new_email).first()
        if email_verification:
            flash('E-mail already in use. Please try another one.', category='error')
            return redirect(url_for('auth.profile'))
        if check_errors(False, new_email, False, False) > 0:
            return redirect(url_for('auth.profile'))
        user.email = new_email
        flash('E-mail Changed!', category='success')

    elif item == "password":
        new_password = request.form.get("newPw")
        confirm_newpw = request.form.get("confirmPw")
        if check_errors(False, False, new_password, confirm_newpw) > 0:
            return redirect(url_for('auth.profile'))
        user.password = generate_password_hash(new_password)
        flash('Password Changed!', category='success')
                
    db.session.commit()
    return redirect(url_for('auth.profile'))
