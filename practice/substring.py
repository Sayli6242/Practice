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


def spliting_string(str, sub_str):
    split_value = []
    tmp = ""
    for sub_str in str:
        if sub_str == " ":
            split_value.append(tmp)
            tmp = ""
        else:
            tmp += sub_str
    if tmp:
        split_value.append(tmp)
    return split_value, tmp


def find_count_of_substring_in_string(str, sub_str, split_value, tmp):
    count = 0
    for i in range(0, len(split_value)):
        if split_value[i] == sub_str:
            count = count + 1
    print(count)
    return count


def main():
    str, sub_str = get_user_input()
    split_value, tmp = spliting_string(str, sub_str)
    count = find_count_of_substring_in_string(str, sub_str, split_value, tmp)


main()
