"""
-Chef is shopping for masks. In the shop, he encounters 22 types of masks:
-Disposable Masks — cost XX but last only 11 day.
-Cloth Masks — cost YY but last 1010 days.
-Chef wants to buy masks to last him 100100 days. He will buy the masks which cost him the least. 
-In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks. Which type of mask will Chef choose?

Input Format
-The first line of input will contain a single integer TT, denoting the number of test cases. Then the test cases follow.
-Each test case consists of a single line of input, containing two space-separated integers X, YX,Y.
Output Format
-For each test case, if Chef buys the cloth masks print CLOTH, otherwise print DISPOSABLE.

"""


T = int(input())
for t in range(T):
    X, Y = input().split()
    X = int(X) * 10
    Y = int(Y) * 100
    if X > Y:
        print("Cloth")
    else:
        print("Disposable")
