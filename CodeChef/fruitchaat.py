"""
-Chef has closed his restaurant and decided to run a fruit stand instead. 
-His signature dish is a fruit chaat consisting of 2 bananas and 1 apple. He currently has X bananas and Y apples. How many chaats can he make with the fruits he currently has?

Input Format
-The first line will contain T, the number of testcases. Then the testcases follow.
-Each testcase consists of a single line containing two space separated integers - X and Y
Output Format
-For each testcase, output the answer on a new line.
"""


T = int(input())
for t in range(T):
    x, y = input().split()
    number_of_bananas = int(x)
    number_of_apples = int(y)
    number_of_chat = number_of_bananas // 2
    print(min(number_of_chat, number_of_apples))
