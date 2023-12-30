"""
"last in first out principle" 

 1) take an empty list
 2) add element 
 3) check list is empty or not 
        - if empty then end program
        - if not then continue
 4) remove element

"""
n = 5
stack =[ ]

def push_elements():
    if len(stack)== n:
        print("stack is full")
    else:
        element = input("enter element: ")
        stack.append(element)
        print(stack)


def pop_element():
    if not stack:
        print("stack is empty")
    else:
        poped_element = stack.pop()
        print("removed element: ",poped_element)
        print(stack)



while True:
    options = int(input("enter operation you want to perform: \n1) push_element \n2) pop_element \n3) quit \n"))
    if options == 1:
        push_elements()
    elif options == 2:
        pop_element()
    elif options == 3:
        break
    else:
        print("enter correct options")
