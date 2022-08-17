"""
Program to Add two Matrices
input - two matrices
Output - one matrix (which has elements with sum of two matrix elements


1.
"""



M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,1,1],[1,1,1],[1,1,1,]]
M3 = []
result = 0
for i in range(len(M1)):
    # print(M1[i])
    l =[]
    for j in range(len(M1[i])):
       s = M1[i][j]+M2[i][j]
       l.append(s)
    M3.append(l)

print(M3)


#result+=1
