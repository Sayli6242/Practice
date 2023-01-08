"""
Alexandra has some distinct integer numbers a1,a2...an. Count number of pairs (i,j) such that:

1≤ i ≤ n 1≤ j ≤ n ai < aj
 

Input
The first line of the input contains an integer T denoting the number of test cases. 
The description of T test cases follows.The first line of each test case contains a single integer n denoting the number of numbers Alexandra has. 
The second line contains n space-separated distinct integers a1, a2, ..., an denoting these numbers.

 
Output
For each test case, output a single line containing number of pairs for corresponding test case.
"""
"""
1) Take list and sort.
2) maintain a count
3) check for indexes of sorted list
4) second index is greater than first
5) increse count
6) print count
"""

T = int(input())
for t in range(T):
    n = int(input())
    lst = input().split()
    lst.sort()
    count = 0
    for j in range(n):
        count += j
    print(count)
