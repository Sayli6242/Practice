"""
Tonight, Chef would like to hold a party for his NN friends.

All friends are invited and they arrive at the party one by one in an arbitrary order. However, they have certain conditions — for each valid ii, when the ii-th friend arrives at the party and sees that at that point, strictly less than A_iA 
i
​
  other people (excluding Chef) have joined the party, this friend leaves the party; otherwise, this friend joins the party.

Help Chef estimate how successful the party can be — find the maximum number of his friends who could join the party (for an optimal choice of the order of arrivals).

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains a single integer NN.
The second line contains NN space-separated integers A_1, A_2, \ldots, A_NA 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .
Output
For each test case, print a single line containing one integer — the maximum number of Chef's friends who could join the party.



"""


"""
1) sort the input list.
2) take count initially zero
3) iterate the sorted list when each num in list compares with index of those num
4) when num in list is greater than idex of num increse count by one
5) when condition gets false stop and print count.

"""
T = int(input())
for t in range(T):
    num_of_friends = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    count = 0
    for i in range(num_of_friends):
        if lst[i] <= i:
            count += 1
        else:
            break

    print(count)
