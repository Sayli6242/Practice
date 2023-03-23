"""
You are a poor person in ChocoLand. Here, people eat chocolates daily instead of normal food. 
There is only one shop near your home; this shop is closed on Sunday, but open on all other days of the week. 
You may buy at most one box of N chocolates from this shop on each day when it is open.

Currently, it's Monday, and you need to survive for the next S days (including the current day). 
You have to eat K chocolates everyday (including the current day) to survive. 
Do note that you are allowed to buy the a chocolate box and eat from it on the same day.

Compute the minimum number of days on which you need to buy from the shop so that you can survive the next S days, 
or determine that it isn't possible to survive.



"""
T = int(input())
for t in range(T):
    N,K,S = input().split()
    num_of_choco_in_box = int(N)
    num_of_choco_eat_everyday = int(K)
    num_of_surviving_day = int(S)
    
    total = num_of_choco_eat_everyday*num_of_surviving_day
    z = num_of_surviving_day //7
    opend = num_of_surviving_day - z
    choco = num_of_choco_in_box - num_of_choco_eat_everyday
    
    if total > (num_of_choco_in_box * opend) or (num_of_surviving_day >= 7 and 
    choco*6 < num_of_choco_eat_everyday):
        print(-1)
    else:
        result = total//num_of_choco_in_box
        if total % num_of_choco_in_box != 0:
            result+=1
        print(result)