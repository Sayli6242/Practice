"""
Somu went to the gym today. He decided to do XX sets of squats. Each set consists of 1515 squats. 
Determine the total number of squats that he did today.

Input Format
- The first line contains a single integer TT — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer XX — the total number of sets of squats that Somu did.
Output Format
- For each test case, output the total number of squats done by Somu.
"""
# T is no. of testCases
T = int(input())

for t in range(T):
    # x is input for each testcase
    x = int(input())
    x = x * 15
    print(x)