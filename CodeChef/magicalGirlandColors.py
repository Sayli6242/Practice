"""
Naturally, the magical girl is very good at performing magic. She recently met her master wizard Devu, who gifted her R potions of red liquid, B potions of blue liquid, and G potions of green liquid.

The red liquid potions have liquid amounts given by r[1], ..., r[R] liters.
The green liquid potions have liquid amounts given by g[1], ..., g[G] liters.
The blue liquid potions have liquid amounts given by b[1], ..., b[B] liters.
She want to play with the potions by applying magic tricks on them. In a single magic trick, she will choose a particular color. Then she will pick all the potions of the chosen color and decrease the amount of liquid in them to half (i.e. if initial amount of liquid is x, then the amount after decrement will be x / 2 where division is integer division, e.g. 3 / 2 = 1 and 4 / 2 = 2).

Because she has to go out of station to meet her uncle Churu, a wannabe wizard, only M minutes are left for her. In a single minute, she can perform at most one magic trick. Hence, she can perform at most M magic tricks.

She would like to minimize the maximum amount of liquid among all of Red, Green and Blue colored potions. Formally Let v be the maximum value of amount of liquid in any potion. We want to minimize the value of v. Please help her.


"""
"""
1) 
2)
3)



"""
T = int(input())
for t in range(T):
    R,G,B,M = input().split()
    