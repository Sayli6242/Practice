"""
Motu and Tomu are very good friends who are always looking for new games to play against each other and ways to win these games. One day, they decided to play a new type of game with the following rules:

The game is played on a sequence 
�
0
,
�
1
,
…
,
�
�
−
1
A 
0
​
 ,A 
1
​
 ,…,A 
N−1
​
 .
The players alternate turns; Motu plays first, since he's earlier in lexicographical order.
Each player has a score. The initial scores of both players are 
0
0.
On his turn, the current player has to pick the element of 
�
A with the lowest index, add its value to his score and delete that element from the sequence 
�
A.
At the end of the game (when 
�
A is empty), Tomu wins if he has strictly greater score than Motu. Otherwise, Motu wins the game.
In other words, Motu starts by selecting 
�
0
A 
0
​
 , adding it to his score and then deleting it; then, Tomu selects 
�
1
A 
1
​
 , adds its value to his score and deletes it, and so on.

Motu and Tomu already chose a sequence 
�
A for this game. However, since Tomu plays second, he is given a different advantage: before the game, he is allowed to perform at most 
�
K swaps in 
�
A; afterwards, the two friends are going to play the game on this modified sequence.

Now, Tomu wants you to determine if it is possible to perform up to 
�
K swaps in such a way that he can win this game.
"""


T = int(input())
for i in range(T):
    score = 0
    N, K = input().split()

    num_of_elements = int(N)
    max_swaps_of_Tomu = int(K)
    list_of_elements =list(map(int, input().split()))
    if max_swaps_of_Tomu > 0:
        max_element_in_list = max(list_of_elements)
        temp = list_of_elements[2]
        list_of_elements[2] = list_of_elements[3] 
        list_of_elements[3] = temp
        Tomus_score = list_of_elements[1::2] 
        Motus_core = list_of_elements[0::2]
        if Tomus_score > Motus_core:
            print('YES')
    else:
        print('NO')
        
        
        
        
        
    