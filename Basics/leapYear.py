
"""find leap year or not.

1) take user input.
2) define condition.
3) check condition.
4) any year that is divisible by 4 is leap year
5) return true.
6) else.
7) return false.

"""
# take user input
x = int(input('Enter year, that you want to check:  '))

# check condition
if x % 4 == 0:
    print('This is leap year')
else:
# print result
    print('This is not leap year')