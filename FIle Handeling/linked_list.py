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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self):
        self.start_node = None

    def Add_Node(self, value):
        new_node = Node(value)
        if self.start_node == None:
            self.start_node = node
        else:
            new_value.next = self.value
            self.value = new_value



