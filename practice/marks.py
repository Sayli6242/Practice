grades = [[0,25,"F"],[26,100,'A']]
m = 13
for g in grades:

    if m >= g[0] and  m <= g[1]:
        print(g[2])
