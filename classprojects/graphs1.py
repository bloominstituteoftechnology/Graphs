# Graphs
----
#nodes connected by edges
#vertexes
#vertices
#verts

#Breadth - first - traversal

class Node:
    def __init__(self, value):
        self.neighbors = []
    def __repr__(self):
        return f'NODE({repr(self.value)})'

def bft(self, node):
    to_vist = Queue()

    visted = set()

    to_vist.enqu


a = Node('A')
b = Node('B')
c = Node('C')


a.neighbors.append(b)
a.neighbors.append(c)

print(a.neighbors)