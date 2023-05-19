import re

def validate_input(input_value, pattern):
    if re.match(pattern, input_value):
        return True
    else:
        return False


def validate_input(input_value, pattern):
    if re.match(pattern, input_value):
        return True
    else:
        return False


def check_name_validation(value):
    pattern = r'^[a-zA-Z ]+$'
    return validate_input(value, pattern)


def check_validation_of_memberID(value):
    pattern = r'^[A-Za-z0-9]+$'
    return validate_input(value, pattern)



def check_ISBN_validation(value):
    pattern = r"^(?:ISBN(?:-13)?:?\s?)?(?=[0-9]{13}$|(?=(?:[0-9]+[-\s]){4})[-\s0-9]{17}$)[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+$"
    return not validate_input(value, pattern)