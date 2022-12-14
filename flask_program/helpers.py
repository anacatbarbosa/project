import re

from flask import flash


def check_email(email): # checking if the e-mail is valid using re, https://docs.python.org/3/library/re.html
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

    # Set the dict value to True if has the requierements - are they: At least 8 digits, one number, one special char, one lowercase and one uppercase letter
    if len(password) > 7:
        password_need['len'] = True
    for char in password:
        if char.isnumeric():
            password_need['number'] = True
        if char.isalpha():
            password_need['letter'] = True
        if not char.alnum():
            password_need['special_char'] = True
        if char.isupper():
            password_need['uppercase'] = True
        if char.islower():
            password_need['lowercase'] = True

    # if one or more of the values is False returns the dict to flash the current messages
    for error in password_need: 
        if password_need[error] == False:
            return password_need
    
    # if everything goes fine return sucess
    return 'success'
 
# Flash the error messages according to the dict given from check_password_requirements
def flash_all(password_errors): 
    if password_errors['number'] == False:
        flash('The password must contain at least 8 digits.', category='error')
    if password_errors['letter'] == False:
        flash('The password must contain at least 1 Letter.', category='error')
    if password_errors['special_char'] == False:
        flash('The password must contain at least 1 special character ex: !"#$%&/()?,.', category='error')
    if password_errors['uppercase'] == False:
        flash('The password must contain at least 1 uppercase letter.', category='error')
    if password_errors['lowercase'] == False:
        flash('The password must contain at least 1 lowercase letter.', category='error')
