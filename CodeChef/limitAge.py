"""
1) by taking input of three numbers(chefs current age, minimum age limit and max age limit )
2) check chefs current age is greater than minimum age limit and 
    smaller than maximum age limit by comparing it with given min and max age.
3) if conditions of min age and max age is true then chef is eligible
4) otherwise not eligible for exam.
"""
T = int(input())
for i in range(T):
    X ,Y,A = input().split()
    min_age = int(X)
    max_age = int(Y)
    chef_current_age = int(A)
    if chef_current_age >= min_age and chef_current_age < max_age:
        print('YES')
    else:
        print('NO')