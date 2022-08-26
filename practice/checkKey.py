"""
Write a Python script to check whether a given key already exists in a dictionary.
1. initialise a dict
get input from user - which key to find
chech if key is present (dict.get(key,"not found") dict[key])
"""


def to_get_user_input():
    x = int(input('enter given for in list'))
    lst = [ ]
    for i in range(x):
        y = int(input(f'enter list values {i}: '))
        lst.append(y)
    return lst



def check_given_key_present_in_list(lst):
    
    z = int(input('enter the number'))

    for i in range(len(lst)): 

        if z == lst[i]:

            return True
        else:
            return False


def main():
    lst = to_get_user_input()
    result = check_given_key_present_in_list(lst)
    if result == True:
        print('number is present in list')
    else:    
        print('number is not present in list')

    
    


main()