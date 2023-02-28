"""
Chef likes to play with cards a lot. Today, he's playing a game with three cards. Each card has a letter written on the top face and another (possibly identical) letter written on the bottom face. Chef can arbitrarily reorder the cards and/or flip any of the cards in any way he wishes (in particular, he can leave the cards as they were). He wants to do it in such a way that the letters on the top faces of the cards, read left to right, would spell out the name of his favorite friend Bob.

Determine whether it is possible for Chef to spell "bob" with these cards.

Input
The first line of the input contains a single integer 
�
T denoting the number of test cases. The description of 
�
T test cases follows.
The first line of each test case contains a single string with length 
3
3 denoting the characters written on the top faces of the first, second and third card.
The second line contains a single string with length 
3
3 denoting the characters written on the bottom faces of the first, second and third card.
Output
For each test case, print a single line containing the string "yes" (without quotes) if Chef can spell "bob" or "no" (without quotes) if he cannot.




"""
for i in range(int(input())):
    s1=input()
    s2=input()
    temp=False
    for i in range(len(s1)):
        if s1[i]=='o'or s2[i]=='o':
            count=0
            for j in range(len(s1)):
                if i!=j: