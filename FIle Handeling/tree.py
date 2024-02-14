"""
#  Binary tree 
1) define class representing nodes in binary tree
    1) define left and right child as None and store value of current node in variable(data)
    2) check if root node is none or not
         - if none then return
         - if not then print current node




"""

# define class representing node in binary tree
class BinaryTreeNode:
    def __init__(self, data):
        # define left and right child as None and store value of node in data(var)
        self.data = data
        self.leftChild = None
        self.rightChild = None

def print_binarytree(root_node):
    # check if root node is none or not 
    if root_node == None:
        return
        
    # print the value of current node
    print("value of current node is :", root_node.data)

    print_binarytree(root.leftChild)
    print_binarytree(root.rightChild)


# create left and right child nodes
root_node.leftChild = BinaryTreeNode(20)
# create root node
root_node = BinaryTreeNode(50)
root_node.rightChild = BinaryTreeNode(30)

print_binarytree(root_node)




