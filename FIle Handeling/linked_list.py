"""
define node class
    - value 
    - next
define class linked list
    - start node 
    - end node
    - define function to add node 
        - check node is empty or not 
            - if yes then assign value
            - if not then  assing next to new_value
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
            self.start_node = node
        # if Linked_list is not empty then
        else:
            # then add new node to beginning 
            new_node.next = self.start_node
            # next node is assigned to new_node
            self.start_node = new_node

    def Remove_Node(self, value):
        pass


linked_list = Linked_list()
linked_list.Add_Node(2)
linked_list.Add_Node(3)

# [2]   [3]
# st