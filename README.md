# Project Com Amor, Graça
 CS50 Final project, recipes web app where users can see and share recipes while having their own profile and being able to manage all their data.

# Necessary to run locally.
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

https://flask.palletsprojects.com/en/2.2.x/

https://flask-login.readthedocs.io/en/latest/

https://www.python.org/downloads/

If you already have pip installed it's possible to just run:
pip install -r flask_program/requirements.txt

# To run only in PC.
command: python3 main.py

# To run as local network host
command: python3 main_locally_host.py #to run hosting into your local network using a 5000 port, it's possible to change the port at the file main_locally_host.py at "app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', XXXX)))" Where XXXX = port number - Please be careful and don't trust unknown domains or public networks, stay safe.

# About this project
You can find the inspiration behind this project on the 'About' page of this project. 
It was created and developed as a team, always analyzed and discussed, so it would become exactly what we pictured.
## HTML
index.html - our website's homepage. It contains a carousel with images uploaded by the users and below a few random recipe links below that when clicked will redirect the user to those recipes.

about.html - where we explain how the project was born and why. The inspiration and the people behind it. It's composed by only a short text with a picture of the developers.

login.html - two forms; one to login if the user has an account, one to register if the user doesn't have an account but wants to. Aand a cute cupcake image!

recipes.html - an infinity scroll page with all recipes uploaded by users. if the user is logged in, there will be a form at the top so a new recipe can be added, if the user is not logged in, no form will show.

recipe_details.html - when you click any recipe on the website, you will be redirected to the respective recipe's page. It includes images of the recipe and the title and text of how to prepare that recipe.

profile.html - users account interface. It will render an infinity scroll page of all the recipes the user uploaded, and there's a side navigation where they can change username, password and e-mail.

All these pages have the same navigation bar and footer. The navigation bar consists of all these links with the option of 'Profile' and 'Log Out' when logged in, and without them if not. The footer consists of our social networks and a copyright.

## CSS

style.css - general styling of common elements all webpages have. That includes the scrollbar, navigation and footer, body general settings, alerts, header styles, the carousel style for the homepage, hover effects and their responsive behavior with three different max-width so it would look great on any screen :)

about.css - as the name suggests, styling of the about.html page. Our shorter CSS file since it's not a page that the user can interact with and also the one with less elements. Just a few rules to make both text and the image look well positioned and also responsive. We don't want our page to look like our Word documents look after we move an image, do we?

login.css - all forms present on our project are styled the same, and here was when we styled the first forms (login and registration). This CSS file contains mainly form stylization since the login page is composed by two forms. 

recipes.css - where we styled the form for adding a recipe and how the recipe list would look. With the help of flexbox and some minimalist hover effects, we were able to organize our recipes (while also making it responsive).

profile.css - once more, flexbox comes to the rescue and helps us with dividing the user profile page with a vertical menu on the left side of the page, and the corresponding dynamic response to each menu button on the right side. We also used the same stylization on the users recipes from recipes.css to keep things neat and tidy (and... responsive!)

## Javascript

index.js -

profile.js -

error.js -
## Python

__init__.py - 

auth.py - 

helpers.py -

models_database.py -

views.py -

main_locally_host.py -
 
main.py -

## SQL

database.db - 
# Credits:
Menu icons created by Freepik - Flaticon https://www.flaticon.com/free-icons/menu 
Big thanks to: https://www.youtube.com/@TechWithTim

