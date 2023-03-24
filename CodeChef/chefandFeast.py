"""
Chef has prepared a feast with N dishes for you. 
You like Chef's cooking, and so you want to eat all the dishes he has prepared for you. 
You are also given an array A of size N, where Ai represents the happiness you get by eating the i-th dish.
You will eat all the dishes in a series of steps. In each step, 
you pick a non empty subset of the remaining dishes and eat them. 
The happiness you get from eating these dishes is the size of the subset multiplied by t
he sum of the individual happiness from the dishes in the subset. You want to maximize the happiness you get from the entire feast,
 which is the sum of happiness in each step.

"""
"""
1)
2)
3)


"""
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    for i in A:
        pass