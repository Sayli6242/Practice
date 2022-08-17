'''
program to print absolute value of a number
if user enters 10 output is 10, if user enters -10 output is 10
Input - number ( ex -1)
Output - absolute value output (ex 1 )

'''
"""
1.Take input from user
2.apply condition if n is less than zero then by dividing n to -1
3.reassign value to n
4. print result 

"""



x = int(input('enter the number'))
result =0
if x < 0:
    x = (-1) * x
print(x)