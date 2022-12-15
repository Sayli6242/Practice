"""
-Chef has his lunch only between 1 pm and 4 pm (both inclusive).
-Given that the current time is XX pm, find out whether it is lunchtime for Chef.

Input Format
-The first line of input will contain a single integer T, the number of test cases. Then the test cases follow.
-Each test case contains a single line of input, containing one integer X.
Output Format
-For each test case, print in a single line YES if it is lunchtime for Chef. Otherwise, print NO.


"""

T = int(input())
for t in range(T):
    x = int(input())
    if x >= 1 and x <=4:
        print('Yes')
    else:
        print('No')