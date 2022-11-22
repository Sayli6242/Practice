"""
Take 10 integer inputs from user and store them in a list and print them on screen.

# Algorithm for solution.
1) Ask user for input.
2) define empty list
3) append the input one by one to empty list
4) Print the list on screen.

"""


def get_input_from_user():
    lst = []
    for i in range(0, 10):
        x = input(f"enter the list item {i}: ")
        lst.append(x)
    print(lst)

    return lst


def main():

    lst = get_input_from_user()


main()
