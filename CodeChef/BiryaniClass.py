"""
- According to a recent survey, Biryani is the most ordered food. 
- Chef wants to learn how to make world-class Biryani from a MasterChef. 
- Chef will be required to attend the MasterChef's classes for XX weeks, and the cost of classes per week is YY coins.
- What is the total amount of money that Chef will have to pay?

Input Format
- The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
- The first and only line of each test case contains two space-separated integers XX and YY, as described in the problem statement.

Output Format
- For each test case, output on a new line the total amount of money that Chef will have to pay.

"""


T = int(input())
for t in range(T):
    num_of_week, cost_per_week = input().split()
    total_money = int(num_of_week) * int(cost_per_week)
    print(total_money)
