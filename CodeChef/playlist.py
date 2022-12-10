"""
-Chef's playlist contains 3 songs named A, B and C, each of duration exactly XX minutes. Chef generally plays these 33 songs in loop, i.e, A \rightarrow B \rightarrow C \rightarrow A \rightarrow B \rightarrow C \rightarrow A \rightarrow \dotsA→B→C→A→B→C→A→…
-Chef went on a train journey of NN minutes and played his playlist on loop for the whole journey. How many times did he listen to the song CC completely?

Input Format
-The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
-Each test case consists of a single line of input, containing two space-separated integers N, XN,X.
Output Format
For each test case, output on a new line the number of times Chef listens to the song CC completely.


"""
T = int(input())
for t in range(T):
    n, x = input().split()
    num_n = int(n)
    num_x = int(x)
    total = num_n / (3 * num_x)
    print(int(total))
