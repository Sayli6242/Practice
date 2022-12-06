"""
-Chef appeared for an exam consisting of 3 sections. Each section is worth 100 marks.
-Chef scored AA marks in Section 1, BB marks in section 2, and C marks in section 3.
-Chef passes the exam if both of the following conditions satisfy:
-Total score of Chef is ≥100;
-Score of each section ≥10.
-Determine whether Chef passes the exam or not.

Input Format
-The first line of input will contain a single integer T, denoting the number of test cases.
-Each test case consists of a single line containing 3 space-separated numbers A,B,C - Chef's score in each of the sections.
Output Format
-For each test case, output PASS if Chef passes the exam, FAIL otherwise.
-Note that the output is case-insensitive i.e. PASS, Pass, pAsS, and pass are all considered same.
"""

T = int(input())
for t in range(T):
    A, B, C = input().split()
    total_score = int(A) + int(B) + int(C)
    if total_score >= 100:
        if int(A) >= 10 and int(B) >= 10 and int(C) >= 10:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")
