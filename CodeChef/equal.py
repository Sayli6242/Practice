"""
-Alice and Bob are very good friends and they always distribute all the eatables equally among themselves.
-Alice has AA chocolates and Bob has BB chocolates. Determine whether Alice and Bob can distribute all the chocolates equally among themselves.

Note that:
-It is not allowed to break a chocolate into more than one piece.
-No chocolate shall be left in the distribution.
Input Format
-The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
-The first and only line of each test case contains two space-separated integers A and B, the number of chocolates that Alice and Bob have, respectively.
Output Format
-For each test case, output on a new line \texttt{YES}YES if Alice and Bob can distribute all the chocolates equally,
"""
T = int(input())
for t in range(T):
    a, b = input().split()
    total = int(a) + int(b)
    if total % 2 == 0:
        print("YES")

    else:
        print("NO")
