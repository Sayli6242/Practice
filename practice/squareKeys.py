"""
Write a Python script to print a dictionary where,
the keys are numbers between 1 and 15 (both values included) and the values are square of keys.

"""


# initialize function to obtain square of keys as values
def to_obtain_square_of_keys_as_values():
    # define empty dictionary to store keys and values
    d3 = { }
    #  apply for loop for acces each key,value in dictionary upto given range
    for key in range(1,15):
        # exponent of key is assign to value to ditionary d3
            value = key ** 2
            # obtained value is assign to d3 as a key: value
            d3[key] = value
            # return dictionary d3
    return d3



def main():

    d3 = to_obtain_square_of_keys_as_values()

    print('this is obtained dictionary: ',d3)

main()