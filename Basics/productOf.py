"""
 Write a program to find the product of all elements of a list.
 input - input - take dynamic (any) number of elements
 output - product of all elements


"""

def get_user_input():
    x = int(input('enter length of list'))
    lst = [ ]
    for i in range(x):
        y = int(input('enter the values in list'))
        lst.append(y)
    return lst

def product_of_all_element_in_lst(lst):
    result = 1
    for i in range(len(lst)):
        result = result * lst[i]
    return result


def main():

    lst = get_user_input()
    result = product_of_all_element_in_lst(lst)
    print('the product of all numbers in a list: ',result)

main()