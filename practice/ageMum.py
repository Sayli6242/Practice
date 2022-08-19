"""
Take input of age of N (any number of) people by user and determine oldest and youngest among them.
Input - N number of.people ( 0< N < 20)
 Output - Print age of youngest and oldest
"""
"""
1.take input of number of people N is length of given array
2.apply for loop to take limit upto N
3.take input of age of those people 
4.store age of those people in array
4.
5.

"""
def get_user_input():
    x = int(input('enter length of list: '))
    lst = [ ]
    for i in range(x):
        age = int(input(f'enter 1st value of age to be in list{i}: '))
        lst.append(age)
    return lst

def find_youngest_oldest_age(lst):
    youngest_age = lst[0]
    oldest_age = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > oldest_age:
            oldest_age = lst[i]
        if lst[i] < youngest_age:
            youngest_age = lst[i]
    return youngest_age , oldest_age

def main():
    lst = get_user_input()
    youngest_age , oldest_age =  find_youngest_oldest_age(lst)

    print('the youngest age is: ',youngest_age)
    print('the oldest age is: ',oldest_age)

main()

# TODO: find min and max number

# arr = arr.append(y)