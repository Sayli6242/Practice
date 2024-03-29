"""
Little chief has his own restaurant in the city. There are N workers there. 
Each worker has his own salary. The salary of the i-th worker equals to Wi (i = 1, 2, ..., N).
Once, chief decided to equalize all workers, that is, he wants to make salaries of all workers to be equal. 
But for this goal he can use only one operation: choose some worker and increase by 1 salary of each worker, 
except the salary of the chosen worker. 
In other words, the chosen worker is the loser, who will be the only worker, 
whose salary will be not increased during this particular operation. 
But loser-worker can be different for different operations, of course. 
Chief can use this operation as many times as he wants. 
But he is a busy man. 
That's why he wants to minimize the total number of operations needed to equalize all workers. 
Your task is to find this number.

"""
T= int(input())
for t in range(T):
        
    N = int(input())
    W = list(map(int,input().split()))
    for i in range(W):
        print()