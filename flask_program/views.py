#File to code @app.route files, but not authentication files routes, such as login and register.
import json
import os
import random
from datetime import datetime

from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, session, url_for)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import db
from .helpers import allowed_file, json_to_js, str_to_list
from .models_database import Post, User

#Blueprint allow to code the views, or @app.routes, in multiple files

views = Blueprint('views', __name__) #setting the Blueprint variable name.
upload_folder = 'flask_program/static/uploaded_files'# path to the uploaded folder to save the files. Path from main.py to upoladed_files
file_to_html =  '../static/uploaded_files' #path to pass to html file, this path + filename will inform the url to the html go take it

@views.route('/')
def index():

    # Max number of images to show randomic in carousel
    max_carousel_display = 5
    # Getting post informations
    carousel = Post.query.filter(Post.carousel == 0).all()
    # Selecting randons posts to display
    random_amount = len(carousel)
    # List to store the path to the carousel images
    carousel_path = []

    if random_amount >= max_carousel_display:
        random_posts = random.sample(range(random_amount), max_carousel_display)
    else:
        random_posts = random.sample(range(random_amount), random_amount)

    for i in random_posts:
        hold = str_to_list(carousel[i].filename)
        carousel_path.append(hold[0])
    
    return render_template('index.html', carousel_highlights=carousel_path, user=current_user)


@views.route('/about')
def about():
    return (render_template('about.html', user=current_user))


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
        
        # Store all the file names from user
        file_names = []
        # Store the path to use into the html files to find the img
        path_html = []
        # Go through the files to check if the file name is sercure, and save all the images at static/uploaded_filles 
        for file in files:
            if file and allowed_file(file.filename):
                # Datatime.now() is used to keep all files with a different name, allows the users uplaod files with the same name, avoid error like two peoplo posting a recipe of ...
                # ... name, avoid error like two peoplo posting a recipe of chocolate cake and upload different files with the same name "chocolate_cake.jpg"
                filename = secure_filename(str(datetime.now()) + file.filename) 
                file_names.append(filename)
                path_save = os.path.join(upload_folder, filename)
                file.save(path_save)
                path_html.append(os.path.join(file_to_html, filename))
            else:
                flash('Allowed image types are -> png, jpg, jpeg', category='error')
                return redirect(url_for('views.recipes'))

        # add all the posts informations to the database
        post = Post(carousel=0, description=description, filename=str(file_names), img_path=str(path_html), title=title, user_id=current_user.get_id()) 
        db.session.add(post)
        db.session.commit()
    
    return render_template('recipes.html', user=current_user)


# This route will receive the information of which recipe the user clicked on and show the recipe, it will have all the images uploaded and the description of it
@views.route('/recipes/<string:post_title>/<string:post_id>', methods=['GET','POST'])
def recipes_pag(post_title, post_id):
    post = Post.query.filter(Post.id == post_id).first()
    if post == None:
        return redirect(url_for('views.recipes'))

    post_path = str_to_list(post.filename)
    
    for i in post_path:
        print (i)
    return render_template('recipe_details.html', user=current_user, page_title=str(post_title), carouselimg = post_path, post_info = post)


@views.route('/get_posts', methods=['POST'])
def get_posts():

    # Post_info = recipes titles and descriptions
    post_info = Post.query.filter(Post.carousel == 0).all()
    # Get user info
    user_info = User.query.filter(User.id == current_user.get_id()).first()
    # Post_thumb = first image from the uploads to use as a thumbnail
    post_thumb = []

    for i in post_info:
        hold = str_to_list(i.img_path)
        post_thumb.append(hold[0])

    if user_info == None:
        data = json_to_js(post_thumb, post_info, None, None)
    else:
        data = json_to_js(post_thumb, post_info, user_info.id, user_info.adm_bool)
    
    # Returns to JS file.
    return jsonify(data)

@views.route('/delete_post', methods=['POST'])
def delete_post():
    post = json.loads(request.data)
    postId = post['postId']
    post = Post.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()

    return jsonify({})