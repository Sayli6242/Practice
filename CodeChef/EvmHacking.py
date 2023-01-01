"""
There are three cities and thus three EVMs. An insider told Chef that his party got A,B,C votes respectively in these three cities according to the EVMs. 
Also, the total number of votes cast are P, Q, R respectively for the three cities.

Chef, being the party leader, can hack at most one EVM so that his party wins. On hacking a particular EVM all the votes cast in that EVM are counted in favor of Chef's party.

A party must secure strictly more than half of the total number of votes cast in order to be considered the winner. Can Chef achieve his objective of winning by hacking at most one EVM?

Input Format
The first line of input contains an integer TT, denoting the number of test cases. The description of TT test cases follows.
Each test case consists of a single line of input, containing six space-separated integers — in order, A, B, C, P, Q, R
Output Format
For each test case, output in a single line the answer — "YES", if Chef can win the election after hacking at most one EVM and "NO" if not.

"""
"""
1) calculate total votes of all cities of two parties.
2) compare chefs_party votes to all all Evms votes.
3) print result.
"""
T = int(input())
for t in range(T):
    A, B, C, P, Q, R = list(map(int, input().split()))
    Total_votes_of_cities = (P + Q + R) / 2
    if (
        (A + B + R) > Total_votes_of_cities
        or (B + C + P) > Total_votes_of_cities
        or (C + A + Q) > Total_votes_of_cities
    ):
        print("yes")
    else:
        print("no")
