"""
Chef recently solved his first problem on CodeChef. The problem he solved has NN test cases. He gets a score for his submission according to the following rules:

If Chef’s code passes all the NN test cases, he gets 100100 points.

If Chef’s code does not pass all the test cases, but passes all the first M\;(M \lt N)M(M<N) test cases, he gets K\;(K \lt 100)K(K<100) points.

If the conditions 11 and 22 are not satisfied, Chef does not get any points (i.e his score remains at 00 points).

You are given a binary array A_1, A_2, \dots, A_NA 
1
​
 ,A 
2
​
 ,…,A 
N
​
  of length NN, where A_i = 1A 
i
​
 =1 denotes Chef's code passed the i^{th}i 
th
  test case, A_i = 0A 
i
​
 =0 denotes otherwise. You are also given the two integers M, KM,K. Can you find how many points does Chef get?

Input Format
First line will contain TT, number of testcases. Then the testcases follow.
The first line of each test case contains three space-separated integers N, M, KN,M,K.
The second line contains NN space-separated integer A_1, A_2,\dots, A_NA 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .
Output Format
For each testcase, output in a single line the score of Chef.


"""
"""
1) check numbers containing in list upto 1.
2) increse count by 1
3) also check count is equal to num of testcases to give 100 points
4) also check count is greater than first testcase given
5) to give points.
6) print result.

"""
T = int(input())
for t in range(T):
    n, m, k = input().split()
    num_of_testcases = int(n)
    first_testcases = int(m)
    point = int(k)
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i == 1:
            count += 1
        else:
            break
    if count == num_of_testcases:
        print("100")
    elif count >= first_testcases:
        print(point)
    else:
        print("0")
