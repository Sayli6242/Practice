"""
Chef took an examination two times. In the first attempt, he scored X marks while in the second attempt he scored Y marks. 
According to the rules of the examination, the best score out of the two attempts will be considered as the final score.

Determine the final score of the Chef.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains two integers X and Y — the marks scored by Chef in the first attempt and second attempt respectively.
Output Format
For each test case, output the final score of Chef in the examination.



"""

# take input for number of testcases
T = int(input())
# take input for each testcase
for i in range(T):
    X, Y = input().split()
    # convert input into integer
    marks_of_first_attempt = int(X)
    marks_of_second_attempt = int(Y)
    # calculate maximum number of marks
    total = max(marks_of_first_attempt, marks_of_second_attempt)
    # print result
    print(total)
