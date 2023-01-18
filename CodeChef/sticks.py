"""





"""
"""
1) find the pair for four sticks
4) 
5) 
6) 
7) 

"""
from intertool import combinations

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    for i in A:
        pairs = list(combinations(A, 2))
        print(pairs)