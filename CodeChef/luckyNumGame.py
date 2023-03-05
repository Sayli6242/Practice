"""
Bob and Alice are playing a game with the following rules:

Initially, they have an integer sequence 
�
1
,
�
2
,
…
,
�
�
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ; in addition, Bob has a lucky number 
�
a and Alice has a lucky number 
�
b.
The players alternate turns. In each turn, the current player must remove a non-zero number of elements from the sequence; each removed element should be a multiple of the lucky number of this player.
If it is impossible to remove any elements, the current player loses the game.
It is clear that one player wins the game after a finite number of turns. Find the winner of the game if Bob plays first and both Bob and Alice play optimally.

Input
The first line of the input contains a single integer 
�
T denoting the number of test cases. The description of 
�
T test cases follows.
The first line of each test case contains three space-separated integers 
�
N, 
�
a and 
�
b.
The second line contains 
�
N space-separated integers 
�
1
,
�
2
,
…
,
�
�
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .
Output
For each test case, print a single line containing the string "ALICE" if the winner is Alice or "BOB" if the winner is Bob (without quotes).




"""
T = int(input())
for t in range(T):
    N, a, b = input().split()
    A = list(map(int,input().split()))
    no_of_integers = int(N)
    Bob_lucky_no = int(a)
    Alice_lucky_no = int(b)
    bob_moves = 0
    alice_moves = 0
    for i in A:
        if i % Bob_lucky_no == 0:
            bob_moves = bob_moves + 1
            
        elif i % Alice_lucky_no == 0:
            alice_moves = alice_moves + 1
            
    if bob_moves > alice_moves:
        print('Bob')
    else:
        print('Alice')      