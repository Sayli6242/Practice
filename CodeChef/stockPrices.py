"""
-Chef wants to buy a stock whose price was SS rupees when the market opened. He will buy the stock if and only if its price is in the range [A, B].
-The price of the stock has changed by C% by the time he was trying to buy the stock. Will he be able to buy the stock?

Input Format
-First line of the input contains TT, the number of testcases. Then the test cases follow.
-Each test case contains 44 space-separated integers S,A,B,C in a single line.
Output Format
-For each test case, if Chef buys the stock print YES, otherwise print NO.

"""
T = int(input())
for t in range(T):
    s, a, b, c = input().split()
    stock_price = int(s)
    num_a = int(a)
    num_b = int(b)
    num_c = int(c)
    stock_per = (stock_price * num_c) / 100
    if stock_per > 0:
        Total = stock_price + stock_per

        if Total in range(num_a, num_b):
            print("yes")

    else:
        print("no")
