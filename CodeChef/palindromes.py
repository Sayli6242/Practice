"""
You are given two positive integers AA and BB. You need to construct two different binary strings (i.e, they are strings which consist of only 00s and 11s), which satisfy these two conditions:

Both the strings should be palindromes.
Each string should have exactly AA 00s, and exactly BB 11s in them.
Output Yes if two such different binary strings can be constructed and No otherwise.

Note:

A string is said to be a palindrome, if the string and the reverse of the string are identical.
Two strings are said to be different if either their lengths are different, or if they differ in at least one character.
Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case contains two space-separated integers, AA and BB, in a new line.
Output Format
For each test case, output on a new line 'Yes', if you can construct two different binary strings satisfying the conditions. If not, output No.



"""
"""
1) take two positive integer(A & B)
2) check input no is even or odd if both of them are odd then print no
3) print result.

""" 
T = int(input())
for t in range(T):
    A,B = input().split()
    num_a = int(A)
    num_b = int(B)
    if num_a% 2 == 0 or num_b% 2 == 0:
        print('yes')
    else:
        print('no')