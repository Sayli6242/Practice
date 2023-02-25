"""


"""
T = int(input())
for t in range(T):
    n,k=map(int,input().split(" "))
    l=list(map(str, input().strip().split()))[:n]
    for i in range(k):
        if(l[-1]=='H'):
            l.pop()
            for i in range(len(l)):
                if l[i]=='H':
                    l[i]='T'
                else:
                    l[i]='H'
        else:
            l.pop()
    print(l.count("H"))