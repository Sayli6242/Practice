"""
Words that contain many consecutive consonants, like "schtschurowskia", are generally considered somewhat hard to pronounce.

We say that a word is hard to pronounce if it contains 44 or more consonants in a row; otherwise it is easy to pronounce. For example, "apple" and "polish" are easy to pronounce, but "schtschurowskia" is hard to pronounce.

You are given a string SS consisting of NN lowercase Latin characters. Determine whether it is easy to pronounce or not based on the rule above — print YES if it is easy to pronounce and NO otherwise.

For the purposes of this problem, the vowels are the characters \{a, e, i, o, u\}{a,e,i,o,u} and the consonants are the other 2121 characters.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains a single integer NN, the length of string SS.
The second line of each test case contains the string SS.
Output Format
For each test case, output on a new line the answer — YES if SS is easy to pronounce, and NO otherwise.

"""


T = int(input())
for t in range(T):
    num_n = int(input())
    num_s = input()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in num_s[0:4]:
        if i in vowels:
            count = count + 1
    if count >= 1 or num_n < 4:
        print("yes")
    else:
        print("no")
