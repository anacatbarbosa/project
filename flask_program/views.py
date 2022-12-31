# File to code @app.route files, but not authentication files routes, such as login and register.
import json
import os
import random
from datetime import datetime

from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, session, url_for)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import db
from .helpers import allowed_file, get_random_list, json_to_js, str_to_list
from .models_database import Post, User

# Blueprint that allows to code the views, or @app.routes, in multiple files

# Setting the Blueprint variable name.
views = Blueprint('views', __name__)

# Path to the uploaded folder to save the files. Path from main.py to upoladed_files
upload_folder = 'flask_program/static/uploaded_files/'

 # Path to pass to html file, this path + filename will inform the url to the html go take it
file_to_html =  '../static/uploaded_files'

# If the user searches for the blank URL is redirected to home
@views.route('/')
def star():
    return redirect('/home')


@views.route('/home')
def index():

    # Max number of images to show randomic in carousel
    max_carousel_display = 5

    # Max number of recipes to show randomic after the carousel
    max_recipes_display = 4

    # Getting post information
    carousel = Post.query.filter(Post.carousel == 0).all()

    # Selecting random posts to display
    random_amount = len(carousel)

    # List to store the path to the carousel information
    carousel_path = []
    carousel_title = []
    carousel_id = []
    
    # List to store the path to the random recipes information
    recipes_path = []
    recipes_title = []
    recipes_id = []

    # The get_random_list will make sure the random numbers won't exceed the Max_*_display and the quantity of recipes it has on db as well
    random_posts = get_random_list(random_amount, max_carousel_display)
    random_recipes = get_random_list(random_amount, max_recipes_display)

    # These for loops will pass the informations to the lists.
    for i in random_posts:
        hold = str_to_list(carousel[i].filename)
        carousel_title.append(carousel[i].title)
        carousel_id.append(carousel[i].id)
        carousel_path.append(hold[0])

    for i in random_recipes:
        hold = str_to_list(carousel[i].filename)
        recipes_title.append(carousel[i].title)
        recipes_id.append(carousel[i].id)
        recipes_path.append(hold[0])

    # Loading random recipes to the show after carousel
    return render_template('index.html', carousel_highlights=carousel_path, user=current_user, post_title=carousel_title, post_id=carousel_id,
                            recipes_highlights=recipes_path, recipes_title=recipes_title, recipes_id=recipes_id)


# Render the about page
@views.route('/about')
def about():
    return (render_template('about.html', user=current_user))


# Render the about general recipes page
@views.route('/recipes', methods=['GET', 'POST'])
def recipes():

    # Post will be called when the logged user uploads a file
    if request.method == 'POST':
        # Get the inputs from html
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
        
        # Stores all the file names from user
        file_names = []

        # Stores the path to use into the html 
        path_html = []

        # Go through the files to check if the file name is secure, and save all the images at static/uploaded_files 
        for file in files:
            if file and allowed_file(file.filename):

                # Datatime.now() is used to keep all files with a different name, allows the users uplaod files with the same name, avoid error like two peoplo posting a recipe with
                # Same file name, e.g. two peoplo posting a recipe of chocolate cake and upload different files with the same name "chocolate_cake.jpg"
                filename = secure_filename(str(datetime.now()) + file.filename) 
                file_names.append(filename)
                path_save = os.path.join(upload_folder, filename)
                file.save(path_save)
                path_html.append(os.path.join(file_to_html, filename))
            else:
                flash('Allowed image types are -> png, jpg, jpeg', category='error')
                return redirect(url_for('views.recipes'))

        # Add all the posts information to the database
        post = Post(carousel=0, description=description, filename=str(file_names), img_path=str(path_html), title=title, user_id=current_user.id) 
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
    
    # Confirm if the recipe really exists, avoid unkown url recipes
    myfile = upload_folder + post_path[0]
    if os.path.isfile(myfile) == False:
        return redirect(url_for('views.recipes'))
    
    # Calc the number of buttons in carousel, showing the number of buttons as the number of images
    carousel_buttons = len(post_path)

    return render_template('recipe_details.html', user=current_user, page_title=str(post_title), carouselimg = post_path, post_info = post, carousel_buttons=carousel_buttons)


@views.route('/get_posts/<string:address>', methods=['POST'])
def get_posts(address):
    
    # Get user info
    user_info = User.query.filter(User.id == current_user.get_id()).first()
    post_info = Post.query.filter(Post.carousel == 0).all()

    # Post_info = recipes titles and descriptions
    if user_info != None:
        if address == "profile" and user_info.adm_bool == 0:
            post_info = Post.query.filter(Post.user_id == current_user.id).all()

    # Post_thumb = first image from the uploads to use as a thumbnail
    post_thumb = []

    for i in post_info:
        hold = str_to_list(i.img_path)
        post_thumb.append(hold[0])

    # If it has a logged user, pass the user id and if the user or not an adm. json_to_js will parse that data to a dict
    # That will jsonify the data for the index.js infinityScroll
    if user_info == None:
        data = json_to_js(post_thumb, post_info, None, None)
    else:
        data = json_to_js(post_thumb, post_info, user_info.id, user_info.adm_bool)
    
    # Returns to JS file.
    return jsonify(data)


@views.route('/delete_post', methods=['POST'])
def delete_post():

    # Get the resquested data from index.js - Post ID
    post = json.loads(request.data)
    postId = post['postId']

    # Get user information
    user_info = User.query.filter(User.id == current_user.get_id()).first()

    # Get the column needed to drop
    post = Post.query.get(postId)


    # All the images to delete from the db and the computer
    post_info = Post.query.filter(Post.id == postId).first()
    if post:
        if post.user_id == user_info.id or user_info.adm_bool == 1:
            
            # Parse the str list format to a real list
            list_delete = str_to_list(post_info.filename)

            # Delete images one by one
            for i in list_delete:
                # Myfile receive = path to the uploaded_files + image name
                myfile = upload_folder + i

                # Tells os it is a file to delete it 
                os.remove(myfile)
            
            # Delete the column from db
            db.session.delete(post)
            db.session.commit()
    
    # Return an empty result 
    return jsonify({})
