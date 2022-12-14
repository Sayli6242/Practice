"""
-Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be X°F.
-A person is said to have fever if his body temperature is strictly greater than 98°F.
-Determine if Chef has fever or not.

Input Format
-The first line contains a single integer T — the number of test cases. Then the test cases follow.
-The first and only line of each test case contains one integer X - the body temperature of Chef in °F.
Output Format
-For each test case, output YES if Chef has fever. Otherwise, output NO.

"""

T = int(input())
for t in range(T):
    x = int(input())
    if x > 98:
        print("Yes")
    else:
        print("No")
