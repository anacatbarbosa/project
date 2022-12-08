#File to code @app.route files, but not authentication files routes, such as login and register.
import os

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
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
    return render_template('index.html')




@views.route('/test', methods=['GET', 'POST'])
def test():

    if request.method == 'POST':
        pic = request.files['file']

        if not pic:
            return 400;
        
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        upload_folder = 'flask_program/static/uploaded_files'
        path_save = os.path.join(upload_folder, filename)
        pic.save(path_save)
        path_html = os.path.join(pic_to_html, filename)
        post = Post(img_path=path_html, filename=filename, mimetype=mimetype, user_id=1)
        db.session.add(post)
        db.session.commit()
    
    img = Post.query.filter(Post.user_id == 1).all()
    return render_template('test_img.html', imgs_uploaded = img)
