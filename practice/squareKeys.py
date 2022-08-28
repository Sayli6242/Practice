"""
Write a Python script to print a dictionary where,
the keys are numbers between 1 and 15 (both values included) and the values are square of keys.

"""

def to_obtain_square_of_keys_as_values():
    dict = 0
    for i in range(1,15):
        dict = dict[i] * dict[i]
        dict.append(dict)
    return dict






def main():

    dict = to_obtain_square_of_keys_as_values()

    print('this is obtained dictionary: ',dict)

main()