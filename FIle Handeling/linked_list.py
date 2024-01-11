"""
define node class
    - which contain value and address of next variable(value, next)
    - store value of start node 
    - then define address(next) of next node.
    - when we create start node then address of next node is None.

define class linked list
    - define method 
    - initially firtst node in linked list is empty
    - define function to add node.
        - pass value to function
        - then add node using node class then check if list is empty or not
        - if list is empty then current node is first and only node in list.
        - if linked list is not empty then
            - add new node at end of list.
    
    - print linked list.
        - printing linked list we move next node until it reaches the end.
        - print value of current node 
        - move to next node of linked list
        - print if no value is found
    
"""

#define class name Node
class Node:

    # define mathod and pass parameter(value)
    def __init__(self, value):
        # store actual value of start_node
        self.value = value
        # define pointer to the next node
        # when start_node is created the next is None
        self.next = None


# define class name Linked_list
class Linked_list:
    # define method
    def __init__(self):
        # initially first node in linked_list is empty
        self.start_node = None

    # define function to add node 
    def Add_Node(self, value): 
        # add new node using Node class
        new_node = Node(value)
        # check if Linked_list is empty or not
        
        if self.start_node == None:
            # if yes then current node is the first and only node in list
            self.start_node = new_node
        # if Linked_list is not empty then
        else:
            # Traverse to the last node
            current_node = self.start_node
            while current_node.next != None:
                current_node = current_node.next
                # Add the new node at the end
            current_node.next = new_node
            # Update the end to be the new node
            self.end = new_node
            

    def print_linked_list(self):
       
        current_node = self.start_node
        # while printing linked list we move next node until it reaches the end.
        while current_node != None:
            # print value of current node 
            print(current_node.value, end=" ")
            # move to next node of linked list
            current_node = current_node.next
            # print if no value is found
        # print("list ended")
        print(None)
    

linked_list = Linked_list()
linked_list.Add_Node(2)
linked_list.Add_Node(3)
linked_list.Add_Node(5)
# [2]   [3]
# st    2nd
#

# print linked list
linked_list.print_linked_list()    