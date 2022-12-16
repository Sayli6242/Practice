"""
-A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
-Chef was only able to sleep X hours yesterday. Determine if he is sleep deprived or not.

Input Format
-The first line contains a single integer T — the number of test cases. Then the test cases follow.
-The first and only line of each test case contains one integer X — the number of hours Chef slept.
Output Format
-For each test case, output YES if Chef is sleep-deprived. Otherwise, output NO.

"""
T = int(input())
for t in range(T):
    x = int(input())
    if x < 7:
        print("YES")
    else:
        print("No")
