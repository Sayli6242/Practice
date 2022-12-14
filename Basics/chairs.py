"""
-Chef's coding class is very famous in Chefland.
-This year X students joined his class and each student will require one chair to sit on. Chef already has Y chairs in his class.
 Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.

Input Format
-The first line contains a single integer T — the number of test cases. Then the test cases follow.
-The first and only line of each test case contains two integers X and Y — the number of students in the class and the number of chairs Chef already has.
Output Format
-For each test case, output the minimum number of extra chairs Chef must buy so that every student gets one chair.
"""

T = int(input())
for t in range(T):
    x, y = input().split()
    num_x = int(x)
    num_y = int(y)
    if num_x >= num_y:
        total = num_x - num_y
        print(total)
    else:
        print(0)
