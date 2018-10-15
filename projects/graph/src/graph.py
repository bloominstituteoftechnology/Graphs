"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # pass  # TODO
        self.vertices = {}
    def add_vertex (self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge (self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge (self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def depth_tranversal(self, vertex_id, visited):
        print(vertex_id)
        visited.append(vertex_id)
        for child_node in vertices[vertex_id]:
            if child_node not in visited:
                depth_tranversal(vertices, vertex_id, visited)

#        unvisited = white, 
#        verts whose neighbors are being explored = gray, 
#        verts with no unexplored neighbors = black




