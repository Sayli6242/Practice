"""
Chef has an array A having N elements. Chef wants to make all the elements of the array equal by repeating the following move.
Choose any integer K between 1 and N (inclusive). Then choose K distinct indices 1,2,…,i1,i2,…,iK, and increase the values of 1,2,…,Ai1​,Ai ,…,AiK by 
1.
Find the minimum number of moves required to make all the elements of the array equal.


"""
"""
1) simpli we have to find difference between the maximum and mininum between array
"""
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    print(max(A)-min(A))
