"""




"""
"""
1) sort given binary string into two list alternatively using pop.
2) first check one team have more goals than other in five shots.
3) if yes then each team will take 5 more shots and whose goal is more,
   the team is winner.
4) and also check between two kicks one team has more goals than other team which is not defeatable then other team is winner.
5) also check if both teams has same goals then reasult is tie.
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
    print(chef_team)
    print(opp_team)