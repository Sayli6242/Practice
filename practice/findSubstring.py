"""
write a python program to find the first appearance of the 'not' and 'poor' from given string,
 
if 'not' follows the 'poor' , replace the whole 'not' ...'poor' substring with 'good'.
Return the resulting string.

pov: 

1) initialise given string
2) 
"""


def spliting_string():
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


# def replace_all (target,find,replace):
#     split_target = target.split()
#     result = ''
#     for i in split_target:
#         if i == find:
#             i = replace
#             result += i + ' '
#             return result.strip()
#         target = "Maybe she's born with it. Maybe it's Maybeline."
#         find = "Maybe"
#         replace = "Perhaps"
#     print replace_all(target, find, replace)
#     return target, find, replace

#     # for i in s:
#     if(i==""):
#         new_str+=s2
#     else:
#         new_str+=i


def main():

    str = "tom is not rich but he is poor"
    sub_str = "good"
    split_value, tmp = spliting_string()


main()
