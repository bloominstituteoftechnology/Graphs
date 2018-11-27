"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
    
    def add_vertex(self, vertex_id, vertices):
        self.vertices[vertex_id] = vertices(vertex_id)

    def add_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            self.vertices[vert1].edges.add(vert2)
            self.vertices[vert2].edges.add(vert1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, vert1, vert2):
        if vert1 in self.vertices:
            self.vertices[vert1].edges.add(vert2)
        else:
            raise IndexError("That vertex does not exist!")

# ## Part 1: Graph, Vertex, Edge Classes

# In the file `graph.py`, implement a `Graph` class that supports the API expected
# by `draw.py`. In particular, this means there should be a field `vertices` that
# contains a dictionary mapping vertex labels to edges. For example:

# ```python
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
# ```

# This represents a graph with four vertices and two total (bidirectional) edges.
# The vertex `'2'` has no edges, while `'0'` is connected to both `'1'` and `'3'`.

# You should also create `add_vertex` and `add_edge` methods that add the
# specified entities to the graph. To test your implementation, instantiate an
# empty graph and then try to run the following:

# ```python
# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
# ```

# You should see something like the first example. As a stretch goal, add checks
# to your graph to ensure that edges to nonexistent vertices are rejected.

# ```python
# # Continuing from previous example
# graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
# ```
    