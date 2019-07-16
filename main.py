from graph import Graph, Node
import math
import random

nodes = 3
g = Graph()
for i in range(nodes):
    g.addNode(Node(i,i))

for i in range(nodes):
    for j in range(nodes):
        g.setWeight(i, j , random.randrange(0,100))
g.printweights()
prev = g.getDjikstraTable(0)


print(prev)
