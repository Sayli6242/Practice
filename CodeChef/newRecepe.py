"""
Rupsa recently started to intern under Chef. 
He gave her N type of ingredients of varying quantity A1, A2, ..., AN respectively to store it. 
But as she is lazy to arrange them she puts them all in a storage box.
Chef comes up with a new recipe and decides to prepare it. 
He asks Rupsa to get two units of each type ingredient for the dish. 
But when she went to retrieve the ingredients, she realizes that she can only pick one item at a time from the box and can know its type only after she has picked it out. 
The picked item is not put back in the bag.
She, being lazy, wants to know the maximum number of times she would need to pick items from the box in the worst case so that it is guaranteed that she gets at least two units of each type of ingredient. 
If it is impossible to pick items in such a way, print -1.

"""
"""
1)iterate over list
2) check each ingredient is double in quantity
3) if yes then count the no of times ingredient is picked
4) divide each quantity of ingredints into 2 halfs
5) count sum of all half of ingredients
6) print count
 
"""
T = int(input())
for t in range(T):
    N = int(input())
    A =list(map(int,input().split()))
    l = 0
    for i in A:
        if i == 2:
            sum(A)
        else:
            l = l - 1
    print(l)
        
       
        
