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
    def __init__(self, conditions, leftChild_node = None, rightChild_node = None, decision = None):
        self.conditions = conditions
        self.leftChild_node = leftChild_node
        self.rightChild_node = rightChild_node
        self.decision = decision
#  define function to make_project_decision based of given requirement.
def make_project_decision(project_data):
    # start with root_node that is chek requirement of budget condition.
        root_node = DecisionTreeNode('budget >= 1000000')
    # define nodes to make  other decision points such as project_scope, team_availability, project_complexity
        project_scope_node = DecisionTreeNode('project scope well defined')
        team_availability_node = DecisionTreeNode('team availability high')
        project_complexity_node = DecisionTreeNode('project complexity low')

    # connect nodes based on decision making flow
        root_node.leftChild_node = project_scope_node
        root_node.rightChild_node = DecisionTreeNode('delay project', decision = 'delay')

        project_scope_node.leftChild_node = team_availability_node
        project_scope_node.rightChild_node = DecisionTreeNode('delay project', decision = 'delay')
    
        team_availability_node.leftChild_node = project_complexity_node
        team_availability_node.rightChild_node = DecisionTreeNode('delay project', decision = 'delay')


    # start traversing the decision tree from root node

        current_node = root_node
        while current_node.decision == None:
            print(current_node.conditions)
            # get user input for decision node
            decision = input("enter input.enter 'yes' or 'no': ")
            # check condisions after getting input
            if decision == 'yes':
                current_node = current_node.leftChild_node
            elif decision == 'no':
                current_node = current_node.rightChild_node
            
            else:
                print("invalid input. enter 'yes' or 'no': ")
            
        # return final decision
        return current_node.decision

# given project data
project_data = {'budget': 100000,'project_scope': 'well_defined', 'team_availability':'high', 'project_complexity':'low'}

# make a project decision and print the result
decision = make_project_decision(project_data)
print('decision: ', decision)