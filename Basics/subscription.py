"""
-Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.
-The meeting platform supports a meeting of maximum 30 minutes without subscription and a meeting of unlimited duration with subscription.
-Determine whether Chef needs to take a subscription or not for setting up the meet.

Input Format
-First line will contain T, the number of test cases. Then the test cases follow.
-Each test case contains a single integer X - denoting the duration of the lecture.
Output Format
-For each test case, print in a single line, YES if Chef needs to take the subscription, otherwise print NO.


"""
T = int(input())
for t in range(T):
    x = int(input())
    if x > 30:
        print("YES")
    else:
        print("NO")
