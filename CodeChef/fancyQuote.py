"""
"I don't have any fancy quotes." - vijju123

Chef was reading some quotes by great people. Now, he is interested in classifying all the fancy quotes he knows. 
He thinks that all fancy quotes which contain the word "not" are Real Fancy; quotes that do not contain it are regularly fancy.

You are given some quotes. For each quote, you need to tell Chef if it is Real Fancy or just regularly fancy.
"""
"""
1) take list of inputs as string
2) iterate list
3) check word "not" is in list
4) if yes then print 'Real Fancy' and break
5) else print regularly fancy

"""

T = int(input())
for t in range(T):
    S = input().split()
    for i in S:
        if i == 'not':
            print('Real Fancy')
            break
    else:
        print('regularly fancy')