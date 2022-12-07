"""
-A study has shown that playing a musical instrument helps in increasing one's IQ by 7 points.
-Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.
-You know that Einstein had an IQ of 170, and Chef currently has an IQ of X.
-Determine if, after learning to play a musical instrument, Chef's IQ will become strictly greater than Einstein's.
-Print "Yes" if it is possible for Chef to beat Einstein, else print "No" (without quotes).

Input Format
-The first and only line of input will contain a single integer XX, the current IQ of Chef.

"""
x = int(input())
if x < 170:
    print("Yes")
else:
    print("No")
