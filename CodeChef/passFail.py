"""
Chef is struggling to pass a certain college course.

The test has a total of NN questions, each question carries 33 marks for a correct answer and -1−1 for an incorrect answer.
 Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got XX questions correct and the rest of them incorrect. For Chef to pass the course he must score at least PP marks.

Will Chef be able to pass the exam or not?

Input Format
First line will contain TT, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three integers N, X, PN,X,P.
Output Format
For each test case output "PASS" if Chef passes the exam and "FAIL" if Chef fails the exam.




"""

T = int(input())
for t in range(T):
    n, x, p = map(int, input().split())
    a = x * 3
    b = n - x
    c = a - b
    if p <= c:
        print("PASS")
    else:
        print("FAIL")
