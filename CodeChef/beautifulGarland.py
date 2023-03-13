"""
There is a garland — a cyclic rope with red and green flowers on it in some order. The sequence of flower colours is described by a string 
�
s; since the rope is cyclic, each two consecutive flowers are adjacent and the first and last flower are also adjacent.

The garland is beautiful if there is no pair of adjacent flowers with identical colours.

You want the garland to be beautiful. To achieve that, you may perform the following operation at most once:

Make two cuts on the rope (not intersecting the flowers), splitting the garland into two parts.
Reverse one of these two parts.
Tie together corresponding endpoints of the two parts, creating one whole garland again.
Can you find out whether it is possible to make the garland beautiful?

"""
"""
1)check for each color in list check next color is alternate. if all pairs are alternate string is beautiful, if any 
pair is not alternate break the loop,string is not beautiful.
2)find if in list idex of identical 2 pair of colors next to each other
3)if yes then reverse the pair and combine with first one. then follow 1st instruction.
4)if no then stop.
"""

T = int(input())
for t in range(T):
    S = list(input())
    flag = 0
    for i in range(len(S)):
        if S[i] == 'R' and S[i+1] == 'G':
            flag = True
            break
        else:
            S[i+1:2]
            total = S[i+1:3]
            z = total.reverse()
           
            S[i+1:3] = total
            flag = False
            
            if S[i] == 'R' and S[i+1] == 'G':
                flag = True
                break
            else:
                flag = False
                break
    if flag == True:
        print('yes')
    else:
        print('no')


        