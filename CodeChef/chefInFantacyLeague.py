"""
Chef is going to start playing Fantasy Football League (FFL) this season. In FFL, each team consists of exactly 1515 players: 22 goalkeepers, 55 defenders, 55 midfielders and 33 forwards. Chef has already bought 1313 players; he is only missing one defender and one forward.

There are NN available players (numbered 11 through NN). For each valid ii, the ii-th player is either a defender or a forward and has a price P_iP 
i
​
 . The sum of prices of all players in a team must not exceed 100100 dollars and the players Chef bought already cost him SS dollars.

Can you help Chef determine if he can complete the team by buying one defender and one forward in such a way that he does not exceed the total price limit?

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains two space-separated integers NN and SS.
The second line contains NN space-separated integers P_1, P_2, \ldots, P_NP 
1
​
 ,P 
2
​
 ,…,P 
N
​
 .
The last line contains NN space-separated integers. For each valid ii, the ii-th of these integers is 00 if the ii-th player is a defender or 11 if the ii-th player is a forward.
Output
For each test case, print a single line containing the string "yes" if it is possible to build a complete team or "no" otherwise (without quotes).



"""
"""
1) check sum of cost of  two players(defender,forward) is less than 100
2) also check sum of two players(defender,forward) is 1.
3) if their sum is 1 count increases by 1
4) check count is equal to 0 or not.
5) if equal then team not buying one defender and one forward
6) if not then team buying one defender and one forward


"""
T = int(input())
for t in range(T):
    n, s = input().split()
    num_of_players = int(n)
    cost = int(s)
    price_of_player = list(map(int, input().split()))
    defender_or_forward_player = list(map(int, input().split()))
    count = 0
    for i in range(num_of_players):
        for j in range(i, num_of_players):
            if (
                price_of_player[i] + price_of_player[j] <= 100 - cost
                and defender_or_forward_player[i] + defender_or_forward_player[j] == 1
            ):
                count = count + 1
    if count == 0:
        print("no")
    else:
        print("yes")
