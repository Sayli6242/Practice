"""
-Chef invented a modified wordle.
-There is a hidden word S and a guess word T, both of length 5.
-Chef defines a string MM to determine the correctness of the guess word. For the i-th index:
-If the guess at the i-thindex is correct, the i-th character of M is G.
-If the guess at the i-th index is wrong, the i-th character of MM is \texttt{B}B.
-Given the hidden word S and guess T, determine string M.

Input Format
-First line will contain T, number of test cases. Then the test cases follow.
-Each test case contains of two lines of input.
-First line contains the string S - the hidden word.
-Second line contains the string T - the guess word.
Output Format
-For each test case, print the value of string M.


"""
T = int(input())
for t in range(T):
    s = list(input())
    t = list(input())
    for i in range(len(s)):
        if s[i] == t[i]:
            print("G", end="")
        else:
            print("B", end="")
    print("")
