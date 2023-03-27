"""
There is new delicious item in Chef's menu - a doughnut chain.
Doughnuts connected successively in line forming a chain.
Chain of 3 doughnuts.
Chef has received an urgent order for making a chain of N doughnuts. 
He noticed that there are exactly N cooked doughnuts in the kitchen, some of which are already connected in chains. 
The only thing he needs to do is connect them in one chain.
He can cut one doughnut (from any position in a chain) into two halves and then use this cut doughnut to link two different chains.
Help Chef determine the minimum number of cuts needed to complete the order.
"""
"""
1) 
2)
3)
4)
5)
"""
T = int(input())
for i in range(T):
    N, M = input().split()
    size_of_order = int(N)
    num_of_cooked_chain = int(M)
    A = list(map(int, input().split()))
    A.sort()
    count =0
    for i in range(num_of_cooked_chain):
        total = num_of_cooked_chain - (i+1)
        count += A[i]
        if count >= total-1:
            if count == total-1:
                print(total-1)
            else:
                print(total)
            break