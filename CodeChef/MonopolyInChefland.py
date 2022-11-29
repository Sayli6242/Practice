"""


"""

T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    print(lst)
    for i in range(len(lst)):
        temp = sum(lst)
        print(temp)
        total = temp - lst[i]
        print(total)
    if total > temp:
        print("YES")

    else:
        print("NO")

    # sum of two companies is greater than third one then print YES.
    # calculate sum of three comapanies then minus value of third one and compare with sum.
    # if R1+:
    #     print("YES")
    # else:
    #     print("NO")
