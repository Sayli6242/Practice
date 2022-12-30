"""


"""
T = int(input())
for t in range(T):
    N = int(input())
    pool_of_letters = list(input())
    meal = "codechef"
    count = 0
    for i in pool_of_letters:
        if i in meal:
            pool_of_letters.pop(i)
            print(pool_of_letters.pop(i))
            if i == meal[i]:
                count += 1
        else:
            break
