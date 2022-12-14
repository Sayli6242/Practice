"""
-Chef got his dream seat in F1 and secured a 3^{rd}
-place in his debut race. He now wants to know the time gap between him and the winner of the race.
-You are his chief engineer and you only know the time gap between Chef and the runner up of the race,
-given as A seconds, and the time gap between the runner up and the winner of the race, given as B seconds.
-Please calculate and inform Chef about the time gap between him and the winner of the race.

Input Format
-The first line of input will contain a single integer T, denoting the number of test cases.
-Each test case consists of a single line of input containing two space-separated integers A and B denoting the
-time gap between Chef and the runner up and the time gap between the runner up and the winner respectively.
Output Format
-For each test case, output the time gap between Chef and the winner of the race.

"""
T = int(input())
for t in range(T):
    a, b = input().split()
    num_a = int(a)
    num_b = int(b)
    time_gap = num_a + num_b
    print(time_gap)
