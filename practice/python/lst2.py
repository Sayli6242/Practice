"""
Take 10 integer inputs from user and store them in a list.
Again ask user to give a number. 
Now, tell user whether that number is present in list or not.

1.take input from user
2.then define empty list
3.make for loop for definite range
4.again ask user for input convert into int and assign them into variable
5.append value to list and store them into variable
6.print result
7.again take input from user and ask them to give number to find in list
8.to find num apply if and check enter number into list and print num is in list
9.else print num is not inlist

"""


def take_user_input():
    x = int(input('enter the number'))
    lst = [ ]
    for i in range(0,x):
        y = int(input('enter values for list'))
        lst.append(y)
        print(lst)
    z = int(input('enter num that u want to find in list '))
    return lst,z

def check_if_element_in_list(lst,z):
    found = False
    for i in lst:
        # 
        if z == i:
            found = True
            break
    return found


def print_result(found):
    if not found:
        print('the number is not present in list')

    if found:
        print('the number is present in list')


def main():
    lst,z = take_user_input()
    present =  check_if_element_in_list(lst,z)
    print_result(present)


main()