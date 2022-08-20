"""
Write a program to print sum, average of all numbers, smallest and largest element of a list.

"""

def get_user_input():
    x = int(input('enter length of string: '))
    lst = [ ]
    for i in range(x):
        y = int(input('enter values for list: '))
        lst.append(y)
    return lst

def total_sum(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]         
    return sum                                    


def get_avrage_of_all_num(lst):
    # result = 0
    # for i in range(len(lst)):
    #     print('add each element of list to result and divide by length of list')
    #     result = result + lst[i] / len(lst)
    return total_sum(lst) / len(lst)


def To_find_small_large_element(lst):
    # take first element as min and max
    small_num = lst[0]
    large_num = lst[0]
    # traverse each element in list 
    for i in range(len(lst)):
        # check if i'th is less than small_num 
        if  lst[i] < small_num:
            # assign ith value to small_num 
            small_num = lst[i]
        # check if i'th is greater than large_num 
        if lst[i] > large_num :
            # assign ith value to large_num 
            large_num = lst[i]

    return small_num, large_num


def main():

    lst = get_user_input()
    
    sum = total_sum(lst)

    avg = get_avrage_of_all_num(lst)

    small_num , large_num  = To_find_small_large_element(lst)

    print('the sum of all element in list are: ',sum)

    print('the avrage of all num in list are: ',avg)

    print('the smallest element in a is is:',small_num)
    print('the largest element in a list is: ',large_num)


main()