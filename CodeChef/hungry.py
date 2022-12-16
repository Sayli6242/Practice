"""
-It's dinner time. Ashish is very hungry and wants to eat something. He has X rupees in his pocket. Since Ashish is very picky, he only likes to eat either PIZZA or BURGER.
-In addition, he prefers eating PIZZA over eating BURGER. The cost of a PIZZA is Y rupees while the cost of a BURGER is  rupees.
-Ashish can eat at most one thing. Find out what will Ashish eat for his dinner.

Input Format
-The first line will contain TT - the number of test cases. Then the test cases follow.
-The first and only line of each test case contains three integers XX, YY and ZZ - the money Ashish has, the cost of a PIZZA and the cost of a BURGER.
Output Format
-For each test case, output what Ashish will eat. (PIZZA, BURGER or NOTHING).

"""

T = int(input())
for t in range(T):
    x, y, z = input().split()
    num_x = int(x)
    num_y = int(y)
    num_z = int(z)
    if num_x >= num_y:
        print("Pizza")
    elif num_x >= num_z:
        print("Burger")
    else:
        print("Nothing")
