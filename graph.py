
# Graph represent a series of nodes as a graph. 
# The weights are represented by a dictionary. Each entry in the dictionary will be a node.
# (The actual weights for each node are stored in the node class to avoid a weird data structure in the weights dictionary)

class Graph: 
    def __init__(self):
        self.__weights = {}
    
    # Get a djiskstra table so actors can make decisions
    def getDjikstraTable(self):
        return None

    # Set a weight between two nodes. 
    # First you delete any existing weights between the two nodes. 
    # Then you set a weight going from one id to the other and vice versa. 
    # Remember, the graph is not directed
    def setWeight(self, id1, id2):
        return None 
    
    # Add a node to the weights dictionary
    def addNode(self, node):
        return None

    # Remove a node from the weights dictionary, 
    # and remove all entries of that node in the other tables
    def removeNode(self, id):
        return None

    # Get
    def getNode(self, id):
        return None 


# Node represents a single nod in a graph
class Node:
    currentId = 0 
    def __init__(self, x = 0, y = 0):
        self.id = Node.currentId
        self.coords = (x, y)
        self.weights = []
        Node.currentId = Node.currentId + 1

    # Estimates the weight from another node 
    def estimateWeight(self, node):
        return None

