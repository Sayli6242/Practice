"""
-Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is X  km away from his home.

-If his office is open on 5 days in a week, find the number of kilometers Chef travels through office trips in a week.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of a single line consisting of single integer X.

"""
T = int(input())
for t in range(T):
    X = int(input())
    z = (X * 20) * 5
    print(z)
