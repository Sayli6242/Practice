"""
Chef recently opened a big e-commerce website where her recipes can be bought online. It's Chef's birthday month and so she has decided to organize a big sale in which grand discounts will be provided.

In this sale, suppose a recipe should have a discount of x percent and its original price (before the sale) is p. 
Statistics says that when people see a discount offered over a product, they are more likely to buy it. Therefore, Chef decides to first increase the price of this recipe by x% (from p) and then offer a discount of x% to people.

Chef has a total of N types of recipes. For each i (1 ≤ i ≤ N), the number of recipes of this type available for sale is quantityi, the unit price (of one recipe of this type, 
before the x% increase) is pricei and the discount offered on each recipe of this type (the value of x) is discounti.

Please help Chef find the total loss incurred due to this sale, if all the recipes are sold out.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the number of recipe types.
N lines follow. The i-th of these lines contains three space-separated integers pricei, quantityi and discounti describing the i-th recipe type.

Output:
For each test case, print a single line containing one real number — the total amount of money lost. 
Your answer will be considered correct if it has an absolute error less than 10-2.

"""
T = int(input())
for t in range(T):
    n = int(input())
    r = []
    total_loss = 0
    for i in range(n):
        up, down, lost = 0, 0, 0
        (p, q, d) = map(int, input().split())
        up = p + p * d / 100
        down = up - up * d / 100
        lost = (p - down) * q
        total_loss = total_loss + lost
    print(total_loss)
