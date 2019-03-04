"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # initialize verticies to an empty dictionary
        self.verticies = {}
    # add_vertex method to create node or vertex and initialize the vertex id to an empty set()

    def add_vertex(self, vertex_id):
        # key of the specific vertex will be vertex_id, while the edges will be initialized to the empty set
        self.verticies[vertex_id] = set()
    # add_directed_edge method to create edges or connections from vertex1 to vertex2, one way

    def add_directed_edge(self, v1, v2):
        # check to see if v1 and v2 are both valid values or actual verticies in the graph
        if v1 in self.verticies and v2 in self.verticies:
            # if valid verticies, from v1 add v2 to the set, only one way or directed
            self.verticies[v1].add(v2)
        # if the provided v1 or v2 does not exist raise error
        else:
            raise IndexError("That vertex does not exist")
    # add_undirected_edge method to create edges or connections from vertex1 to vertex2, both ways

    def add_undirected_edge(self, v1, v2):
        # check to see if v1 and v2 are both valid values or actual verticies in the graph
        if v1 in self.verticies and v2 in self.verticies:
            # if valid verticies, from v1 add v2 to the set
            self.verticies[v1].add(v2)
            # then add from v2 to v1 to the set, this allows the connection both ways
            self.verticies[v2].add(v1)
        # if the provided v1 or v2 does not exist raise error
        else:
            raise IndexError("That vertex does not exist")


# test graph
graph = Graph()  # instantiate graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_directed_edge('0', '1')
graph.add_directed_edge('0', '3')
print(graph.verticies)
# test for non existing vertex
graph.add_directed_edge('0', '4')
print(graph.verticies)
