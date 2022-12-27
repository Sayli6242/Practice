"""
King loves to go on tours with his friends.

King has N cars that can seat 5 people each and M cars that can seat 7 people each. 
Determine the maximum number of people that can travel together in these cars.

Input Format
The first line of input contains a single integer T, the number of test cases.
The first and only line of each test case contains two space-separated integers N and M — the number of 5-seaters and 7-seaters, respectively.
Output Format
For each test case, output on a new line the maximum number of people that can travel together.



"""
# take no. of testcases as input
T = int(input())
# take values for each testcase in a loop
for t in range(T):
    # take values as input
    N, M = input().split()
    # convert them into integer
    num_of_5seater_car = int(N)
    num_0f_7seater_car = int(M)
    # calculate maximum number of people in cars
    num_of_people_in_5seater_car = num_of_5seater_car * 5
    num_of_people_in_7seater_car = num_0f_7seater_car * 7
    maximum_num_of_people = num_of_people_in_7seater_car + num_of_people_in_5seater_car
    # print result
    print(maximum_num_of_people)
