import random


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, label):
        self.vertices[label] = (Vertex(label))

    def show_graph(self):
        return self.vertices

    def add_edge(self, vertex, destination):
        vert = self.vertices[vertex]
        vert.edges.add(Edge(destination))

    def dft(self, node):
        visited = []
        stack = [node]
        while len(stack) > 0:
            vert = stack.pop(0)
            if vert not in visited:
                visited.append(vert)
                if vert.edges:
                    for edge in vert.edges:
                        stack.insert(0, self.vertices[edge.destination])
        return visited

    def dfs(self, node, target):
        visited = []
        stack = [node]
        while len(stack) > 0:
            vert = stack.pop(0)
            if vert not in visited:
                visited.append(vert)
                if vert.label == target:
                    return True
                if vert.edges:
                    for edge in vert.edges:
                        stack.insert(0, self.vertices[edge.destination])
        return False

    def bft(self, start_node):
        queue = []
        visited = []
        queue.insert(0, start_node)
        while len(queue) > 0:
            vert = queue.pop()
            if vert.label not in visited:
                visited.append(vert.label)
                if vert.edges:
                    for edge in vert.edges:
                        queue.insert(0, self.vertices[edge.destination])
        return visited

    def bfs(self, start_node, target):
        queue = []
        visited = []
        queue.insert(0, start_node)
        while len(queue) > 0:
            vert = queue.pop()
            print('vert', vert.label)
            if vert.label not in visited:
                visited.append(vert.label)
                if vert.edges:
                    for edge in vert.edges:
                        queue.insert(0, self.vertices[edge.destination])
            if target == vert.label:
                return True

        return False


class Vertex:
    def __init__(self, label, x=None, y=None):
        self.label = label
        self.edges = set()
        if x == None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y == None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y


class Edge:
    def __init__(self, destination):
        self.destination = destination
