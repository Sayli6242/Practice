"""
- Chef's dog binary hears frequencies starting from 6767 Hertz to 4500045000 Hertz (both inclusive).

- If Chef's commands have a frequency of XX Hertz, find whether binary can hear them or not.

Input Format
- The first line of input will contain a single integer TT, denoting the number of test cases.
- Each test case consists of a single integer XX - the frequency of Chef's commands in Hertz.

"""


T = int(input())
for t in range(T):
    X = int(input())
    if X >= 67 and X <= 45000:
        print("YES")
    else:
        print("NO")
