"""
-There is a sale going on in Chefland. For every 2 items Chef pays for, he gets the third item for free (see sample explanations for more clarity).
-It is given that the cost of 1 item is X rupees. Find the minimum money required by Chef to buy at least N items.

Input Format
-First line will contain T, number of test cases. Then the test cases follow.
-Each test case contains of a single line of input, two integers N and X.
Output Format
-For each test case, output the minimum money required by Chef to buy at least NN items.

"""
T = int(input())
for t in range(T):
    n, x = input().split()
    num_of_items = int(n)
    cost_of_one_item = int(x)
    total = num_of_items - (num_of_items // 3)
    money_required_to_buy_items = total * cost_of_one_item
    print(money_required_to_buy_items)
