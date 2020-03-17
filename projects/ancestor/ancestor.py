from util import Stack, Queue  # These may come in handy


class GraphNode:
    def __init__(self, value):
        self.children = set()
        self.parents = set()
        self.value = value

    def addChild(self, node):
        self.children.add(node)
        node.parents.add(self)

    def __repr__(self):
        children = [x.value for x in self.children]
        parents = [x.value for x in self.parents]
        return f"Node: {self.value} Children: {children} parents: {parents}"
class Graph:
    def __init__(self):
        self.vertices = {}

    def addNode(self, value):
        if self.vertices.get(value, None) is None:
            self.vertices[value] = GraphNode(value)
        else:
            print("That node already exists!")

    def addEdge(self, value1, value2):
        if value1 not in self.vertices:
            self.addNode(value1)
        if value2 not in self.vertices:
            self.addNode(value2)
        node1 = self.vertices[value1]
        node2 = self.vertices[value2]
        node1.addChild(node2)

    def getNode(self, value):
        return self.vertices.get(value, None)

    def ancestorPaths(self, value):
        node = self.getNode(value)
        if node is None:
            return None
        s = Stack()
        s.push([value])

        ancestorPaths = []

        while s.size() > 0:
            path = s.pop()
            node = self.getNode(path[-1])
            for parentNode in node.parents:
                newPath = path.copy()
                newPath.append(parentNode.value)
                s.push(newPath)
                ancestorPaths.append(newPath)

        return ancestorPaths

    def __repr__(self):
        for value in self.vertices:
            print(self.vertices[value])

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        parentValue = pair[0]
        childValue = pair[1]
        g.addEdge(parentValue, childValue)

    ancestorPaths = g.ancestorPaths(starting_node)

    longestPath = []
    for path in ancestorPaths:
        if len(path) > len(longestPath):
            longestPath = path
        elif len(path) == len(longestPath):
            if path[-1] < longestPath[-1]:
                longestPath = path

    if len(longestPath) == 0:
        return -1
    else:
        return longestPath[-1]
