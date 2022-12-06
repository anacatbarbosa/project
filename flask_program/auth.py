#File to code authentication files routes, such as login and register.
from flask import Blueprint, flash, redirect, render_template, request, session, url_for #Blueprint allow to code the views, or @app.routes, in multiple files

auth = Blueprint('auth', __name__) #setting the Blueprint variable name.

