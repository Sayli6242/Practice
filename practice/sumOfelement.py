
"""
Write a program to find the sum of all elements of a list.

"""
from functools import total_ordering


def get_user_input():
    x = int(input('enter the values: '))
    lst = [ ]
    for i in range(x):
        y = int(input(f'enter elements for list{i}: '))
        lst.append(y)
    return lst

def sum_of_all_elements_in_list(lst):
    total = 0
    for i in range(0,len(lst)):
        total = total + lst[i]
    return total
 
def main():

   lst = get_user_input()
   total= sum_of_all_elements_in_list(lst)
   print('this is the sum of all elements in list',total)

main()