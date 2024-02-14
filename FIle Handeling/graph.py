'''
1) make a class name Graph and define empty dict to store
    - node 
    - edge
2) define function add_node to add nodes

3) define function add_edge to add edges
    - add edge in between two nodes                      ""  G(0,N)""
4) print graph

'''
# make a class name graph with attributes node and edge
class Graph:
    def __init__(self):
        # define empty dict to store graph and their edges and nodes
        self.graph = {} 
    

    def Add_Node(self, node):
        """
    define fuction for add nodes

        Args:
            node (_type_): _description_
        """
        # define empty list to store node
        self.graph[node] = []


    def add_edge(self, node1, node2):
        """add edge between two nodes

        Args:
            node1 (int): node of graph
            node2 (int): node of graph
        """
        # add edge between two nodes
        # add node2 into node1 connected node list
        self.graph[node1].append(node2)
        # add node1 into node2 connected node list
        self.graph[node2].append(node1)

    def print_graph(self) :
        for node, edge in self.graph.items():
            print(f"Node {node} is connected to: {edge}")

# example:

make_graph = Graph()

make_graph.Add_Node(2)
make_graph.Add_Node(3)
make_graph.Add_Node(5)
make_graph.Add_Node(7)

make_graph.Add_Edge(2,3)
make_graph.Add_Edge(3,7)


make_graph.print_graph()


