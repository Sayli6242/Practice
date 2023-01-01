"""
Chef and Dhyey have become friends recently. Chef wants to test Dhyey's intelligence by giving him a puzzle to solve.

The puzzle contains an integer sequence A_1, A_2, \ldots, A_NA 
1
​
 ,A 
2
​
 ,…,A 
N
​
 . The answer to the puzzle is the maximum of A_i \% A_jA 
i
​
 %A 
j
​
 , taken over all valid ii, jj.

Help Dhyey solve this puzzle.

Input
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
For each test case, print a single line containing one integer — the answer to the puzzle.



"""


"""
1) find maximun number from given list.
2) make new list and find mod of each element in list with max_num.
3) return anwer to new list
4) again find maximum number in new list 
5) print result
"""

N = int(input())
A = list(map(int, input().split()))
max_num = max(A)
new_lst = []
for i in A:
    total = i % max_num
    new_lst.append(total)
    maximum = max(new_lst)
print(maximum)
