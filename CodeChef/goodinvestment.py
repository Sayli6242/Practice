"""
Chef has invested his money at an interest rate of XX percent per annum while the current inflation rate is YY percent per annum.

An investment is called good if and only if the interest rate of the investment is at least twice of the inflation rate.
Determine whether the investment made by Chef is good or not.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two integers XX and YY, the interest rate and the current inflation rate respectively.
Output Format
For each test case, output YES if the investment is good, NO otherwise.


"""
T = int(input())
for t in range(T):
    x, y = input().split()
    interest_rate = int(x)
    current_inflation_rate = int(y)
    if interest_rate >= (current_inflation_rate * 2):
        print("yes")
    else:
        print("no")
