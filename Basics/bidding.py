"""
-Alice, Bob and Charlie are bidding for an artifact at an auction.
-Alice bids A rupees, Bob bids B rupees, and Charlie bids C rupees (where A, B, and C are distinct).
-According to the rules of the auction, the person who bids the highest amount will win the auction.
-Determine who will win the auction.

Input Format
-The first line contains a single integer T — the number of test cases. Then the test cases follow.
-The first and only line of each test case contains three integers A, B, and C, — the amount bid by Alice, Bob, and Charlie respectively.
Output Format
-For each test case, output who (out of Alice, Bob, and Charlie) will win the auction.

"""
T = int(input())
for t in range(T):
    a, b, c = input().split()
    num_a = int(a)
    num_b = int(b)
    num_c = int(c)
    dict = {"alice": num_a, "bob": num_b, "charlie": num_c}
    v = list(dict.values())
    k = list(dict.keys())
    print(k[v.index(max(v))])
