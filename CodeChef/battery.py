"""
-Chef's phone shows a Battery Low notification if the battery level is 15% or less.
-Given that the battery level of Chef's phone is X%, determine whether it would show a Battery low notification.

Input Format
-First line will contain TT, number of test cases. Then the test cases follow.
-Each test case contains a single line of input, an integer XX, denoting the battery level of the phone.

Output Format
-For each test case, output in a single line Yes, if the battery level is 15% or below. Otherwise, print No.
"""
T = int(input())
for t in range(T):
    x = int(input())
    if x < 17:
        print("yes")
    else:
        print("no")
