"""
-In the current semester, you have taken X RTP courses, Y Audit courses and Z Non-RTP courses.
-The credit distribution for the courses are:
-4 credits for clearing each RTP course.
-2 credits for clearing each Audit course.
-No credits for clearing a Non-RTP course.
-Assuming that you cleared all your courses, report the number of credits you obtain this semester.

Input Format
-The first line contains a single integer T, the number of test cases. T test cases follow. 
-Each test case consists of one line, containing 33 integers separated by spaces.
-The first integer is X, the number of RTP courses.
-The second integer is Y, the number of Audit courses.
-The third integer is Z, the number of non-RTP courses.
"""

T = int(input())
for t in range(T):
    x, y, z = input().split()
    num_x = int(x)
    num_y = int(y)
    num_z = int(z)
    RTP_course = num_x * 4
    Audit_course = num_y * 2
    non_RTPcourse = num_z * 0

    num_reportCard = RTP_course + Audit_course + non_RTPcourse
    print(num_reportCard)
