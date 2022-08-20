"""
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.


"""

def get_user_input():
    lst = [ ]
    # give values in the range of 0 to 10
    for i in range(10):
        # take integer input from user
        y = int(input(f'enter value for list {i}: '))
        # append y to lst
        lst.append(y)
    return lst

def copy_all_elements_in_reverce_order(lst):
    # initilise a list to store reverse values
    rev = []
    # print list in reverse
    for i in range(-1, -len(lst),-1):
        print(f"element at index {i}, is {lst[i]}")
        rev.append(lst[i])
    return rev

def main():

    lst = get_user_input()

    new_lst = copy_all_elements_in_reverce_order(lst)

    print('the list is: ', lst)
    print('list in reverse order is: ',new_lst)


main()

