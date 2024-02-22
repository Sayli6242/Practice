


T = int(input())

for i in range(T):
    
    N, M, K, L, R = map(int, input().split())

    min_price = 0

    # Iterate loop for each can
    for i in range(N):
        temp, price = map(int, input().split())
        for j in range(M):
            if temp > K + 1:
                temp -= 1
            elif temp < K - 1:
                temp += 1
            else:
                temp = K

        if L <= temp <= R:
            min_price = min(min_price, price)

    if min_price == 0:
        print(-1)
    else:
        print(min_price)
