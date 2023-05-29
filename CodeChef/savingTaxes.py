# cook your dish here
T = int(input())
for i in range(T):
    X,Y = input().split()
    amount1 = int(X)
    amount2 = int(Y)
    if amount1 > amount2 :
        tax = amount1 - amount2
        print(tax)
    
    # y < earn = had to pay tax
    # X (X > Y)