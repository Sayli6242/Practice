"""
Write a program to find the sum of all elements of a list.
input - take dynamic (any) number of elements
output - sum of all elements

"""

def take_user_input():
    x = int(input('enter the number'))
    lst = [ ]
    for i in range(0,x):
        y = int(input('enter values for list'))
        lst.append(y)
        print(lst)
def calculate_sum(lst):
      sum_of_nat_num = 0
      for i in range(1,x):
        print(i)
        sum_of_nat_num = sum_of_nat_num + i
        return sum_of_nat_num

def main():
   lst =  take_user_input()
   result = calculate_sum(lst) 
   print(result)


main()