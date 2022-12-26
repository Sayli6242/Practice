"""
Ada's classroom contains N⋅M tables distributed in a grid with NN rows and M columns. Each table is occupied by exactly one student.

Before starting the class, the teacher decided to shuffle the students a bit. After the shuffling, each table should be occupied by exactly one student again. 
In addition, each student should occupy a table that is adjacent to that student's original table, i.e. immediately to the left, right, top or bottom of that table.

Is it possible for the students to shuffle while satisfying all conditions of the teacher?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers N and M.
Output
For each test case, print a single line containing the string "YES" if it is possible to satisfy the conditions of the teacher or "NO" otherwise (without quotes).
"""


# taking input for tastecases
T = int(input())
for t in range(T):

    # take input for each testcase
    N, M = input().split()

    # converting two space saperated input into integer
    num_of_rows = int(N)
    num_of_columns = int(M)

    # calculating shuffle of student
    if (num_of_rows % 2) and (num_of_columns % 2):
        print("yes")
    else:
        print("No")
