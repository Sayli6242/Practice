"""






"""
"""
1) obtain number of pages required (X - Y)
2) check notebook of quantity of those num of pages available in shop or not (z < p[i])
3) then check their price of notebook and compare with leftover coins. (k == c[i])
4) if all above conditions satisfies then print 'yes'.
5) otherwise print 'no'
"""
T = int(input())
for t in range(T):
    x, y, k, n = input().split()
    len_of_poetry = int(x)
    leftover_pages = int(y)
    rubles_chef_has = int(k)
    num_of_notebooks = int(n)
    pages = list(map(int, input().split()))
    price_of_notebook = list(map(int, input().split()))
    # print(price_of_notebook)
    num_of_pgs_req = len_of_poetry - leftover_pages
    res = {}
    for key in pages:
        for value in price_of_notebook:
            res[key] = value
            price_of_notebook.remove(value)
            break

    Flag = True
    for key in res:
        if num_of_pgs_req <= res.get(key):
            if rubles_chef_has < res.get(value):
                Flag = True
        else:
            Flag = False
    if Flag == True:
        print("luckychef")
    else:
        print("unluckyChef")
