"""
Finally, a COVID vaccine is out on the market and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible.
There are a total of NN people with ages a_1, a_2,....., a_N.
There is only one hospital where vaccination is done and it is only possible to vaccinate up to DD people per day.
Anyone whose age is ≥80 or ≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk.
Find the smallest number of days needed to vaccinate everyone.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and D.
The second line contains NN space-separated integers a_1, a_2,...., a_Na 
1
​
 ,a 
2
​
 ,…,a 
N
​
 .
Output
For each test case, print a single line containing one integer ― the smallest required number of days.

"""
"""
1) take input for total num of total_num_of_people , vaccinated_people_per_day
2) check each persons age and add it to a proper list(risk, non risk)
3) 
"""


from math import ceil

T = int(input())
for t in range(T):
    # take input for total num of people, vaccinated people per day
    N, D = input().split()
    total_num_of_people = int(N)
    vaccinated_people_per_day = int(D)
    lst = list(map(int, input().split()))
    count_risk = 0
    count_non_risk = 0
    risk = []
    non_risk = []
    # check each person age and add it to a proper list(risk, non_isk)
    for i in lst:
        if i >= 80 or i <= 9:
            risk.append(i)
            count_risk += 1
        else:
            non_risk.append(i)
            count_non_risk += 1
    # calculate total num of vaccination days by using ceil division
    num_of_day_for_total_vaccination = (
        ceil(count_risk / vaccinated_people_per_day)
    ) + (ceil(count_non_risk / vaccinated_people_per_day))
    print(num_of_day_for_total_vaccination)
