"""

Find largest and smallest elements of a list.

1.define main function 
2.make 3 functions according to steps
3.firstly make fuction to get user input and make a list
4.then return list
4.secondly make function for calculate min and max values
5.then return values
6.and print within main function
7.at the end call main fuction
"""
def get_user_input():
    x = int(input('enter length of list '))
    lst = [ ]
    for i in range(x):
        y = int(input(f'enter the value at index {i}: '))        #formatted string
        lst.append(y)
    return lst

def calculate_min_max(lst):
    max_element = lst[0]
    min_element = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
        if lst[i] < min_element:
            min_element = lst[i]
    return min_element , max_element

def main():
    lst = get_user_input()
    
    min_element,max_element = calculate_min_max(lst)

    print('minimum value is ',min_element)
    print('minimum value is ',max_element)

main()
