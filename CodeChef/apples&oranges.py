"""
-Bob has X rupees and goes to a market. The cost of apples is Rs.A per kg and the cost of oranges is Rs.B per kg.
-Determine whether he can buy at least 1 kg each of apples and oranges.

Input Format
-The first line of input will contain an integer X, the amount of money Bob has.
-The second line of input contains two space-separated integers A and B, the cost per kg of apples and oranges respectively.
Output Format
-Print a single line containing Yes if Bob can buy the fruits and No otherwise.



"""
x = int(input())
a,b = input().split()
num_a = int(a)
num_b = int(b)
total = num_a + num_b
if total <= x:
    print('Yes')
else:
    print('No')