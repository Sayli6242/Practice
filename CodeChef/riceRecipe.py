"""




"""


T = int(input())
for t in range(T):
    N = int(input())
    for i in range(N):
        vote = input().split()
        d = {}
        d = {vote[i]: vote[i + 1] for i in range(0, len(vote))}
    print(d)
