"""


"""

T = int(input())
for t in range(T):
    is_dominant = False
    armies = input().split()
    army = [int(a) for a in armies]
    for a in range(len(armies)):
        total = sum(army) - army[a]
        if army[a] > total:
            print("YES")
            is_dominant = True
            break
    if is_dominant != True:
        print("NO")
