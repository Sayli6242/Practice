"""
Sergey recently learned about country codes - two letter strings, denoting countries. 
For example, BY stands for Belarus and IN stands for India. Mesmerized by this new discovery, Sergey now looks for country codes everywhere!
Sergey has recently found a string S consisting of uppercase Latin letters. He wants to find the number of different country codes that appear in S as contiguous substrings. 
For the purpose of this problem, consider that every 2-letter uppercase string is a valid country code.

Input
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first and only line of each test case contains a string S, consisting of uppercase Latin letters.

Output
For each test case, output a single line containing the number of different country codes appearing in the given string.

"""


T = int(input())
for i in range(T):
    lst = []
    s = input()
    count = 0
    for i in range(len(s) - 1):
        if s[i : i + 2] not in lst:
            lst.append(s[i : i + 2])
            count = count + 1
    print(count)
