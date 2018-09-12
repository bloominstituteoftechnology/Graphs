"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, v_id, x=None, y=None, value=None, color='white'):
        self.id = int(v_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, v_id):
        if vertex not in self.vertices:
            self.vertices[v_id] = Vertex(v_id)
        else:
            print('Please input a different vertex')
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            print("The edge could not be created")


def DFT(adjList, node_id, visited):
    visited.append(node_id)
    for child_node in adjList[node_id]:
        if child_node not in visited:
            DFT(adjList, child_node, visited)



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

DFT(graph.vertices, '0', [])