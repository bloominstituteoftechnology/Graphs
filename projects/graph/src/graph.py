#!/usr/bin/python
import random
"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label):
        self.label = label
        self.edges = set()
        self.pos = pos
        self.edges = set()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """Add anew vertex, optionally with edges to other vehicles."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional = True):
        """Add a edge (default bidrectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')    
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

def main(): #instantiate your graph
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    if __name__ == '_main_':
        main()

def bfs(self, start):
    random_color = '#' + \
        ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    queue = []
    found = []
    queue.append(start)
    found.append(start)

    start.color = random_color

    while (len(queue) > 0):
        v = queue[0]
        for edge in v.edges:
            if edge not in found:
                found.append(edge)
                queue.append(edge)
                edge.color = random_color

        queue.pop(0)  # TODo look at collections.dequeue
    return found

# Get the connected components
def get_connected_components(self):
    # Connected Components
    # Go to the next unfound vertex in graph vertices and call BFS on it
    # Go to step 1 until we get to the end of the array(loop)

    searched = []

    for index, vertex in self.vertices.items():
        if vertex not in searched:
            searched.append(self.bfs(vertex))

    return searched

