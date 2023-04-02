"""




"""
"""
1) sort given binary string into two list alternatively using pop.
2)
"""
T = int(input())
for t in range(T):
    p = list(input())
    chef_team = [ ]
    opp_team = [ ]
    count = 0
    for i in range(len(p)):
        if (count % 2) == 0:
            popped = p.pop(0)
            chef_team.append(popped)
            count+=1
        else:
            popped = p.pop(0)
            opp_team.append(popped)
            count+=1
        