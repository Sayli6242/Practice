T = int(input())
for t in range(T):
    s = list(input())
    t = list(input())
    for i in range(len(s)):
        if s[i] == t[i]:
            print("G", end="")
        else:
            print("B", end="")