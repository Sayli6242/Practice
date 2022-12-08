"""
-You are given NN integers. Find the count of numbers divisible by KK.

Input Format
-The input begins with two positive integers NN, KK. The next NN lines contains one positive integer each denoted by A_i
.

Output Format
-Output a single number denoting how many integers are divisible by KK.
"""

(n, k) = map(int, input().split())

ans = 0

for i in range(n):
    x = int(input())
    if x % k == 0:
        ans += 1

print(ans)
