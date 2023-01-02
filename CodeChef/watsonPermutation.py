"""
Watson gives an array A of N integers A1, A2, ..., AN to Sherlock. He wants Sherlock to reorganize the array in a way such that no two adjacent numbers differ by more than 1.

Formally, if reorganized array is B1, B2, ..., BN, then the condition that | Bi - Bi + 1 | ≤ 1, for all 1 ≤ i < N(where |x| denotes the absolute value of x) should be met.

Sherlock is not sure that a solution exists, so he asks you.

Input
First line contains T, number of test cases. Each test case consists of N in one line followed by N integers in next line denoting A1, A2, ..., AN.

Output
For each test case, output in one line YES or NO denoting if array A can be reorganized in required way or not.

"""

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N-1):
        if abs(A[i] - A[i+1]) > 1:
            print('NO')
            break
    else:
        print('YES')