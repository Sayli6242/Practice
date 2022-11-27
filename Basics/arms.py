

"""

1 understand the problem

2 write in words
    1. get numbers 
    2. convert to string
    3. traverse the string to get individual charachter
        4. convert char to int
        5. calculate number to the power to length of number which is store into a veriable
        6. sum x power length to sum variable
    7. compare sum is equal to  num

3. convert steps to code
    1. Write smaller function 
    2. Remove inputs use function params
    3. remove print instead return values(conclution/result)
    4. dont convert types inside function, function should only contain minimal required code
    5. call functions and get user inouts from separate function


4. If something wrong debug line by line


"""

def arm_strng(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for i in num_str:
        int_i = int(i)
        x_pow_len = pow(int_i,num_len )
        sum = sum + x_pow_len

    if num == sum:
        return True  
    else:
        return False


print(arm_strng(371))





