"""
# You are given a string 's'  and width 'w' .
# Your task is to wrap the string into a paragraph of width 'w' .

1) take a string
2) iterate the list
3) store each element and append to new list to lenght(w)
4) print each element from list 

s = ['123456789123456789']
"""

s = "123456789123456789"
l = 4
# print(len(s))
for i in range(0, len(s)):
    if (i + 1) % l - 1 == 0:
        print("\n")

    print(s[i], sep="", end="")
