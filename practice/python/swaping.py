# Python program to interchange first and last elements in a list

# for i in range(12, 16):
# print(i)

lst = [1, 2, 3, 4, 5]
# list[4] = int(4)
# list[3] = int(3)
# list[2] = int(2)
# list[1] = int(1)
# list[0] = int(5)
# a,b=b,a

l = len(lst)
# lst[0], lst[l - 1] = lst[l - 1], lst[0]

#

n = 3
for i in range(n):
    popped = lst.pop()
    lst = [popped] + lst

print(lst)

# 51234
