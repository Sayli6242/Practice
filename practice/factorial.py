"""
Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n.

 E.g.-

4! = 1*2*3*4 = 24

3! = 3*2*1 = 6

2! = 2*1 = 2

1! = 1

0! = 1

Write a program to calculate factorial of a number using loop

"""



def get_user_input():
    num = int(input('enter the number: '))
    return num

def To_get_factorial_on_num(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial


def main():
    num = get_user_input()
    factorial = To_get_factorial_on_num(num)
    print('factorial of no. is: ', factorial)

main()






