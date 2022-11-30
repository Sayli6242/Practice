"""
- Chef appeared for a placement test.

- There is a problem worth XX points. Chef finds out that the problem has exactly 1010 test cases. 
- It is known that each test case is worth the same number of points.

- Chef passes NN test cases among them. Determine the score Chef will get.

NOTE: See sample explanation for more clarity.

Input Format
- First line will contain TT, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers XX and NN, the total points for the problem and the number of test cases which pass for Chef's solution.


"""
T = int(input())
for t in range(T):
    X, N = input().split()
    a = int(int(X) / 10)
    b = a * int(N)
    print(b)
