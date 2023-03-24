"""
Given a string s. 
Can you make it a palindrome by deleting exactly one character? 
Note that size of the string after deletion would be one less than it was before.

"""
"""
1)
2)
3)



"""


T = int(input())
for t in range(T):
    s=input()
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            ss=s[:i]+s[i+1:]
            sss=s[:len(s)-1-i]+s[len(s)-i:]
            if ss == ss[::-1] or sss == sss[::-1]:
                print('YES')
                break
            else:
                print('NO')
                break 
    else:
        print('YES')
