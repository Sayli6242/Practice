"Search element in a list using binary search"


"""1)  define a list 
    2) take user input for range of list
    3) define empty list to store elements
    4) apply for loop to itrate each element in a list.
    5) 
"""


def take_user_input():

    size = int(input("enter range of list"))
    lst = []
    for i in range(size):
        new_lst = int(input("enter the elements in a list"))
        lst.append(new_lst)
    num = int(input("enter the number to be searched: "))

    return lst, size, num


def linear_search(lst, size, num):
    result = 0
    for i in range(size):
        if lst[i] == num:
            print("number is found")

        else:
            print("number not found")


def main():

    lst, size, num = take_user_input()

    linear_search(lst, size, num)


main()
