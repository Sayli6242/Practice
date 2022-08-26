"""
Print the following patterns using loop :

"""

def get_user_input():
    num_of_rows = int(input('enter the no. of rows: '))
    return num_of_rows

def for_print_pattterns(num_of_rows):
    row = 0
    while row < num_of_rows:
        row  = row + 1
    while row > num_of_rows:
        print(' * ',end='\n')
    return True

def main():
    num_of_rows = get_user_input()
    for_print_pattterns(num_of_rows)
    print('the pattern is')
    print(' * ')


main()




































# x = int(input('enter the number of rows'))
# for i in range(1, x+1):
#     for j in range(1, i + 1):
#         print(' * ',end='')
   




