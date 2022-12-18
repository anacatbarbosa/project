#File to code @app.route files, but not authentication files routes, such as login and register.
import os

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import db
from .helpers import allowed_file
from .models_database import Post, User

#Blueprint allow to code the views, or @app.routes, in multiple files

views = Blueprint('views', __name__) #setting the Blueprint variable name.
upload_folder = 'flask_program/static/uploaded_files'# path to the uploaded folder to save the files. Path from main.py to upoladed_files
file_to_html =  '../static/uploaded_files' #path to pass to html file, this path + filename will inform the url to the html go take it

@views.route('/')
def index():

    carousel = Post.query.filter(Post.carousel == 1).all()
    return render_template('index.html', posts=carousel, user=current_user)


@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)


@views.route('/recipes', methods=['GET', 'POST'])
def recipes():

    if request.method == 'POST':
        # Get the only one or the multiple files from html
        files = request.files.getlist['file[]']
        description = request.form.get('recipe_description')
        title = request.form.get('recipe_title')

        file_names = []
        path_html = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file)
                file_names.append(filename)
                path_save = os.path.join(upload_folder, filename)
                file.save(path_save)
                path_html.append(os.path.join(file_to_html, filename))
            else:
                flash('Allowed image types are -> png, jpg, jpeg', category='error')
                return redirect('views.recipes')

        post = Post(carousel=0, description=description, filename=filename, img_path=path_html, title=title, user_id=current_user.get_id()) 
        db.session.add(post)
        db.session.commit()
    
    img = Post.query.filter(Post.carousel == 0).all()
    
    print(len(img))
    print(current_user.get_id())
    return render_template('recipes.html', imgs_uploaded = img, user=current_user)
