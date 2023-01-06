"""




"""
"""
1) obtain the num which is divisible by Alice and Not divisible by bob.
2) if there is no num present who satisfies the condition return -1
4) print result

"""
T = int(input())
for t in range(T):
    a, b, n = map(int, input().split())
    if a % b == 0:
        print("-1")
    elif n % a == 0 and n % b != 0:
        print(n)
    else:
        x = a * ((n // a) + 1)
        if x % b == 0:
            print(x + a)
        else:
            print(x)
