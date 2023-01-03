"""



"""

"""
1) make list and seperate each element in it.
2) make pair of each using slices
3) compare each pair with other
4) append to new list
5) increase count each time
5) print result
"""
T = int(input())
for t in range(T):
    S = list(input())
    result = 0
    lst = []
    for i in range(len(S) - 1):
        if S[i : i + 2] not in lst:
            lst.append(S[i : i + 2])
            result = result + 1
    print(result)
