"""
Chef is given two arrays AA and BB of length NN each.

In one operation Chef can choose one element of AA and one element of BB and increase them by 11.

More formally: Chef can pick two integers i, ji,j (1\le i, j \le N)(1≤i,j≤N) and increment A_iA 
i
​
  and B_jB 
j
​
  by 11.

Determine the minimum number of operations required to make AA and BB equal.

Output -1−1 if it is not possible to make AA and BB equal.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains a single integer NN - denoting the length of arrays AA and BB.
The second line of each test case contains NN space separated integers A_1, A_2, A_3, \dots A_NA 
1
​
 ,A 
2
​
 ,A 
3
​
 ,…A 
N
​
  - denoting the array AA.
The third line of each test case contains NN space separated integers B_1, B_2, B_3, \dots B_NB 
1
​
 ,B 
2
​
 ,B 
3
​
 ,…B 
N
​
  - denoting the array BB.
Output Format
For each test case, output the minimum number of operations to make AA and BB equal or -1−1 if they cannot be made equal.
"""
"""
1) check each num of list A and  list B 
2) compare them when num of list A is greater than num of list B
3) substract num of list A from num of list B 
4) and increase their count for A list by 1
5) othervise substract num of list B from num of list A.
6) and increse their count for B list by 1.
7) then check count of both list are equal or not.
8) if equal then print count of list A.
9) if not then print -1.
"""
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    C = 0
    D = 0
    for i in range(N):
        if A[i] > B[i]:
            C += A[i] - B[i]
        else:
            D += B[i] - A[i]
    if C == D:
        print(C)
    else:
        print(-1)
