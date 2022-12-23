"""
Chef has X coins worth 1 rupee each and Y coins worth 2 rupees each.
He wants to distribute all of these X+Y coins to his two sons so that the total value of coins received by each of them is the same.
Find out whether Chef will be able to do so.

Input Format
The first line of input contains a single integer T, denoting the number of testcases.
The description of T test cases follows.
Each test case consists of a single line of input containing two space-separated integers X and Y.
Output Format
For each test case, print "YES" (without quotes) if Chef can distribute all the coins equally and "NO" otherwise. 




"""

T = int(input())
for t in range(T):
    x, y = input().split()
    num_x = int(x)
    num_y = int(y)
    if (num_x % 2) == (num_y % 2) == 0:
        if num_x % 2 == 0 and num_x > 0:
            print("yes")
    else:
        print("no")
