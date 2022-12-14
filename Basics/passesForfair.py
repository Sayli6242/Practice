"""
-There is a fair going on in Chefland. Chef wants to visit the fair along with his N friends. Chef manages to collect KK passes for the fair. 
-Will Chef be able to enter the fair with all his N friends?
-A person can enter the fair using one pass, and each pass can be used by only one person.

Input Format
-The first line of input will contain a single integer T, denoting the number of test cases.
-Each test case consists of a single line containing two space-separated integers N, K.
Output Format
-For each test case, print on a new line YES if Chef will be able to enter the fair with all his N friends and NO otherwise.



"""
T = int(input())
for t in range(T):
    n, k = input().split()
    num_n = int(n)
    num_k = int(k)
    if (num_n + 1) <= num_k:
        print("YES")
    else:
        print("NO")
