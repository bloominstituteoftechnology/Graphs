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
        self.verticies = {}

    def add_vertex(self, value): # --> Takes in a value
        self.verticies[value] = set() # --> Creates a set with given value

    def add_edge(self, vertex_one, vertex_two):
        # --> Need to check first if the vertex exists
        # --> To do this, we can use set-methods: get() to check if it is self.verticies
        if self.vertices.get(vertex_one) not None and self.verticies.get(vertex_two) not None:
            # --> Connect edges!
