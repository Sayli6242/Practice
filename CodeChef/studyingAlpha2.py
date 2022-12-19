"""
Not everyone probably knows that Chef has younger brother Jeff. Currently Jeff learns to read.

He knows some subset of the letter of Latin alphabet. In order to help Jeff to study, Chef gave him a book with the text consisting of N words. Jeff can read a word iff it consists only of the letters he knows.

Now Chef is curious about which words his brother will be able to read, and which are not. Please help him!

Input
The first line of the input contains a lowercase Latin letter string S, consisting of the letters Jeff can read. Every letter will appear in S no more than once.

The second line of the input contains an integer N denoting the number of words in the book.

Each of the following N lines contains a single lowecase Latin letter string Wi, denoting the ith word in the book.

Output
For each of the words, output "Yes" (without quotes) in case Jeff can read it, and "No" (without quotes) otherwise.
"""

S = input()
N = int(input())
for i in range(N):
    W = input()
    c = 0
    for i in W:
        if i not in S:
            c += 1
    if c != 0:
        print("NO")
    else:
        print("YES")
