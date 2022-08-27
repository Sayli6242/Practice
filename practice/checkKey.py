"""
Write a Python script to check whether a given key already exists in a dictionary.
1. initialise a dict
get input from user - which key to find
chech if key is present (dict.get(key,"not found") dict[key])
"""


dict = {5,1,2,4,6,3,7,51,46}
def check_given_key_present_in_dictionary(dict):
    
    z = int(input('enter the number'))

    for i in range(len(dict)): 

        if z == dict[i]:

            return True
        else:
            return False


def main():
  
    result = check_given_key_present_in_dictionary(dict)
    if result == True:
        print('number is present in dict')
    else:    
        print('number is not present in dict')

    
    


main()