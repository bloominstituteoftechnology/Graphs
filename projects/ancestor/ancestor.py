from util import Stack, Queue  # These may come in handy


class GraphNode:
    def __init__(self, value):
        self.children = set()
        self.parent = None
        self.value = value

    def addChild(self, node):
        self.children.add(node)
        node.parent = self
class Graph:
    def __init__(self):
        self.vertices = {}

    def addNode(self, value):
        if self.vertices.get(value, None) is None:
            self.vertices[value] = GraphNode(value)
        else:
            print("That node already exists!")

    def addEdge(self, value1, value2):
        if value1 in self.vertices and value2 in self.vertices:
            node1 = self.vertices[value1]
            node2 = self.vertices[value2]
            node1.addChild(node2)
        else:
            raise IndexError("That vertex doesn't exist!")

    def getNode(self, value):
        return self.vertices.get(value, None)

def earliest_ancestor(ancestors, starting_node):
    pass
