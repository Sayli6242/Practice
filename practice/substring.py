"""
Write a python for taking input from user and count the occurrences of substring in string

1) take user input
2) initialize a string
3) ask user for a sub_string to count
4) iterate the entire string for that particular sub_string and then
   increase the counter when we encounter the particular character.
5) print result
"""


def get_user_input():
    str = input("enter random string: ")
    sub_str = input("enter wanted word: ")
    return str, sub_str


def find_count_of_substring_in_string(
    str,
    sub_str,
):
    count = 0
    for i in str:
        if i == sub_str:
            count = count + 1
    print(count)


def main():
    str, sub_str = get_user_input()
    count = find_count_of_substring_in_string(
        str,
        sub_str,
    )


main()
