"""
The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

Rent a cooler at the cost of XX coins per month.
Purchase a cooler for YY coins.
Chef wonders what is the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.

Input Format
The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
The first and only line of each test case contains two integers XX and YY, as described in the problem statement.
Output Format
For each test case, output the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.


"""
T = int(input())
for i in range(T):
    X, Y = input().split()
    rent_of_cooler = int(X)
    purchase_of_cooler = int(Y)
    total = purchase_of_cooler // rent_of_cooler
    max_total = purchase_of_cooler // rent_of_cooler - 1

    if purchase_of_cooler % rent_of_cooler == 0:
        print(max_total)
    else:
        print(total)
