"""
Chef has a string SS with him. Chef is happy if the string contains a contiguous substring of length strictly greater than 22 in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are a, e, i, o, and u.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, a string SS.
Output Format
For each test case, if Chef is happy, print HAPPY else print SAD.


"""

T = int(input())
for t in range(T):
    s = input()
    sub_string = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i in sub_string:
            count = count + 1
            if count > 2:
                print("Happy")
                break
    else:
        print("Sad")
