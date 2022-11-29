"""
- Alice has a bucket of water initially having W litres of water in it.
- The maximum capacity of the bucket is X liters.
- Alice turned on the tap and the water starts flowing into the bucket at a rate of Y litres/hour. 
- She left the tap running for exactly ZZ hours. Determine whether the bucket has been overflown, 
- filled exactly, or is still left unfilled.

OUTPUT FORMAT
- For each test case, print the answer on a new line:
- If the bucket has overflown print overflow.
- If it is exactly filled print filled.
- If it is still unfilled, print unfilled. 

"""
T = int(input())
for t in range(T):
    W, X, Y, Z = input().split()
    if int(W) + int(Y) * int(Z) == int(X):
        print("FILLED")
    elif int(W) + int(Y) * int(Z) <= int(X):
        print("UNFILLED")
    else:
        print("OVERFLOW")

    # print(int(W) + int(Y) * int(Z))
