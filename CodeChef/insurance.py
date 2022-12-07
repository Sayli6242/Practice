"""
-Chef bought car insurance. The policy of the insurance is:
-The maximum rebatable amount for any damage is Rs XX lakhs.
-If the amount required for repairing the damage is <+X lakhs, that amount is rebated in full.
-Chef's car meets an accident and required Rs YY lakhs for repairing.
-Determine the amount that will be rebated by the insurance company.

Input Format
-The first line of input will contain a single integer TT, denoting the number of test cases.
-The first and only line of each test case contains two space-separated integers XX and YY.
Output Format
-For each test case, output the amount (in lakhs) that will be rebated by the insurance company.
"""

T = int(input())
for t in range(T):
    X, Y = input().split()
    print(min(X, Y))
