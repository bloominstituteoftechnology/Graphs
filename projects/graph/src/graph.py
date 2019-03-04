

"""Simple graph implementation"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_id):
        """Creates a new vertex with no edges."""
        self.vertices[vertex_id] = set()

    def add_edge(self, source_id, end_id):
        """Connects two vertices along an edge, bidirectionally."""
        # Ensure endpoints are valid vertices on the graph
        if not (source_id in self.vertices):
            raise Exception('Invalid vertex id for edge source.')
        if not (end_id in self.vertices):
            raise Exception('Invalid vertex id for edge destination.')
        # Connect vertices symmetrically
        vertex_source = self.vertices[source_id]
        vertex_source.add(end_id)
        vertex_end = self.vertices[end_id]
        vertex_end.add(source_id)
