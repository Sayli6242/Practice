"""
Take input of age of N (any number of) people by user and determine oldest and youngest among them.
Input - N number of.people ( 0< N < 20)
 Output - Print age of youngest and oldest
"""
"""
1.take input of number of people N is length of given array
2.apply for loop to take limit upto N
3.take input of age of those people 
4.store age of those people in array
4.
5.

"""


N = int(input('enter number of people '))
ages = []
for i in range(N):
    age = int(input('enter the age '))
    ages.append(age)

# TODO: find min and max number

# arr = arr.append(y)