"""
Chef categorises an instagram account as spam, if, the following count of the account is more than 
10
10 times the count of followers.

Given the following and follower count of an account as 
�
X and 
�
Y respectively, find whether it is a spam account.

Input Format
The first line of input will contain a single integer 
�
T, denoting the number of test cases.
Each test case consists of two space-separated integers 
�
X and 
�
Y — the following and follower count of an account, respectively.
Output Format
For each test case, output on a new line, YES, if the account is spam and NO otherwise.

You may print each character of the string in uppercase or lowercase. For example, the strings YES, yes, Yes and yES are identical.



"""

T = int(input())
for t in range(T):
    x,y=map(int,input().split())
    if x>y*10:
        print("yes")
    else:
        print("no")