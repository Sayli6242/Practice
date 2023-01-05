"""
Donald Drumpf has spent the entire summer lobbying to gather votes for the upcoming student government election. At his University, 
there are a total of N students. Each student in the university casts a vote. The size of student government is determined by the number of students that get at least K votes.

Each person that receives at least K votes is given a post in the student government. The Dean noticed that every year, 
there are a few students who vote for themselves. He decided to add a rule to disqualify any such individuals who vote for themselves i.e they cannot be part of the student government.

You are given an array A, where Ai denotes the person who the i-th person voted for. Can you compute the size of the student government?

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

For each test case, first line consists of two space separated integers N, K.

Second line consists of N space separated integers denoting the array A, where i-th integer denotes Ai.

Output
For each test case, output a single line containing an integer corresponding to the size of the student government.
"""
"""
1) check each student got K no. of votes
2) if k no of votes lies in the list for each student then increase count by 1
3) if not then stop.
4) 
5)
"""

N, K = input().split()
votes = int(K)
A = list(map(int, input().split()))
size = 0
count = 0
for i in A:
    if i == votes:
        count = count + 1
        if count == votes:
            size = size + 1
        print(size)
