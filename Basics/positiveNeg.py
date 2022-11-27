"""
Check if the number is positive or negative or zero and display an appropriate message

1.take input from user
2.apply condition if input number is greater than zero then it is positive number.
3.again apply if number is less than zero its is negetive number.
4.else it is zero 
5.print zero


"""

x = int(input('enter the number'))
result = 0
if x > 0:
    print('the number is positive')    
elif x < 0:
        print('the number is negetive')
elif x == 0:
    print('number is zero')