"""
insertion
1) make sure your list is must be sorted to perform insertion.
2) Take input from user.
3) ask user to enter size of list
4) then define empty list
5) ask user to enter values in list
6) then append the values to empty list.
7) again ask user for value to be insert
8) make space for value to be insert with value(none).
9) apply while loop and define condition value of list[i] > value to be insert and i > = 0
    for making empty index for value to be inserted list[i+1] = list[i]
10) then decrese indexing by i-1
11) Run the loop until it get terminate
12) loop get terminate when list[i] < value to be insert and




"""
def get_user_input():
    size = int(input('enter size of list'))
    lst = [ ]
    for i in range(size):
        a = int(input('enter the values of list'))
        lst.append(a)

    return lst

def insertion(lst,size,key):
    i = size - 1
    key.append(None)
    while i<= 0 and lst[i] < key :
        lst[i + 1] = lst[i]
        i = i - 1
        lst[i+1] = key
        print('updated list is: ',lst)
    return 







def main():
  
  key = insertion(lst,size,key) 
  lst = get_user_input()
  



main()