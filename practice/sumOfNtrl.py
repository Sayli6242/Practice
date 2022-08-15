"""
Find the sum of natural numbers using while loop

input - n how many numbers to count (ex 10 - count sum of first 10 natural numbers)
Output - sum

"""
"""
1.take input from user
2.convert it into integer
3.apply for loop upto range given by user
4.sum of all interger in given range
5.print result
"""




def sum_natural_num(x):
    sum_of_nat_num = 0
    for i in range(1,x):
        print(i)
        sum_of_nat_num = sum_of_nat_num + i
    return sum_of_nat_num
  
def get_user_input():
    x = int(input('enter the value'))
    result = sum_natural_num(x)
    print(result)


get_user_input()