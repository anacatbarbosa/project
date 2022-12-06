import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

#configure app name
app = Flask(__name__)

#template auto-reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Setting session to use filesystem 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/')
def index():
    return render_template("index.html") 
