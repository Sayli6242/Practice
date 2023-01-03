"""
RJ is a very curious observer. On the first day of every month, he tries to figure out, for each of the seven days of the week, how many times that day occurs in the current month.

RJ got confused so badly doing this that he asks for your help! He asks several queries; in each query, 
he gives you the number of days in the current month and which day of the week is on the 1st of the current month.

For each query, you should tell him how many times each day of the week occurs.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains an integer W and a string S, separated by a space.
W denotes the number of days in the current month.
S is one of the strings "mon", "tues", "wed", "thurs", "fri", "sat" or "sun", denoting the day of the week on the 1st of the current month.
Output
For each query, print seven space-separated integers denoting the number of occurrences of Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

"""
"""
1) make list of days in week
2) make count of each days appear in a week
3) 
"""
T = int(input())
for t in range(T):
    W, S = input().split()
    days_of_month = int(W)
    lst = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    X = W // 28
    print(X)
    count = 0
    for i in lst:
        for i in range(days_of_month):
            count = count + 1

        print(count)
