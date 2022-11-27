"""
A school has following rules for grading system:
a. Below 25 - F

b. 25 to 45 - E

c. 45 to 50 - D

d. 50 to 60 - C

e. 60 to 80 - B

f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

"""
"""
1.take input from user
2.intialize list inside list make sublist which contain marks and grades of students.
3.apply for loop 
4.inside for loop make conditions to check and access index value inside sublist 
5.print result


"""

m = int(input('enter marks'))
grades = [[0,25,'F'],[25,45,'E'],[45,50,'D'],[50,60,'c'],[60,80,'B'],[80,100,'A']]

for g in grades:
    if m >= g[0] and  m <= g[1]:
        print(g[2])
    
