"""
-Chef has NN empty bottles where each bottle has a capacity of X litres.
-There is a water tank in Chefland having K litres of water. Chef wants to fill the empty bottles using the water in the tank.
-Assuming that Chef does not spill any water while filling the bottles, find out the maximum number of bottles Chef can fill completely.

Input Format
-First line will contain TT, number of test cases. Then the test cases follow.
-Each test case contains of a single line of input, three integers N, X and K.
Output Format
-For each test case, output in a single line answer, the maximum number of bottles Chef can fill completely.

"""

T = int(input())
for t in range(T):
    n, x, k = input().split()
    total = int(k) / int(x)
    if int(total) < int(n):
        print(total)
    else:
        print(n)
