"""
Take 20 integer inputs from user and print the following:
Input - 20 numbers

number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s.

"""

def get_user_input():
    x = int(input('enter length of list: '))
    lst = [ ]
    for i in range(x):
        y = int(input(f'enter list element {i}: '))     
        lst.append(y)
    return lst

def check_num_positive_negetive(lst):     
    
    positive_num = [ ]
    negetive_num = [ ]
    zeros = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            positive_num.append(lst[i])
        
        if lst[i] < 0:
            negetive_num.append(lst[i])
        if lst[i] == 0:
            zeros += 1                          #zeros = zeros + 1
    return positive_num , negetive_num    


def check_num_even_odd(lst):
    even_num = [ ]
    odd_num = [ ]
    for i in range(len(lst)):
        if lst[i] %2==0:
            even_num.append(lst[i])
        if lst[i] %2 !=0:
            odd_num.append(lst[i])
    return even_num , odd_num


def main():
    lst = get_user_input()

    positive_num , negetive_num = check_num_positive_negetive(lst)

    even_num , odd_num = check_num_even_odd(lst)

    print('number of positive number is: ',len(positive_num))
    print('positive numbers is: ',positive_num)

    print('number of negetive number is: ',len(negetive_num))
    print('negetive numbers is: ',negetive_num)

    print('number of even numbers is: ',len(even_num))
    print('even numbers are: ',even_num)

    print('number of odd numbers is: ',odd_num)
    print('odd numbers is',odd_num)


main()