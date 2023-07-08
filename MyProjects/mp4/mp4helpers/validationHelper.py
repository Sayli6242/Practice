
import re

from datetime import datetime

def validate_input(input_value, pattern):
    if re.match(pattern, input_value):
        return True
    else:
        return False

        
def check_number_in_range(number,lst_len):
    if number >= 1 and number <= lst_len:
        return True
        
    else:
        return False


def check_name_validation(book_title):
    pattern = r'^[a-zA-Z ]+$'
    return validate_input(book_title, pattern)
    
# where r means raw string
def check_validation_of_provide_ID(id):
    pattern = r'^[A-Za-z0-9]+$'
    return validate_input(id, pattern)

def check_ISBN_validation(ISBN_number):
    pattern = r'^\d{10}$|^\d{13}$'
    return validate_input(ISBN_number, pattern)



def check_year_validation(publication_year):
    if publication_year >= 0 and publication_year <= 9999:
        return True
    else:
        return False


def check_phone_validation(member_contact):
    if len(str(member_contact)) >= 1 and len(str(member_contact)) <= 10:
        return True
    else:
        return False

def check_amount_validation(amount):
    if amount > 0:
        return True
    else:
        return False

def validate_due_date(date_string):
    try:
        due_date =  datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_id(user_id):
    if user_id.isdigit():
            return int(user_id)
    else:
        print('Invalid input. Please enter a valid numeric value.')
    
def validate_choice(dict_name):
    try:
        if choice in dict_name:
            return choice
        else:
            print('Invalid choice. Please enter a valid option number.')
    except ValueError:
            print('Invalid input. Please enter a valid option number.')