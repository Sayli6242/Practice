"""
Chef is on his way to become the new big bull of the stock market 
but is a bit weak at calculating whether he made a profit or a loss on his deal.

Given that Chef bought the stock at value X and sold it at value Y. 
Help him calculate whether he made a profit, loss, or was it a neutral deal.


"""


T = int(input())
for t in range(T):
    x,y = input().split()
    initial_Stock_value = int(x)
    sold_value = int(y)
    if initial_Stock_value < sold_value:
        print("PROFIT")
    elif initial_Stock_value > sold_value:
        print("LOSS")
    else:
        print("Neutral")