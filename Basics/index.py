# """ 
#   inputStr[start:end:step]  syntax for slicing


# arr   i.like.this.program.very.much

# a     !
# b      !

res = like+"."+res

# message = "hey user"
# print(len(message))


# a = "Hey User!"
# print(len(a))


# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


# b = "google.com"

# y = str(123)
# x = "hello" * 3
# print(x, y)

# x = "hello" + "world"
# y = len(x)
# print(y, x)

# x = "hello" + "to python" + "world"
# for char in x:
#   y = char
#  print(y, ":", end=" ")


# num_1 = "100"
# num_2 = "200"

# num_1 = int(num_1)
# num_2 = int(num_2)

# print(num_1 + num_2)

# teams = ["India", "bulgeria", "naizeria", "kazakistan", "england"]
# print(len(teams))

# print(teams[0:2])

# teams.append("Pakistan")

# teams.insert(2, "pakistan")  # 2 denotes location of string

teams2 = ["urope", "arebia"]
teams.extend(teams2)

teams.remove("bulgeria")

popped = teams.pop()
print(popped)

teams.reverse()

teams2.sort()                       #sort out list in alphabetical order

nums = [1, 2, 3, 4, 5, 6]
nums.sort()                         #sort our list in assending order

nums.reverse()                       # sort our list in descending order

nums.sort(reverse=True)                  # also by using this we print list in descending order

print(teams2)

print(nums)

sorted_nums = sorted( nums)                 # getting sorted version of list without altering original list

print(sorted_nums)

print(sum(nums))

print(teams.index("bulgeria"))                  #to find index

for x in teams:                                  # instead of x u can use any variabel
  print(x)

for index, team in enumerate(teams):
  print(index, team)


# list are mutable and tuples are not
# """