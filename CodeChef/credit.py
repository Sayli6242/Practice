"""
-To access CRED programs, one needs to have a credit score of 750750 or more.
-Given that the present credit score is XX, determine if one can access CRED programs or not.
-If it is possible to access CRED programs, output \texttt{YES}YES, otherwise output \texttt{NO}NO.

Input Format
-The first and only line of input contains a single integer XX, the credit score.

Output Format
-Print \texttt{YES}YES if it is possible to access CRED programs. Otherwise, print \texttt{NO}NO.
"""
x = int(input())
if x > 750:
    print("YES")
else:
    print("NO")
