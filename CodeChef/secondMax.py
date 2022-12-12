"""
-Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

Input
-First line contains the number of triples, N.
-The next N lines which follow each have three space separated integers.
Output
-For each of the N triples, output one new line which contains the second-maximum integer among the three.

1) take input of 3 x ,y ,z integers. 
2) apply if condition x is greater than y and z
3) again apply if condition y is greater than x and z
4) else print z
5) 

"""
T = int(input())
for t in range(T):
    x, y, z = input().split()
    num_x = int(x)
    num_y = int(y)
    num_z = int(z)
    if (num_x > num_y) and (num_y < num_z):
        print(num_x)
    elif (num_y > num_z) and (num_y < num_x):
        print(num_y)
    else:
        print(num_z)
