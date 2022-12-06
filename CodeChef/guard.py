"""
-Ezio can manipulate at most XX number of guards with the apple of eden.
-Given that there are YY number of guards, predict if he can safely manipulate all of them.

Input Format
-First line will contain T, number of test cases. Then the test cases follow.
-Each test case contains of a single line of input, two integers X and Y.
Output Format
-For each test case, print YES if it is possible for Ezio to manipulate all the guards. Otherwise, print NO.

"""
T = int(input())
for t in range(T):
    X, Y = input().split()
    if int(X) > int(Y) or int(X) == int(Y):
        print("YES")
    else:
        print("NO")
