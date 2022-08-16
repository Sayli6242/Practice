"""
check whether an alphabet is vowel or consonant


1. take input from user
2. store it in a variable
3. define a list of vowels
4. apply condition to check the number is vowel or consonent if condition is true then print vowel
5. else it is consonent
6. print result

"""
x = input('enter character: ')
lst = ['a','e','i','o','u','A','E','I','O','U']

if x in lst:
    print('this is vowel')
else:
    print('this is consonent')