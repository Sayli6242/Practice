"""
-chef opened a company which manufactures cars and bikes. Each car requires 4 tyres while each bike requires 2 tyres. Chef has a total of N tyres (N is even). 
-He wants to manufacture maximum number of cars from these tyres and then manufacture bikes from the remaining tyres.
-chef's friend went to Chef to purchase a bike. If Chef's company has manufactured even a single bike then Chef's friend will be able to purchase it.
-Determine whether he will be able to purchase the bike or not.

Input Format
-The first line contains an integer T denoting the number of test cases. The T test cases then follow.
-The first line of each test case contains an integer NN denoting the number of tyres.
"""

T = int(input())
for i in range(T):
    num_of_tyres = int(input())
    total = num_of_tyres % 4
    if total >= 2:
        print("Yes")
    else:
        print("No")
