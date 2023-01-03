"""
A number is called palindromic if its decimal representation is a palindrome. You are given a range, described by a pair of integers L and R. Find the sum of all palindromic numbers lying in the range [L, R], inclusive of both the extrema.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains a pair of space separated integers L and R denoting the range for which you are required to find the sum of the palindromic numbers.

Output
For each test case, output a single line containing the sum of all the palindromic numbers in the given range.

"""
"""
1) define numbers of given range
2) convert each num into string for comparison
1) check starting index of num is equal to ending index of num using slicing.
2) if palindrome founds calculate sum of those num until given range.
3) print all sum

"""

T = int(input())
for t in range(T):
    L, R = map(int, input().split())
    sum = 0
    for i in range(L, R + 1):
        i = str(i)
        if i == i[::-1]:
            sum += int(i)
    print(sum)
