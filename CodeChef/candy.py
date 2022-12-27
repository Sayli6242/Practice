"""


Abhi is a salesman. He was given two types of candies, which he is selling in NN different cities.

For the prices of the candies to be valid, Abhi's boss laid down the following condition:

A given type of candy must have distinct prices in all NN cities.
In his excitement, Abhi wrote down the prices of both the candies on the same page and in random order instead of writing them on different pages. 
Now he is asking for your help to find out if the prices he wrote are valid or not.

More formally, you are given an array AA of size 2N2N. Find out whether it is possible to split AA into two arrays, each of length NN, such that both arrays consist of distinct elements.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains one integer NN, denoting the number of cities
The second line contains 2N2N space-separated integers A_1, A_2, \ldots, A_{2N}A 
​— the elements of the array AA.
Output Format
For each test case output the answer on a new line — Yes if the given array represents a valid list of prices, and No otherwise.




"""
# take input for no. of testcases
T = int(input())
# take input for each testcase
for t in range(T):
    # N is number of different cities
    N = int(input())
    A = list(map(int, input().split()))
    # take a list of element for price of both candies
    lst = []
    for element in lst:
        lst.append(A.count(element))
    # compare list size upto 2
    if max(lst) > 2:
        print("no")
    else:
        print("yes")
