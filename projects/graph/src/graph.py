"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    # def add_vertex_original(self, vertex):
    #     self.vertices[vertex] = set()

    # def add_edge_original(self, node_a, node_b):
    #     self.vertices[node_a].add(node_b)

    def add_vertex(self, vertex, edges=()):
        """
        Adds a new vertex, optionally with edges to other vertices.
        """
        if vertex in self.vertices:
            raise Exception('Error: this vertex already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """
        Add an edge(default: bidirectional) between two vertices.
        """
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

# def main():
graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('2', '3')
graph.add_edge('3', '1')

print(graph.vertices)

# if __name__ == '__main__':
#     main()
