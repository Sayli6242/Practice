"""
- In Chefland, a tax of rupees 1010 is deducted if the total income is strictly greater than rupees 100100.
- Given that total income is XX rupees, find out how much money you get.

Input Format
- The first line of input will contain a single integer TT, denoting the number of test cases.
- The first and only line of each test case contains a single integer XX — your total income.


"""
T = int(input())
for t in range(T):
    X = int(input())
    if X > 100:
        total = X - 10
        print(total)
    else:
        print(X)
