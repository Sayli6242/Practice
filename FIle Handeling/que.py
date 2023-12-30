"""
"first in firt out principle"
1) fix sized list
2) check list is empty or not
        - if empty then continue
        - if not then quit program
3) enqueue operation
        - add element to list at list[0] index
4) dequeue operation
        - remove element from list at list[0] index


""" 
n = 10
queue = []

def enqueue_operation():
    element =  int(input("enter element: "))
    if len(queue) == n:
        print("queue is full")
    else: 
        queue.append(element)
        print(queue)
    
def dequeue_operation():   
    if not queue:
        print("queue is empty")
    else:
        removed_element = queue.pop(0)
        print("removed element is: ",removed_element)
        print(queue)
    
while True:
    choice = int(input("enter operation you want to perform: \n1) enqueue(add element) \n2) dequeue(remove element) \n3) quit \n"))
    if choice == 1:
        enqueue_operation()
    elif choice == 2:
        dequeue_operation()
    elif choice == 3:
        break
    
    else:
        print("enter valid choice")