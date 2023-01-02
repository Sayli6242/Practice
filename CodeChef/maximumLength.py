"""
You are given an integer NN. Consider the sequence containing the integers 1, 2, \ldots, N1,2,…,N in increasing order (each exactly once). 
Find the maximum length of its contiguous subsequence with an even sum.

Input Format
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first and only line of each test case contains a single integer NN.
Output Format
For each test case, print a single line containing one integer --- the maximum length of a contiguous subsequence with even sum.

"""
"""
1) chek input num(N) and next num(N+1) 
2) calculate their sum is even or odd
3) print result.

"""
T = int(input())
for t in range(T):
    N = int(input())
    total = (N * (N + 1)) // 2
    if total % 2 == 0:
        print(N)
    else:
        print(N - 1)
