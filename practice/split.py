"""
how to split string without using split() function.

"""


def spliting_string(str):
    new_lst = []
    temp = " "
    for sub_str in str:
        if sub_str == " ":
            new_lst.append(temp)
            temp = " "
        else:
            temp += sub_str
    if temp:
        new_lst.append(temp)

    print(new_lst, temp)

    return new_lst, temp


def main():
    str = "tom is a good person"
    new_lst, temp = spliting_string(str)


main()
