#File to code @app.route files, but not authentication files routes, such as login and register.
import os

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import db
from .helpers import allowed_file, json_to_js, str_to_list
from .models_database import Post, User

#Blueprint allow to code the views, or @app.routes, in multiple files

views = Blueprint('views', __name__) #setting the Blueprint variable name.
upload_folder = 'flask_program/static/uploaded_files'# path to the uploaded folder to save the files. Path from main.py to upoladed_files
file_to_html =  '../static/uploaded_files' #path to pass to html file, this path + filename will inform the url to the html go take it
number_test = 0

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
        files = request.files.getlist('files[]')
        description = request.form.get('recipe_description')
        title = request.form.get('recipe_title')

        # Check if title or description are empty
        if title == "":
            flash('A recipe needs a title as beautiful as the food!', category='error')
            return redirect(url_for('views.recipes'))
        if description == "":
            flash('Please insert a description, we need to know how to cook that delicious recipe!', category='error')
            return redirect(url_for('views.recipes'))
            
        file_names = []
        path_html = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_names.append(filename)
                path_save = os.path.join(upload_folder, filename)
                file.save(path_save)
                path_html.append(os.path.join(file_to_html, filename))
            else:
                flash('Allowed image types are -> png, jpg, jpeg', category='error')
                return redirect(url_for('views.recipes'))

        post = Post(carousel=0, description=description, filename=str(file_names), img_path=str(path_html), title=title, user_id=current_user.get_id()) 
        db.session.add(post)
        db.session.commit()
    
    # Post_info = recipes titles and descriptions
    post_info = Post.query.filter(Post.carousel == 0).all()
    # Post_thumb = first image from the uploads to use as a thumbnail
    post_thumb = []
    for i in post_info:
        hold = str_to_list(i.img_path)
        post_thumb.append(hold[0])

    json_to_js(post_thumb, post_info)
    
    return render_template('recipes.html', post_info = post_info, user=current_user, post_thumb = post_thumb)