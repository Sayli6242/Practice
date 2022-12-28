"""
Chef visited a grocery store for fresh supplies. There are NN items in the store where the i^{th}i 
th
  item has a freshness value A_iA 
i
​
  and cost B_iB 
i
​
 .

Chef has decided to purchase all the items having a freshness value greater than equal to XX. Find the total cost of the groceries Chef buys.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two space-separated integers NN and XX — the number of items and the minimum freshness value an item should have.
The second line contains NN space-separated integers, the array AA, denoting the freshness value of each item.
The third line contains NN space-separated integers, the array BB, denoting the cost of each item.
Output Format
For each test case, output on a new line, the total cost of the groceries Chef buys.



"""

# take input for no of testcase
T = int(input())
# take input for each testcase
for i in range(T):
    # take input for number of items and minimum freshness value
    n, x = map(int, input().split())
    # take input for denoting freshness value of each item as list
    A = list(map(int, input().split()))
    # take input for denoting cost of each item.
    B = list(map(int, input().split()))
    # return count
    total = 0
    for i in range(len(A)):
        # comparing item in list A with minimum freshness value of item
        if A[i] >= x:
            total = +B[i]
    # print result
    print(total)
