"""
-Chef's computer has NN GB of free space. He wants to save X files, each of size 1 GB and Y files, each of size 2 GB on his computer.
-Will he be able to do so?
-Chef can save all the files on his computer only if the total size of the files is less than or equal to the space available on his computer.

Input Format
-The first line contains an integer T, denoting the number of test cases. The T test cases then follow:
-The first and only line of each test case contains three integers N, X, Y denoting the free-space in computer, the number of 1 and 2 GB files respectively.
Output Format
-For each test case, print YES if Chef is able to save the files and NO otherwise.

"""
T = int(input())
for t in range(T):
    n,x,y = input().split()
    num_x = int(x)
    num_y = int(y)
    num_n = int(n)
    num1 = num_x *1
    num2 = num_y *2
    total_size = num1 + num2
    if num_n >= total_size:
        print('YES')
    else:
        print('NO')