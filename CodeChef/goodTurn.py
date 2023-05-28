"""
1) take input using input.
2) check sum of chefs num and chefina's num is greater than 6 
3) if yes then turn is good
4) otherwise bad.

"""
T = int(input())
for i in range(T):
    X,Y = input().split()
    chef_num_on_dice = int(X)
    chefina_num_on_dice = int(Y)
    total_of_both = chef_num_on_dice + chefina_num_on_dice
    if total_of_both > 6:
        print("YES")
    else:
        print("NO")
