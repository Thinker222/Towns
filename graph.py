
import math
import numpy as np

# Graph represent a series of nodes as a graph.
# Graph represent a series of nodes as a graph.
# The weights are represented by a dictionary. Each entry in the dictionary will be a node.
# (The actual weights for each node are stored in the node class to avoid a weird data structure in the weights dictionary)

class Graph:
    def __init__(self):
        self.__nodes = {}
    # Get a djiskstra table so actors can make decisions
    def getDjikstraTable(self, id):
        node = self.__nodes[id]
        dim = len(list(self.__nodes.keys())) - 1
        table = np.zeros(shape=(dim, dim))
        table = np.subtract(table, 1)
        unFinishedIds = list(self.__nodes.keys())
        unFinishedIds.remove(node.id)
        finishedIds = []
        while len(unFinishedIds) != 0:
            bestWeight = unFinishedIds[0]
        return None

    # Set a weight between two nodes. 
    # First you delete any existing weights between the two nodes. 
    # Then you set a weight going from one id to the other and vice versa. 
    # Remember, the graph is not directed
    def setWeight(self, id, id2, val, estimate=True):
        self.__nodes[id].weights[id2] = val
        self.__nodes[id2].weights[id] = val

        # Add a node to the weights dictionary

    def addNode(self, node):
        self.__nodes[node.id] = node

    # Remove a node from the weights dictionary, 
    # and remove all entries of that node in the other tables
    def removeNode(self, id):
        self.__nodes[id] = None

    # Get
    def getNode(self, id):
        return self.__nodes[id]

class Node:
    currentId = 0

    def __init__(self, x=0, y=0):
        self.id = Node.currentId
        self.coords = (x, y)
        # Key is a node id
        # Value is a weight
        self.weights = {}
        Node.currentId = Node.currentId + 1

    # Estimates the weight from another node 
    def estimateWeight(self, node):
        return math.sqrt(math.pow(self.coords[0] - node.coords[0], 2) + math.pow(self.coords[1] - node.coords[1], 2))

