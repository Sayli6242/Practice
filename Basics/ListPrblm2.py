"""
Take 10 integer inputs from user and store them in a list. 
Again ask user to give a number. Now, tell user whether that number is present in list or not.

# Algorithm for solution.

1) aks user for 10 interger input
2) define empty list
3) append the inter input one be one in empty list.
4) ask user to give a number.
5) check the number is present in list or not
6) If present print 'Found'
7) else print 'not found'

"""


def get_user_input():
    lst = []
    for i in range(0, 10):
        x = int(input(f"enter the list number {i}: "))
        lst.append(x)
    print(lst)
    return lst


def check_the_number_in_lst(lst):

    num = int(input("enter number to be found"))
    for i in range(0, 10):
        if lst[i] == num:
            print(f"found at {lst[i]} index")

            return num


def main():

    lst = get_user_input()
    num = check_the_number_in_lst(lst)


main()
