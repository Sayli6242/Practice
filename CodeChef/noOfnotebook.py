"""
Chef likes to write poetry. Today, he has decided to write a X pages long poetry, but unfortunately his notebook has only Y pages left in it. 
Thus he decided to buy a new CHEFMATE notebook and went to the stationary shop. Shopkeeper showed him some N notebooks, where the number of pages and price of the ith one are Pi pages and Ci rubles respectively. 
Chef has spent some money preparing for Ksen's birthday, and then he has only K rubles left for now.

Chef wants to buy a single notebook such that the price of the notebook should not exceed his budget and he is able to complete his poetry.

Help Chef accomplishing this task. You just need to tell him whether he can buy such a notebook or not. 
Note that Chef can use all of the Y pages in the current notebook, and Chef can buy only one notebook because Chef doesn't want to use many notebooks.

Input
The first line of input contains an integer T, denoting the number of test cases. Then T test cases are follow.

The first line of each test case contains four space-separated integers X, Y, K and N, described in the statement. 
The ith line of the next N lines contains two space-separated integers Pi and Ci, denoting the number of pages and price of the ith notebook respectively.

Output
For each test case, Print "LuckyChef" if Chef can select such a notebook, otherwise print "UnluckyChef" (quotes for clarity).
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
