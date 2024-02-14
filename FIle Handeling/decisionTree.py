"""
1) make class of DecisionTreeNode  to define decision node and decision tree with attributes 
    - condition_node
    - leftChild_node
    - rightChild_node
    - decision 
2)  define function to make_project_decision based of given requirement.
    - start with root_node that is check requirement of budget condition.
    - define nodes to make other decision points such as
        - project scope
        - team availability
        - project complexity
    - connect nodes based on decision making flow
        - if budget condition gets true 
            - continue
        - if budget condition gets false
            - delay project
    - then traverse the tree
        - start from root_node
        - get user_input for decision node
    - check conditions after getting input
        - if condition is true then
            - go to leftchild_node 
        - if condition is false then
            - go to rightchild_node
        - repeat untill decision node getting final decision
    - return decision
"""

# make class of DecisionTreeNode  to define decision node and decision tree with attributes 
class DecisionTreeNode:
    def __init__(self, condition, leftChild_node = None, rightChild_node = None, decision = None, input = [], title = ''):
        self.condition = condition   # > < >= <= == 
        self.leftChild_node = leftChild_node 
        self.rightChild_node = rightChild_node
        self.decision = decision # yes,no
        # input = []  (contain 1 or 2 value )
        self.input = input
        self.title = title

#  define function to make_project_decision based of given requirement.
def make_project_decision():

    # start with root_node that is check requirement of budget condition.
        budget= 10000
        actual_budget = 10000000
        project_scope = True
        team_availability = True



        root_node = DecisionTreeNode('>', None , None, 'yes', [budget, actual_budget],'budget_decision')
        project_scope_node = DecisionTreeNode('boolean',None,None,'yes', [project_scope],'project_scope')
        team_availability_node = DecisionTreeNode('boolean',None,None,'no', [team_availability],'team_availability')

        root_node.leftChild_node = project_scope_node
        root_node.rightChild_node = team_availability_node


        
        current_node = root_node


        
        # check if the node has left or right 
        # if node does not have left,right node then print current node
        # check condition and make left or right current depending on condition 
        #  
        while True:
            if current_node.leftChild_node == None and current_node.rightChild_node == None :
                print(current_node.decision)
                break

            result =  evaluate_conditions(current_node.condition, current_node.input ) 
            if result == True:
                current_node = current_node.leftChild_node
            else:
                current_node = current_node.rightChild_node
      
    
            
 # start traversing the decision tree from root node
def evaluate_conditions(condition , input):
    # make a project decision and print the result
    
    if condition == '>':
        return input[0] > input[1]
    
    elif condition == 'boolean':
        # Check if the project scope is well-defined
        return input[0]
        

decision = make_project_decision()
# print('decision: ', decision)

