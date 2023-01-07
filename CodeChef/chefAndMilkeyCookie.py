"""
Limak is a little polar bear, who loves eating cookies and drinking milk. For this reason he often visits Chef's kitchen.

Limak is going to spend N minutes in the kitchen. Each minute he either eats a cookie or drinks milk. 
Cookies are very sweet and thus Limak's parents have instructed him, that after eating a cookie, he has to drink milk in the next minute.

You are given whether he ate a cookie or drank milk in each of the N minutes. Your task is to check if Limak followed his parents' instructions. 
That is, you need to verify whether after each eaten cookie he drinks milk in the next minute. Print "YES" or "NO" for each test case accordingly.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains an integer N denoting the number of minutes.

The second line of a test case contains N space-separated strings S1, S2, ..., SN. The string Si is either "cookie" (if Limak eats a cookie in the i-th minute) or "milk" (otherwise).

Output
For each test case, output a single line containing the answer — "YES" if Limak followed his parents' instructions, and "NO" otherwise, both without the quotes.

Steps:

1) check position of cookies in list
2) also check position of milk after cookies in list.
3) if above steps are executed correctly then flag increase by 1
4) and continue to further steps
5) also check value in flag is equal to num of cookies on list
6) if condition gets true then print yes
7) if condition gets false then print no.
"""
T = int(input())
for t in range(T):
    N = int(input())
    S = list(input().split())
    flag = 0
    for i in range((N - 1)):
        if S[i] == "cookie" and S[i + 1] == "milk":
            flag += 1
        else:
            continue
    if flag == S.count("cookie"):
        print("yes")
    else:
        print("no")
