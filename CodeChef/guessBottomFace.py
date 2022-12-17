"""
-It is known that in regular dice, the sum of opposite faces is 7.
-A regular dice is rolled and you are given the value X showing on the top face. Determine the value on the bottom face.

Input Format
-The first line will contain T - the number of test cases. Then the test cases follow.
-The first and only of each test case contains a single integer X - the value on the top face.
Output Format
-For each test case, output the value on the bottom face.
"""
T = int(input())
for t in range(T):
    value_on_topface = int(input())
    value_on_bottomface = 7 - value_on_topface
    print(value_on_bottomface)
