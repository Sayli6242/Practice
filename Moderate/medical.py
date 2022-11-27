
"""
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
input - number of total classes , number of classes attended, Has any medical condition.
Output - Print True if user attendance is above 75% or if he has a medical condition false if not

1. take input from user to ask about medical condition
2. apply condition if he/ she has medical cause then print Y
3. else N
"""




z =int(input('total no. of class held'))
y =int(input('total no of class attend'))
x = input('student has medical condition : ')

result = int((y/z)*100)

if result > 75 or  x == 'Y':
   print('true')
else:
    print('false')

