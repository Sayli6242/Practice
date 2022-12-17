"""
-In Uttu's college, a semester is said to be a:
-Overload semester if the number of credits taken >65.
-Underload semester if the number of credits taken <35.
-Normal semester otherwise
-Given the number of credits XX taken by Uttu, determine whether the semester is Overload, Underload or Normal.

Input Format
The first line will contain TT - the number of test cases. Then the test cases follow.
The first and only of each test case contains a single integer XX - the number of credits taken by Uttu.


"""

T = int(input())
for t in range(T):
    num_of_credits = int(input())
    if num_of_credits > 65:
        print("overload")
    elif num_of_credits < 35:
        print("underload")
    else:
        print("normal")
