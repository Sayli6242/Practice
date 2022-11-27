"""
Make a list by taking 10 input from user. Store only even values given and print the list.

"""



def get_user_input():
    lst = [ ]
    for i in range(10):
        y = int(input(f'enter the list values{i}: '))
        lst.append(y)
    return lst


def check_for_even_values(lst):
    result = 0
    new_lst = [ ]
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    
    return new_lst
            
    
def main():

    lst = get_user_input()


    new_lst  = check_for_even_values(lst)

    print('this is list of numbers: ',lst)
    print('this are even values: ', new_lst)


main()