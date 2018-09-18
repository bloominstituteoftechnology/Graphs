"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f"{self.vertices}"

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception('Error: That vertex already exists')
        else:
            self.vertices[vertex] = set()

    def add_edge(self, start, end):
        if start not in self.vertices:
            raise Exception('Error: Start vertex not found')
        if end not in self.vertices:
            raise Exception('Error: End vertex not found')
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)

    def add_directed_edge(self, start, end):
        if start not in self.vertices:
            raise Exception('Error: Start vertex not found')
        if end not in self.vertices:
            raise Exception('Error: End vertex not found')
        else:
            self.vertices[start].add(end)

def dft(adjList, node_id):
    print(node_id)
    for child_node in adjList[node_id]:
        dft(adjList, child_node)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_directed_edge('0', '1')
graph.add_directed_edge('0', '2')
graph.add_directed_edge('2', '3')

dft(graph.vertices, '0')
