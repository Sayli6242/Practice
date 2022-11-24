"""
# You are given a string 's'  and width 'w' .
# Your task is to wrap the string into a paragraph of width 'w' .

1) take a string
2) iterate the list to get index 
3) print value at each index.  
4) compare modulo of each index up length l and print on new line
4) print 

s = ['123456789123456789']
"""

s = "123456789123456789"
l = 4
# print(len(s))
for i in range(0, len(s)):
    print(s[i], sep="", end="")
    # print((i + 1) % l == 0)
    if (i + 1) % l == 0:
        print(" ")
