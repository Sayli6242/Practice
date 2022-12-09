"""
-If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

Input Format
-The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

Output Format
-For each test case, display the sum of first and last digits of N in a new line.

"""


T = int(input())
for t in range(T):
    N = input()
    total = int(N[0]) + int(N[len(N) - 1])
    print(total)
