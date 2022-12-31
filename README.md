# Project Com Amor, Graça
 CS50 Final project, recipes web app where users can see and share recipes while having their own profile and being able to manage all their data.

 # Video Demo URL
 https://youtu.be/2o3cHpEI1pE

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

#All files explained
## HTML
index.html - our website's homepage. It contains a carousel with images uploaded by the users and below a few random recipe links below that when clicked will redirect the user to those recipes.

about.html - where we explain how the project was born and why. The inspiration and the people behind it. It's composed by only a short text with a picture of the developers.

login.html - two forms; one to login if the user has an account, one to register if the user doesn't have an account but wants to. Aand a cute cupcake image!

recipes.html - an infinity scroll page with all recipes uploaded by users. if the user is logged in, there will be a form at the top so a new recipe can be added, if the user is not logged in, no form will show.

recipe_details.html - when you click any recipe on the website, you will be redirected to the respective recipe's page. It includes images of the recipe and the title and text of how to prepare that recipe.

profile.html - users account interface. It will render an infinity scroll page of all the recipes the user uploaded, and there's a side navigation where they can change username, password and e-mail.

All these pages have the same navigation bar and footer. The navigation bar consists of all these links with the option of 'Profile' and 'Log Out' when logged in, and without them if not. The footer consists of our social networks and a copyright.

## CSS

style.css - general styling of common elements all webpages have. That includes the scrollbar, navigation and footer, body general settings, alerts, header styles, the carousel style for the homepage, hover effects and their responsive behavior with different screen sizes so it would look great on almost any screen :)

about.css - as the name suggests, styling of the about.html page. Our shorter CSS file since it's not a page that the user can interact with and also the one with less elements. Just a few rules to make both text and the image look well positioned and also responsive. We don't want our page to look like our Word documents look after we move an image, do we?

login.css - all forms present on our project are styled the same, and here was when we styled the first forms (login and registration). This CSS file contains mainly form stylization since the login page is composed by two forms. 

recipes.css - where we styled the form for adding a recipe and how the recipe list would look. With the help of flexbox and some minimalist hover effects, we were able to organize our recipes (while also making it responsive).

recipe_details.css - with the help of flexbox we stylized each individual recipe page with a carousel composed of the uploaded images from the user and the respective recipe on it's side. It follows the same style rules as the rest of the website and let's just say making a carousel responsive is not an easy task... but we made it!

profile.css - once more, flexbox comes to the rescue and helps us with dividing the user profile page with a vertical menu on the left side of the page, and the corresponding dynamic response to each menu button on the right side. We also used the same stylization on the users recipes from recipes.css to keep things neat and tidy (and... responsive!)

## Javascript

index.js - the first and main JavaScript file. It's where we implemented infinity scroll functions, how many recipes to show first, and how many to load during scroll on recipes.html. It's also where we implemented the delete post function and where we fetch the necessary data with fetchData function to display on our recipes page. (If in need of guidance, check the comments on the code where we explain the different objectives of each part!)

profile.js - where we made the user interface from profile.html dynamic. With the help of getElementbyId we fetched all the clickable buttons and added, on click, the necessary HTML to show each form. User can change name, e-mail and password. By fetching the <div> where all the HTML info would be rendered, all we had to do was render different HTML forms for each button!

error.js - there was this little bug on recipes where on post deletion it would still redirect the user to the recipe page when clicking on the delete button despite it being, well, deleted. This file prevents that from happening by redirecting the user to the recipes.html page in case the recipe is no longer in our database.
## Python

__init__.py - where the app is created using a random secret key and all its configurations. It's configurated to create the database if it's non-existant otherwise it just accesses the existant one for the website's functionalities. All the processes are explained in comments throughout all the code. Sets flask configurations and handles the 404 error.

auth.py - it handles login, logout, register, profile and credentials updates. If with admin privelege, the admin can also add a new admin. You can also find a detailed orientation regarding these processes on the code file comments.

helpers.py - contains helping functions for the other python files. Similar to helpers.py on CS50's finance project. Helpers.py contains check_email, check_password_requirements, flash_all, check_errors, allowed_file, str_to_list, json_to_js, get_random_list. As the other coding files, you have helping comments on each of these functions explaining what they do!

models_database.py - used database models for user and posts (it contains all user and recipes information respectively). Information such as ids, names, file names, etc.

views.py - it handles homepage, about, recipes, recipe_details, infinity scroll for recipes.html and profile.html, and delete post function. On a short explanation, views.py handles the webpages where no security authentication is necessary, while auth.py handles the pages and functionalities present when the user is authenticated.

main_locally_host.py - file to make the flask server easier to run hosting it on a local network (according to flask documentation, not safe to use for production. Don't use it on a public or unknown network, please stay safe!)
 
main.py - file to make the app run easier, on PC. Avoiding long terminal commands, the web app can be run with just python3 main.py or python3 main_locally_host.py (please remember the latter one should NOT be used in public or unknown networks).

## SQL

database.db - contains two tables, one for user information, one for post information. User table is composed by id, adm_bool (check if user is admin), email, password, name and posts. Post table is composed by id, carousel, description, date, filename, img_path, title, user_id. User table is connected to Post table through posts.

## General Files

colors.txt - contains our website and logo colors.

static_imgs folder - images used on our website, like the logo and the cupcakes on the login/register page. 

uploaded_files - images uploaded by users.
# Credits:
Menu icons created by Freepik - Flaticon https://www.flaticon.com/free-icons/menu 

Fonts used - https://fonts.google.com/

Our savior - https://getbootstrap.com/

Our bibles - https://stackoverflow.com/
             https://www.w3schools.com/
             https://cs50.harvard.edu/x/2022/
             https://www.geeksforgeeks.org/

Honorable mention to - https://www.google.com

Big thanks to: https://www.youtube.com/@TechWithTim

# Dedicated to

This is, in fact, a lot more than our final CS50x final project. We started the CS50x course shortly after Leo's dad, Renato Silva, passed away. And like we described on our About Us page, this project was named after my aunt Graça Machado who passed 5 years ago, and who taught me how to cook. 
From April (when we started the course) to today (the 31st of December), we doubted far too many times if we would be able to finish or even do a Final Project worth submitting.
We would like to dedicate this project to them, Renato who was known for his amazing grill skills and seasoning gifts and even better dad skills, and Graça, the best pastry chef in town, while also being, like her desserts, the sweetest aunt and human being one could ever meet.
Love you always,

Catarina & Leonardo