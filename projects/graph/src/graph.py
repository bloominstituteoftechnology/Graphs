"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        '''
        there should be a field vertices that contains a dictionary
        mapping vertex labels to edges.
        '''
        self.vertices = {}

    def add_vertex(self, value): # --> Takes in a value
        self.vertices[value] = set() # --> Creates a set with given value

    def add_edge(self, vertex_one, vertex_two): # --> vertex_one and vertex_two 
        # --> Need to check first if the vertex exists
        # --> To do this, we can use set-methods: get() to check if it is self.vertices
        if self.vertices.get(vertex_one) is not None and self.vertices.get(vertex_two) is not None:
            # --> Connect edges!
            self.vertices[vertex_one].add(vertex_two)
            self.vertices[vertex_two].add(vertex_one)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)