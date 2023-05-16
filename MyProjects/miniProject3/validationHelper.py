
def check_name_validation(name):
    pattern = r'^[a-zA-Z ]+$'
    if re.match(pattern, name):
        return True
    else:
        return False

def check_phone_validation(phone):

    pass

    