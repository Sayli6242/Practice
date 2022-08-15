"""
Find greatest of three numbers (without using any built in python functions)
input - 3 numbers
output - greatest of three numbers
"""
"""
1.intialize three numbers
2.convert it into int
3.store it in a variables
4.apply if condition x is greater than y and z
5.again apply if condition y is greater than x and z
6.again apply if condition z is greater than x and y
7.check condition wheather true of false
8.print result

"""



def max_num(x, y, z):
    if x > y  and  x > z:
        return x
    if y > z  and  y > x:
        return y
    if z > x  and  z > y:
        return z

def get_user_input_find_max_num():

    x = int(input('Enter 1st num'))
    y = int(input('Enter 2st num'))
    z = int(input('Enter 3st num'))
    res = max_num(x, y, z)
    print(res)
    
get_user_input_find_max_num()

