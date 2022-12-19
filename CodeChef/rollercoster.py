"""
Chef's son wants to go on a roller coaster ride. The height of Chef's son is XX inches while the minimum height required to go on the ride is HH inches. Determine whether he can go on the ride or not.

Input Format
The first line contains a single integer TT - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers XX and HH - the height of Chef's son and the minimum height required for the ride respectively.
Output Format
For each test case, output in a single line, YES if Chef's son can go on the ride. Otherwise, output NO.



"""
T = int(input())
for t in range(T):
    x, H = input().split()
    son_height = int(x)
    minimum_height_required = int(H)
    if son_height >= minimum_height_required:
        print("Yes")
    else:
        print("No")
