"""
-Chef is given 33 integers A, B and C such that A<B<C.
-Chef needs to find the value of max(A, B, C) - min(A, B,c)
-Here max(A,B,C) denotes the maximum value among A,B,C while min(A,B,C) denotes the minimum value among A, B, C.

Input Format
-The first line of input will contain a single integer T, denoting the number of test cases.
-Each test case consists of 3 integers A, B, C.
Output Format
-For each test case, output the value of max(A, B, C) - min(A, B, C).

"""

T = int(input())
for t in range(T):
    a, b, c = input().split()
    num_a = int(a)
    num_b = int(b)
    num_c = int(c)

    number = [num_a, num_b, num_c]
    m = max(number) - min(number)
    print(m)
