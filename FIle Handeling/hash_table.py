
"""
- hashing algorithms (string to big int, big int to small int )N
    - take string convert it into big integer.
    - 
- array size (0.5 * array size ) → resize 2* array size (element shuffle)
"""
"""
- we have to make low level array with validation of C.
- hash table making.
    - while making hash table take a random string 
    - convert random string into big integer number.
    - then convert big integer number into small int.
    - 
"""

# import string
# import random

# def generate_random_string(length):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
#     random_string = ""
#     for _ in range(length):
#         random_index = random.randint(0, len(characters) - 1)
#         random_char = characters[random_index]
#         random_string += random_char    
#     return random_string
# random_string = generate_random_string(12)  
# print("Random String:", random_string)



array = []

# make string to big integer 
def string_to_big_int(string):

    big_int = 0
    # sum of all ascii value of characters in string
    for i in string:
        a = ord(i)
        big_int = big_int + a

    return big_int
    
# convert big int into small int
def big_int_to_small_int(big_int, array_size):

    # Take the remainder when divided by array_size
    small_int = big_int % array_size

    return small_int

# # Insert key value pairs into the array(set value)

def set_key_value(array, key, value):

    big_int = string_to_big_int(key)
    small_int = big_int_to_small_int(big_int,array_size)
   
    array[small_int] = (key,value)
    # print(array)
    return array
 
 #  chech key is present in hash table (get)







string = "apple"

array_size = 10


big_int = string_to_big_int(string)
print(big_int)

small_int = big_int_to_small_int(big_int, array_size)
print(small_int)

array = set_key_value(array, "key1", "value1")
print(array)



