"""




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