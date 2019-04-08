"""
Simple graph implementation
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, num):
        if num not in self.vertices:
            self.vertices[num] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


    def addDoubleEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)
            self.vertices[v1].add(v2)

    def bft(self, node):
        q = Queue()
        visited = set()
        q.enqueue(node)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)

                for nextVertice in self.vertices:
                    q.enqueue(nextVertice)


graph = Graph()
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')

graph.add_directed_edge('1', '2')
graph.add_directed_edge('1', '3')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '1')
graph.add_directed_edge('3', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('5', '6')



graph.bft('1')

