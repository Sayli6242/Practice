"""





"""
"""
1) find the pair for four sticks
4) 
5) 
6) 
7) 

"""


T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    lst = []
    for i in range(0, N - 1):
        for j in range(i + 1, N - 1):
            if lst[i] and lst[j] in A:
                z = lst[i] * lst[j]
                print(z)
