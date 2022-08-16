""" 
generate multiplication table for input number

1.take input from user
2.convert into int
3.apply for loop for definite range
4.first sum of input to iself then add result into it 
5.print result


""" 
x = int(input('enters the number'))
result = 0
for _ in range(1,11):  
    result = result + x
    print(result)