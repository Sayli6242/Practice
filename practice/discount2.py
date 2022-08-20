"""
 A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.
Input - item price, quantity
Output - total cost (with discount if total bill is above 1000)

1.take input from user 
2.conver into int
3.calculate percentage of class attend by using formula
4.apply condition if percentage is greater than 75 then print true
5.else false
6.print result



"""


z =int(input('total no. of class held'))
y =int(input('total no of class attend'))

x = 0
result = (y/z)*100
x = result
if x > 75:
   print('true')
else:
    print('false')
