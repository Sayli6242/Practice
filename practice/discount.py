"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.

1.take input from users 
2.define discount price , original price , discount percentage which is given
3.apply if condition and check the amount is more than 1000 then apply discount
4.appy formula 

"""
x = int(input('enter the quantity of product '))
# # Tp = 1000
# dc = 10 
i_unit = 100
 

if x >= 1000:
    dc = x*i_unit/100
    print('the discount is ',dc)




