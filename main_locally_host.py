import os

from flask_program import creat_app

app = creat_app()

if __name__ =="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))

#A main file to make it easier to run locally.
