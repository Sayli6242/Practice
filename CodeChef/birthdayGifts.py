"""
It’s Chef's birthday. He and his twin have received N gifts in total. 
The i-th gift has a price of Ai. 
Each twin wants to keep the most expensive gifts for himself.
The twins take K turns alternately (each has K turns, for 2⋅K turns in total).
It is given that 2⋅K+1≤N. In a turn, a person may choose one gift. 
The only exception is the last turn of the twin who moves second, where he gets to choose two gifts instead of one.
Assuming they both choose gifts optimally and you can choose who takes the first turn, 
find the maximum total cost of the gifts that Chef keeps.

"""
"""
1) Take out maximum no. from list and store them in list1 again take out max num from list and store it in list2. follow these alternatly.
2) when number of turns is equals to 1 then sum of all two lists
3) and print maximum sum 
4)
5)

"""

T = int(input())
for t in range(T):
    N,K = input().split()
    A = list(map(int, input().split()))
    no_of_gifts = int(N)
    no_of_turns = int(K)*2
    A.sort(reverse=True)
    lst_1 = [ ]
    lst_2 = [ ]
    for i in range(no_of_gifts):  
        Popped_ele = A.pop(0)
        lst_1.append(Popped_ele)
        no_of_turns -= 1
        if lst_1 != [ ]:
            Popped = A.pop(0)
            lst_2.append(Popped)
            no_of_turns -= 1
            if no_of_turns == 0:
                lst_2.append(A.pop(0))
                A = sum(lst_1)
                B = sum(lst_2)
                print(max(A,B))
                break