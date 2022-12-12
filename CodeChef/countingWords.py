"""
-Harsh was recently gifted a book consisting of NN pages. Each page contains exactly MM words printed on it. As he was bored, he decided to count the number of words in the book.
-Help Harsh find the total number of words in the book.

Input Format
-The first line of input will contain a single integer TT, denoting the number of test cases.
-Each test case consists of two space-separated integers on a single line, NN and MM — the number of pages and the number of words on each page, respectively.
Output Format
-For each test case, output on a new line, the total number of words in the book.
"""

T = int(input())
for t in range(T):
    n, m = input().split()
    num_n = int(n)
    num_m = int(m)
    total = num_n * num_m
    print(total)
