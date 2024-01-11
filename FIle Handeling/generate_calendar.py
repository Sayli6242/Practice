"""
Write a program to generate a simple text-based calendar for a specified month and year.

"""

#define class name Node
class Node:

    # define method and pass parameter(value)
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
            # if yes then current node is the first and only node in the list
            self.start_node = new_node
        # if Linked_list is not empty then
        else:
            # then add new node to beginning 
            new_node.next = self.start_node
            # next node is assigned to new_node
            self.start_node = new_node

    def Remove_Node(self, value):
        pass

# Example usage
linked_list = Linked_list()
linked_list.Add_Node(2)
linked_list.Add_Node(3)
linked_list.Add_Node(5)

# Print the linked list
current_node = linked_list.start_node
while current_node:
    print(current_node.value, end=" ")
    current_node = current_node.next












# Method to remove at given index
def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")



