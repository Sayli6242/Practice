"""
Chef wants to make a purchase. For this, he needs 
�
X gold coins, but he has none at the moment.

Chef has 
�
N fixed deposits, the 
�
�
ℎ
i 
th
  of which is worth 
�
�
A 
i
​
  coins. He wants to open the minimum number of these deposits so that he has at least 
�
X coins.

You have to tell Chef the minimum number of fixed deposits he must open in order to have 
�
X coins, or say that this is impossible.

"""
T = int(input())
for t in range(T):
    n,x=map(int,input().split())
    lst=sorted(list(map(int,input().split())))
    sm=sum(lst)
    
    if sm<x:
        print(-1)
    else:
        s=0
        for i in range(0,n):
            s=s+lst[i]
            if s>=x:
                break
        print(i+1)