"""
Ram and Shyam are playing a game of Truth and Dare. In this game, Shyam will ask Ram to perform tasks of two types:

Truth task: Ram has to truthfully answer a question.
Dare task: Ram has to perform a given task.
Each task is described by an integer. (If a truth task and a dare task are described by the same integer, they are still different tasks.) You are given four lists of tasks:

�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
T 
r,1
​
 ,T 
r,2
​
 ,…,T 
r,t 
r
​
 
​
 : the truth tasks Ram can perform.
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
D 
r,1
​
 ,D 
r,2
​
 ,…,D 
r,d 
r
​
 
​
 : the dare tasks Ram can perform.
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
T 
s,1
​
 ,T 
s,2
​
 ,…,T 
s,t 
s
​
 
​
 : the truth tasks Shyam can ask Ram to perform.
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
D 
s,1
​
 ,D 
s,2
​
 ,…,D 
s,d 
s
​
 
​
 : the dare tasks Shyam can ask Ram to perform.
Note that the elements of these lists are not necessarily distinct, each task may be repeated any number of times in each list.

Shyam wins the game if he can find a task Ram cannot perform. Ram wins if he performs all tasks Shyam asks him to. Find the winner of the game.

Let's take an example where Ram can perform truth tasks 
3
3, 
2
2 and 
5
5 and dare tasks 
2
2 and 
100
100, and Shyam can give him truth tasks 
2
2 and 
3
3 and a dare task 
100
100. We can see that whichever truth or dare tasks Shyam asks Ram to perform, Ram can easily perform them, so he wins. However, if Shyam can give him dare tasks 
3
3 and 
100
100, then Ram will not be able to perform dare task 
3
3, so Shyam wins.

Input
The first line of the input contains a single integer 
�
T denoting the number of test cases. The description of 
�
T test cases follows.
The first line of each test case contains a single integer 
�
�
t 
r
​
 .
The second line contains 
�
�
t 
r
​
  space-separated integers 
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
T 
r,1
​
 ,T 
r,2
​
 ,…,T 
r,t 
r
​
 
​
 .
The third line contains a single integer 
�
�
d 
r
​
 .
The fourth line contains 
�
�
d 
r
​
  space-separated integers 
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
D 
r,1
​
 ,D 
r,2
​
 ,…,D 
r,d 
r
​
 
​
 .
The fifth line contains a single integer 
�
�
t 
s
​
 .
The sixth line contains 
�
�
t 
s
​
  space-separated integers 
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
T 
s,1
​
 ,T 
s,2
​
 ,…,T 
s,t 
s
​
 
​
 .
The seventh line contains a single integer 
�
�
d 
s
​
 .
The eighth line contains 
�
�
d 
s
​
  space-separated integers 
�
�
,
1
,
�
�
,
2
,
…
,
�
�
,
�
�
D 
s,1
​
 ,D 
s,2
​
 ,…,D 
s,d 
s
​
 
​
 .
Output
For each test case, print a single line containing the string "yes" if Ram wins the game or "no" otherwise.



"""

T = int(input())
for i in range(int(input())):
    A = input()
    t1 = list(map(int, input().split()))
    B = input()
    d1 = list(map(int, input().split()))

    C = input()
    t2 = list(map(int, input().split()))
    D = input()
    d2 = list(map(int, input().split()))

    flag = False

    # check truth task
    for i in t2:
        if i not in t1:
            flag = True
            break

    # check dare task
    if not flag:
        for i in d2:
            if i not in d1:
                flag = True
                break

    if flag:
        print("no")
    else:
        print("yes")
