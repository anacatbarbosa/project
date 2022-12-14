#File to code authentication files routes, such as login and register.
from flask import (  # Blueprint allow to code the views, or @app.routes, in multiple files
    Blueprint, flash, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

#Blueprint allow to code the views, or @app.routes, in multiple files

auth = Blueprint('auth', __name__) #setting the Blueprint variable name.

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        a = 'test'
    return render_template('login.html')