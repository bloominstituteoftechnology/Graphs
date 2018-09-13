"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.root = None

    def add_vertex(self, vertex):
        if self.root is None:
           self.root = vertex
        if vertex in self.vertices:
            raise Exception(f'vertex {vertex} already exists')
        
        self.vertices[vertex] = set()
    
    def add_edge(self, vertex1, vertex2):
        if not vertex1 in self.vertices:
            raise Exception(f'vertex1: {vertex1} does not exist')
        
        if not vertex2 in self.vertices:
            raise Exception(f'vertex2: {vertex2} does not exist')

        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)
    
    def add_directional_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices[vertex2]:
            raise Exception(f'Use the add_edge method instead')
        self.vertices[vertex1].add(vertex2)dge method instead')
        self.vertices[vertex1].add(vertex2)
    
    def set_root_vertex(self, root_vertex):
        self.root = root_vertex
    
    def dfs(self):
        ids = []
        visited = {}
        def get_node_ids(start_vert = self.root):
            visited[start_vert] = 1
            ids.append(start_vert.id)
            for child_vert in self.vertices[start_vert]:
                if child_vert not in visited:
                    get_node_ids(child_vert)

        get_node_ids()
        return ids
