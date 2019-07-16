
import math
import numpy as np
import sys
# Graph represent a series of nodes as a graph.
# Graph represent a series of nodes as a graph.
# The weights are represented by a dictionary. Each entry in the dictionary will be a node.
# (The actual weights for each node are stored in the node class to avoid a weird data structure in the weights dictionary)

class Graph:
    def __init__(self):
        self.__nodes = {}
    # Get a djiskstra table so actors can make decisions
    def getDjikstraTable(self, id):
        q = list(self.__nodes.keys())
        dist = {}
        prev = {}
        for node in self.__nodes:
            dist[node] = sys.maxsize
            prev[node] = sys.maxsize
        dist[id] = 0
        prev[id] = 0
        while len(q) != 0:
            remove = self.min_dist(q, dist)
            q.remove(remove)
            for weight in list(self.__nodes[remove].weights.keys()):
                if self.__nodes[remove].weights[weight] + dist[remove] < dist[weight] :
                    dist[weight] = self.__nodes[remove].weights[weight] + dist[remove]
                    prev[weight] = remove
        return prev

    def min_dist(self, q, dist):
        min = q[0]
        minDist = dist[min]

        for node in q:
            if dist[node] < minDist:
                minDist = dist[node]
                min = node
        return min

    # Set a weight between two nodes. 
    # First you delete any existing weights between the two nodes. 
    # Then you set a weight going from one id to the other and vice versa. 
    # Remember, the graph is not directed
    def setWeight(self, id, id2, val, estimate=True):
        self.__nodes[id].weights[id2] = val
        self.__nodes[id2].weights[id] = val


    def getWeight(self, id, id2):
        return  self.__nodes[id].weights[id2]
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

    def printweights(self):
        for node in self.__nodes:
            print(self.__nodes[node].weights)

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

