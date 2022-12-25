"""
Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently, Alice's score is AA and Bob's score is BB.

Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that will be further scored in the match before it ends.

Input Format
The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
The first and only line of each test case contains two space-separated integers AA and BB, as described in the problem statement.

Output Format
For each test case, output on a new line the minimum number of points that will be further scored in the match before it ends.


"""
# take input for no of testcases
T = int(input())
for t in range(T):
    # take input for each test case
    A, B = input().split()
    # convern each input into integer
    Alice_score = int(A)
    Bob_score = int(B)
    # substract player's score from initial score
    A_score = 7 - Alice_score
    B_score = 7 - Bob_score
    # calculating mininum number of points
    result = min(A_score, B_score)
    print(result)
