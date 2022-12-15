"""
-Finally, after purchasing a water cooler during the April long challenge, Chef noticed that his water cooler requires 2 liters of water to cool for one hour.
-How much water (in liters) would be required by the cooler to cool for NN hours?

Input Format
-The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
-The first and only line of each test case contains an integer N, as described in the problem statement.
Output Format
-For each test case, output the number of liters of water required by the water cooler to cool for NN hours.

"""

T = int(input())
for t in range(T):
    n = int(input())
    total = n*2
    print(total)

