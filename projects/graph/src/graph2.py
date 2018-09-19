"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color='white'):
        self.id=int(vertex_id)
        self.x = x
        self.y = y
        self.value=value
        self.color=color
        self.edges=set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise Exception('That vertex does not exist.')
    def add__directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise Exception('That vertex does not exist.')

def dft(adjList, node_id, visited):
    print(node_id)
    visited.append(node_id)
    for el in adjList[node_id]:
        if el not in visited:
            dft(adjList, el, visited)

def bft(aList, node_id):
    queue = []
    queue.append(node_id)
    visited = []
    while len(frontier) > 0:
        n = frontier.pop()
        if n not in visited:
            print(n)
            visited.append(n)
            for el in aList[n]:
                queue.append(el)

