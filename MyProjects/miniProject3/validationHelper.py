
import re

def validate_input(input_value, pattern):
    if re.match(pattern, input_value):
        return True
    else:
        return False



def check_name_validation(book_title):
    pattern = r'^[a-zA-Z ]+$'
    return validate_input(book_title, pattern)
# where r means raw string
def check_validation_of_memberID(member_id):
    pattern = r'^[A-Za-z0-9]+$'
    return validate_input(member_id, pattern)

def check_ISBN_validation(ISBN_number):
    pattern = r'^(?:ISBN(?:-13)?:?\s?)?(?=[0-9]{13}$|(?=(?:[0-9]+[-\s]){4})[-\s0-9]{17}$)[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+$'
    return validate_input(ISBN_number, pattern)



def check_year_validation(publication_year):
    return check_range_validation(publication_year, 0, 9999)


def check_phone_validation(member_contact):
    return check_range_validation(member_contact, 1, 10)