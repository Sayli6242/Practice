"""
In an attempt to control the rise in population, Archer was asked to come up with a plan. This time he is targeting marriages. 
Archer, being as intelligent as he is, came up with the following plan:
A man with name M is allowed to marry a woman with name W, only if M is a subsequence of W or W is a subsequence of M.
A is said to be a subsequence of B, if A can be obtained by deleting some elements of B without changing the order of the remaining elements.
Your task is to determine whether a couple is allowed to marry or not, according to Archer's rule.

Input :
The first line contains an integer T, the number of test cases. T test cases follow. Each test case contains two space separated strings M and W.

Output :
For each test case print "YES" if they are allowed to marry, else print "NO". (quotes are meant for clarity, please don't print them)



"""
T = int(input())
for i in range(T):
    x,y = input().split()
    if len(x)>len(y):
        x,y = y,x
    i = 0
    for j in y :
        if j == x[i]:
            i+=1
        if i == len(x):
            break
    if i == len(x):
        print("YES")
    else:
        print("NO")