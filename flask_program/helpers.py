import json
import random
import re

from flask import flash

from . import db
from .models_database import User

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Checking if the e-mail is valid using re, https://docs.python.org/3/library/re.html
def check_email(email): 
    regex =  '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]\w{2,3}$' 
    if re.search(regex2,email) or re.search(regex,email):   
        return True  
    else:   
        return False

def check_password_requirements(password):
    # Dict with all password requirements needed set as false
    password_need = {
        'letter': False,
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'special_char': False,
        'len': False
    }

    # Set the dict value to True if it has the requierements - they are: At least 8 digits, one number, one special char, one lowercase and one uppercase letter
    if len(password) > 7:
        password_need['len'] = True
    for char in password:
        if char.isnumeric():
            password_need['number'] = True
        if char.isalpha():
            password_need['letter'] = True
        if not char.isalnum():
            password_need['special_char'] = True
        if char.isupper():
            password_need['uppercase'] = True
        if char.islower():
            password_need['lowercase'] = True

    # If one or more of the values is False returns the dict to flash the current messages
    for error in password_need: 
        if password_need[error] == False:
            return password_need
    
    # If everything goes fine return sucess
    return 'success'
 
# Flash the error messages according to the dict given from check_password_requirements
def flash_all(password_errors): 
    if password_errors['len'] == False:
        flash('The password must contain at least 8 digits.', category='error')
    if password_errors['letter'] == False:
        flash('The password must contain at least 1 Letter.', category='error')
    if password_errors['number'] == False:
        flash('The password must contain at least 1 number.', category='error')
    if password_errors['special_char'] == False:
        flash('The password must contain at least 1 special character ex: !"#$%&/()?,.', category='error')
    if password_errors['uppercase'] == False:
        flash('The password must contain at least 1 uppercase letter.', category='error')
    if password_errors['lowercase'] == False:
        flash('The password must contain at least 1 lowercase letter.', category='error')


# Check_error will be used in multiple files, for different reasons. If one of the arguments is explicitly False, it will skip the verification
# e.g. The check_errors will be used at change_e-mail as well, so the code won't check the name and password
def check_errors(name, email, password1, password2):
    errors = 0
    if name == False:
        pass
    elif len(name) < 2:
        flash('Name must be greater than 1.', category='error')
        errors += 1
    
    if email == False:
        pass
    elif not check_email(email):
        flash('Invalid E-mail.', category='error')
        errors += 1

    # check_password_requirements is a function that returns 'success' or a dictionary that contains all the errors with a value False. 
    if password1 == False:
        pass    
    elif check_password_requirements(password1) != 'success':
        # flash_all gets the dict returned by check_password_requirements and flashes all the errors
        flash_all(check_password_requirements(password1))
        errors += 1
    elif password1 != password2:
        flash('Passwords do not match. Please try again.', category='error')
        errors += 1
    return errors

# https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/#a-gentle-introduction
def allowed_file(filename): 
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Func to receive a list in a str format and return as a true list, ex: receive a str - "['test', 'hi']" and return a list - ['test', 'hi']
# If no str pass return an empty list, if an incorrect format value is passed return none
def str_to_list(string):
    list_to_return = []
    item_to_append = ''
    # if str is not a string return None
    if type(string) != type(str()):
        return None

    # If str is empty or an empty list, return an empty list
    if string == '' or string == '[]':
        return list_to_return
    
    # Going through the string to check where is the '[', ']' and the items inside of it

    quote_one = 0 # Check if the forloop found the first quote, after the first quote it will add all to the item_to_append
    quote_two = 0 # Check if the forloop found the second quote, after the second quote it will add the item_to_append to the list_to_returns

    for char in string:
        if char == "'" and quote_one == 0:
            quote_one = 1
            quote_two = 0

        elif char == "'" and quote_one == 1:
            quote_one = 0
            quote_two = 1

        elif quote_one == 1:
            item_to_append += char

        if quote_two == 1:
            list_to_return.append(item_to_append)
            item_to_append = ''
            quote_two = 0

    return list_to_return


# This function will write or edit a json file to give the infinity scroll the necessary informations
def json_to_js(path, posts, current_user_id, adm_bool):
    # Opening and reading what is at json file to find how many times we already called the function infinity scroll. The variable counter informs what is the last image we have stopped at,
    # the counter always starts at 9, the standard output recipes. If the user scrolldown we show six more.
    # If the len(path) is lower or equal to 0, it's not necessary to show more, so it doesn't change the json file
    if len(path) == 0:
        return None

    # Posts must have an id, img_path and title
    data = {
        "path":[],
        "titles":[],
        "post_id":[],
        "user_id": [],
        "adm": []
    }
    counter = 0
    path_to_add = []
    titles_to_add = []
    id_to_add = []
    user_id = []

    for post in posts:
        path_to_add.append(path[counter])
        titles_to_add.append(post.title)
        id_to_add.append(post.id)
        user_id.append(post.user_id)
        counter += 1

    data['path'] = path_to_add
    data['titles'] = titles_to_add
    data['post_id'] = id_to_add
    data['user_id'] = user_id
    data['current_user'] = current_user_id
    data['adm'] = adm_bool

    # Returns a dict to the js file.
    return data


# Returns a list of random numbers depending of the max quantity
# max_quantity = Quantity of random numbers to look for in range(range_random)
# If the range_random is lower than max_quantity then max_quantity = range_random
def get_random_list(range_random, max_quantity):

    random_list = []
    if range_random >= max_quantity:
        random_list = random.sample(range(range_random), max_quantity)
    else:
        random_list = random.sample(range(range_random), range_random)

    return random_list