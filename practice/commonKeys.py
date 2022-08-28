"""
Write a Python program to combine two dictionary adding values for common keys.

Input:
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

Output:
{'a': 400, 'b': 400, 'd': 400, 'c': 300}

"""




# initialise function for combining two dict
def To_combine_two_dict_of_Same_values(d1,d2):
    # define for loop to access each key in dict
    d3 = { }
    for i in d2:  
        # check duplicate keys exist in dict
        if i in d1:
            #adding values of both the dictionary of same key and add key and value(addition) into third dictionary.
            print(i)
            result = d1[i] + d2[i]
            d3[i]= result 
        else:
            # add value  of d2[i]  into third dictionary on key i.
            d3[i] = d2[i]

    for i in d1:
        if i in d2:
            pass
        else:
            d3[i] = d1[i]
    return d3


def main():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
   
    result = To_combine_two_dict_of_Same_values(d1,d2)

    print('this is combined dict: ',result)

main()