# implement your own power function (take input number(a)  and exponent(b), returns the a^b)
"""
1.understand the problem
2.write in words
   1. take input from user
   2.convert to string
   2.convert to integer
   3.define function
      1. make for loop upto given range
      2. 
   4. returns function
   5. code
 """

def pow(number, power):
    result = 1
    for _ in range(power):
        result = result * number
    return result


def get_user_inputs_calculate_pow():
    x = int(input('enter number'))
    n = int(input('enter power'))
    res = pow(x, n)
    print(res)

get_user_inputs_calculate_pow()


