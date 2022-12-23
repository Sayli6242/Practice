"""
Chef loves Chess and has thus invented a new piece named "Disabled King".

Let's denote the cell at the intersection of the ii-th column from the left and jj-th row from the top by (i, j)(i,j).

If he is currently in cell (x,y)(x,y), the disabled king can move to the following positions in one move (provided that he remains in the chessboard):

(x,y+1)
(x,y-1)
(x+1,y+1)
(x+1,y-1)
(x-1,y+1)
(x-1,y-1)
In short, the Disabled King cannot move horizontally.

In an N \times NN×N chessboard, the Disabled King is currently situated at the top-left corner (cell (1, 1)(1,1)) and wants to reach the top-right corner (cell (N, 1)(N,1)). Determine the minimum number of moves in which the task can be accomplished.

Input Format
The first line will contain TT, the number of test cases. Then the test cases follow.
Each test case contains a single integer NN in a separate line.
Output Format
Output the minimum number of moves to get from the top-left cell to the top-right one.




"""

T = int(input())
for t in range(T):
    n = int(input())
    if n % 2 == 1:
        print(n - 1)
    else:
        print(n)
