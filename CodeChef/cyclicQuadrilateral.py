"""
You are given the sizes of angles of a simple quadrilateral (in degrees) AA, BB, CC and DD, in some order along its perimeter. 
Determine whether the quadrilateral is cyclic.

Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 180^{\circ}180 
∘
 .

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first and only line of each test case contains four space-separated integers AA, BB, CC and DD.
Output
Print a single line containing the string "YES" if the given quadrilateral is cyclic or "NO" if it is not (without quotes).




"""

T = int(input())
for t in range(T):
    a, b, c, d = map(int, input().split())
    if a + c and b + d != 180:
        print("no")
    else:
        print("yes")
