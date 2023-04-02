"""
Kerim is an environment-friendly guy. Today, he accepted Samir's challenge of planting 20 million trees by 2020. Currently, there are 
N trees (numbered 1 through N) planted at distinct positions on a line; for each valid i, the position of the i-th tree is Ai​.

A set of trees is beautiful if for each tree in this set (let's denote its position by x), there is a tree at the position 1
x−1 and/or a tree at the position 
+
1
x+1.
Kerim's task is to plant some (possibly zero) trees in such a way that the resulting set of all planted trees (the initial 
�
N trees and those planted by Kerim) is beautiful. 
It is only allowed to plant trees at integer (possibly negative) positions. 
Find the minimum number of trees he needs to plant in order to achieve that.
"""
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    count = 0
    i == 0
    for i in range(N):
        if i == 0:
            if A[i+1] != A[i]+1:
                count += 1
                A[i] = A[i]+1
            elif i == len(A) - 1:
                if A[i-1]!= A[i]-1:
                    count+=1
            else:
                if A[i+1]!= A[i]+1  and [i-1] != A[i]-1:
                    count+=1
                    A[i] = A[i] + 1
            i+=1
    print(count)