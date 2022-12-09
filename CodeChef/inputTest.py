"""
-You are given NN integers. Find the count of numbers divisible by KK.

Input Format
-The input begins with two positive integers N, K. The next N lines contains one positive integer each denoted by A.

Output Format
-Output a single number denoting how many integers are divisible by K.

"""
(n, k) = input().split()

count = 0

for i in range(int(n)):
    x = int(input())
    if int(x) % int(k) == 0:
        count = count + 1

print(count)
