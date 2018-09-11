"""
Simple graph implementation compatible with BokehGraph class.
"""
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError(f'Vertex {vertex} already exists')
    
    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            if edge not in self.vertices[vertex]:
                self.vertices[vertex].add(edge)
                self.vertices[edge].add(vertex)
            else:
                raise ValueError(f'Edge {edge} already exists with Vertex {vertex}')
        else:
            raise ValueError(f'Vertex {vertex} does not exist')

demo_g = Graph()
demo_g.add_vertex('0')
demo_g.add_vertex('1')
demo_g.add_vertex('2')
demo_g.add_vertex('3')
demo_g.add_edge('0', '1')
demo_g.add_edge('0', '3')
for vertex in demo_g.vertices:
    print(f'{vertex}: {demo_g.vertices[vertex]}')