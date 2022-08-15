""" 
    check if number is odd or even
    input - a number
    Output - True or False (true if even false if odd)
"""


"""
1. take input from user
2. store them in variables
3. convert them into integer
4. apply condition if 2 modulus n is equal to 0 then it is even number
5. aplly condition else 2 modulus n is not equal to 0 then it is odd number
6. print result
"""

def check_even_odd_int(x):
    if x % 2 == 0:
       return True
    else:
       return False

def get_user_input():
    x = int(input('enter a number'))
    result =  check_even_odd_int(x)
    print(result)

get_user_input()
