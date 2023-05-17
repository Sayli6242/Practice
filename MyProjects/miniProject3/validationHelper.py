
import re


def check_name_validation(Book_title):
    pattern = r'^[a-zA-Z ]+$'
    if re.match(pattern, Book_title):
        return True
    else:
        return False

def check_validation_of_memberID(MemberID,book_ID):
    pattern = r'^[A-Za-z0-9]+$'

    if re.match(pattern, MemberID,book_ID):
        return True
    else:
        return False

def check_year_validation(Publication_year):
    if Publication_year < 0  or Publication_year > 9999:
        return False    
    else:
        return True     

def check_ISBN_validation(ISBN_number):
    if ISBN_number ==  (r"^(?:ISBN(?:-13)?:?\s?)?(?=[0-9]{13}$|(?=(?:[0-9]+[-\s]){4})[-\s0-9]{17}$)[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+$"):
        return False
    else:
        return True

def check_phone_validation(member_contact):
    if member_contact >= 1 and member_contact <= 10:
        return False     
    else:
        return True