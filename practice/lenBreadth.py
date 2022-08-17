"""
Take values of length and breadth of a rectangle from user and check if it is square  or not.

1.take two input from user 
2.store it in a variables
3.convet into integer
3.apply condition if length is equal to breadth then it is square 
4.else this is not square
5.print result

"""

l = int(input('enter length'))
b = int(input('enter breadth'))
result = 0
if l == b:
    print('this is square')
else:
    print('this is not square')
