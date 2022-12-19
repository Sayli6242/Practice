"""
In Chefland, precipitation is measured using a rain gauge in millimetre per hour.

Chef categorises rainfall as:

LIGHT, if rainfall is less than 33 millimetre per hour.
MODERATE, if rainfall is greater than equal to 33 millimetre per hour and less than 77 millimetre per hour.
HEAVY if rainfall is greater than equal to 77 millimetre per hour.
Given that it rains at XX millimetre per hour on a day, find whether the rain is LIGHT, MODERATE, or HEAVY.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single integer XX — the rate of rainfall in millimetre per hour.
Output Format
For each test case, output on a new line, whether the rain is LIGHT, MODERATE, or HEAVY.



"""
T = int(input())
for t in range(T):
    x = int(input())
    if x < 3:
        print("Light")
    elif x >= 3 and x < 7:
        print("Moderate")
    else:
        print("Heavy")
