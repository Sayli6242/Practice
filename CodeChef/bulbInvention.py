"""
Now Chef has worked on multiple search algorithms to optimize search. 
For this project, he uses a modulo-based search algorithm that he invented himself. 
So first he chooses an integer K and selects all indices i in increasing order such that
imodK=0 and test the gases on such indices,
then all indices 
�
i in increasing order such that imodK=1, and test the gases on such indices, and so on.

Given N, the index of the gas p that will work, and K, find after how much time will he be able to give
Chefland a new invention assuming that testing 1 gas takes 1 day.
"""
"""
1)
2)



"""

T = int(input())
for t in range(T):
    N,p,K = input().split()
    no_of_integer = int(N)
    index_of_gas = int(p)
    first_choose_int = int(K)
    new_lst = [ ]
    for i in range(0,no_of_integer):
        result = i % first_choose_int
        new_lst.append(result)
        
        