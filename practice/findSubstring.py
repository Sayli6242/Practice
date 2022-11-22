"""
write a python program to find the first appearance of the 'not' and 'poor' from given string,
if 'not' follows the 'poor' , replace the whole 'not' ...'poor' substring with 'good'.
Return the resulting string.

pov: 

1) get input string
2) split the string to get the list of words.
3) iterate list and compare value with "not"
4) If found check next word is "poor".
5) replace the given word with substring.
6) print the result.

"""


def spliting_string(str, sub_str):
    new_lst = []
    temp = " "
    for sub_str in str:
        if sub_str == " ":
            new_lst.append(temp)
        else:
            temp += sub_str
    if temp:
        new_lst.append(temp)

    return new_lst, temp

def replace_the_string(new_lst, temp, sub_str):
    i = 0
    for word in new_lst:
        if new_lst[i] == "not":
            new_lst[i + 1] == "poor"

        i += 1
    print(new_lst)
    return new_lst


#     # for i in s:
#     if(i==""):
#         new_str+=s2
#     else:
#         new_str+=i


def main():

    str = "tom is not rich but he is poor"
    not_i = None
    poor_i = None

    # [ni:pi]=

    sub_str = "good"
    new_lst, temp = spliting_string(str, sub_str)
    sub_str = replace_the_string(new_lst, sub_str, temp)


main()
