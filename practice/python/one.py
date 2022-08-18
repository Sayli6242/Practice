"""

Take 10 integer inputs from user and store them in a list and print them on screen.

1.take input from user
2.convert into integer
3.apply for loop for given range
4.again take input from user ask for values in list
5.and store the values and append to list 
6.print result

"""

x = int(input('enter a value'))
lst = []
for i in range(0,x):
    l = int(input('enter numbers for list'))
    lst.append(l)
print(lst)

