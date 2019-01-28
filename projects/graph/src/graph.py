from queue import Queue
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex:
            self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)

    def bft(self, starting_node):
        q = Queue()
        visited = set()
        visited.add(starting_node)
        q.Enqueue(starting_node)
        while q.len() > 0:
            node = q.dequeue()
            if node not in visited:
                visited.append(node)
                for i in self.vertices[node]:
                    q.enqueue(i)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1') 
graph.add_edge('0', '3')
print(graph.vertices)
