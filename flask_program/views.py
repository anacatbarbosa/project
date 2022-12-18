#File to code @app.route files, but not authentication files routes, such as login and register.
import os

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import db
from .models_database import Post, User

#Blueprint allow to code the views, or @app.routes, in multiple files

views = Blueprint('views', __name__) #setting the Blueprint variable name.
upload_folder = 'flask_program/static/uploaded_files'# path to the uploaded folder to save the files. Path from main.py to upoladed_files
pic_to_html =  '../static/uploaded_files' #path to pass to html file, this path + filename will inform the url to the html go take it
#path_save = os.path.join(upload_folder, filename)

@views.route('/')
def index():

    img = Post.query.filter(Post.user_id == 1).all()
    return render_template('index.html', posts=img, user=current_user)


@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)


@views.route('/recipes', methods=['GET', 'POST'])
def recipes():

    if request.method == 'POST':
        pic = request.files['file']

        if not pic:
            flash('File not found, please select a valid file.', category='error')
        else:
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            upload_folder = 'flask_program/static/uploaded_files'
            path_save = os.path.join(upload_folder, filename)
            pic.save(path_save)
            path_html = os.path.join(pic_to_html, filename)
            post = Post(carousel=0, description="test", filename=filename, img_path=path_html, mimetype=mimetype, title="Test", user_id=1) 
            db.session.add(post)
            db.session.commit()
    
    img = Post.query.filter(Post.carousel == 0).all()
    return render_template('recipes.html', imgs_uploaded = img, user=current_user)
