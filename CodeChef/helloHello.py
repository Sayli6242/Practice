"""
Chef talks a lot on his mobile phone. 
As a result he exhausts his talk-value (in Rokdas) very quickly.
One day at a mobile recharge shop, he noticed that his service provider gives add-on plans which can lower his calling rates (Rokdas/minute). 
One of the plans said "Recharge for 28 Rokdas and enjoy call rates of 0.50 Rokdas/min for one month". 
Chef was very pleased. His normal calling rate is 1 Rokda/min. And he talked for 200 minutes in last month, which costed him 200 Rokdas. 

If he had this plan activated, it would have costed him: 28 + 0.60*200 = 128 Rokdas only! Chef could have saved 72 Rokdas.

But if he pays for this add-on and talks for very little in the coming month, he may end up saving nothing or even wasting money. 
Now, Chef is a simple guy and he doesn't worry much about future. He decides to choose the plan based upon his last month’s usage.

There are numerous plans. 
Some for 1 month, some for 15 months. 
Some reduce call rate to 0.75 Rokdas/min, 
some reduce it to 0.60 Rokdas/min. 
And of course each of them differ in their activation costs. 

Note - If a plan is valid for M months, then we must pay for (re)activation after every M months (once in M months). 
Naturally, Chef is confused, and you (as always) are given the task to help him choose the best plan.

"""
T = int(input())
for t in range(T):
    D_rate, no_of_min , Plan = map(float, input().split())
    savings = 0
    bestValue = 0
    z = D_rate * Plan
    print(z)
    for i in range(int(Plan)):
        Months, Rate, Cost = map(float,input().split())
        Monthy_cost = Cost / Months
        print(Monthy_cost)
    # Months = int(input())
    # Rate = int(input())
    # Cost = int(input())
   
    