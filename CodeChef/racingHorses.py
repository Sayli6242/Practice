"""
Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. 
He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. 
This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.

There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. 
The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be able to host a very interesting race. 
Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

Input:
First line of the input file contains a single integer T, the number of test cases.
Every test case starts with a line containing the integer N.
The next line contains N space separated integers where the i-th integer is S[i].

Output:
For each test case, output a single line containing the minimum difference that is possible.
"""
"""
1) sort the list
2) substract one from other to obtain difference between them
3) store their obtain result in new list
4) track minimum number from new list 
5) print result 
"""
T = int(input())
for t in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    lst = []
    for i in S:
        for j in S:
            if i < j:
                total = j - i
                lst.append(total)
                break
    print(min(lst))
