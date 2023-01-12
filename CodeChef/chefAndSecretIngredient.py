"""





"""
"""
1)  check each dish in given list.
2)  compare it with given amount of secrete ingredient
3)  if any of dish contains equal of more amount than given amount of secrete ingredient.
4)  count icreases by 1
5)  if not then count is 0
6)  then check if count is not equal to 0 then print Yes
7)  otherwise print no
"""
T = int(input())
for t in range(T):
    N, X = input().split()
    number_of_students = int(N)
    secrete_ingredient = int(X)
    A = list(map(int, input().split()))
    count = 0
    for i in A:
        if i >= secrete_ingredient:
            count = count + 1
            break
        else:
            count = count + 0
    if count != 0:
        print("Yes")
    else:
        print("no")
