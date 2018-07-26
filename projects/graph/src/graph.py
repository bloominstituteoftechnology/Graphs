"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """
    Represent a single vertex that is aware of all existing verrtices
    """
    all_vertices = set()
    all_vertix_labels = set()

    def __init__(self, label):
        if label in Vertex.all_vertix_labels:
            raise Exception('Error: vertex {} already exists'.format(label))

        self.label = label
        self.visited = False
        self.component = None
        Vertex.all_vertices.add(self)
        Vertex.all_vertix_labels.add(self.label)

    def __repr__(self):
        return str(self.label)

    def _get_obj_instance(label):
        """
        Return Vertex object instance of string representation
        """
        for vertex in Vertex.all_vertices:
            if vertex.label == label:
                return vertex
        return None


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}
        self.vertex_obj_map = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """
        Create Vertex instances and add to graph
        """
        vertex_edges = set()
        for edge in edges:
            if edge not in self.vertex_obj_map.keys():
                raise Exception(
                    'Error: cannot create edge to nonexistent vertex')
            vertex_edges.add(self.vertex_obj_map[edge])

        vertex = Vertex(vertex)
        self.vertex_obj_map[vertex.label] = vertex
        self.vertices[vertex.label] = vertex_edges

    def add_edge(self, start, end, bidirectional=True):
        """
        Add edge to existing vertex
        """
        if start not in self.vertex_obj_map.keys():
            raise Exception('Error: vertex {} does not exist'.format(start))
        if end not in self.vertex_obj_map.keys():
            raise Exception('Error: vertex {} does not exist'.format(end))

        start_vertex = self.vertex_obj_map[start]
        end_vertex = self.vertex_obj_map[end]

        self.vertices[start_vertex.label].add(end_vertex)
        if bidirectional:
            self.vertices[end_vertex.label].add(start_vertex)

    def search(self, start, algorithm='bfs', reset=True):
        """
        Search graph with breadth first algorithm or depth first search
        """
        quack = []
        trail = []
        start_vertex = self.vertex_obj_map[start]
        pop_index = 0 if algorithm == 'bfs' else -1
        quack.append(start_vertex)

        if reset:
            for vertex in self.vertex_obj_map.values():
                vertex.visited = False

        while quack:
            current = quack.pop(pop_index)
            if not current.visited:
                for vertex in self.vertices[current.label]:
                    if not vertex.visited:
                        quack.append(vertex)
                current.visited = True
                current.component = self.components
                trail.append(current.label)

        return trail

    def find_connected_components(self):
        unvisited = self._find_unvisited_vertices()
        while unvisited:
            self.components += 1
            self.search(unvisited[0], 'bfs', False)
            unvisited = self._find_unvisited_vertices()

    def _find_unvisited_vertices(self):
        """
        Return a list of all vertices that have not been visited
        """
        unvisited = []
        for vertex in self.vertex_obj_map:
            if not self.vertex_obj_map[vertex].visited:
                unvisited.append(vertex)
        return unvisited
