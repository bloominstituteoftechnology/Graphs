"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def breadth_first_traversal(self, starting_node):
        to_visit = []
        visited = set()
        to_visit.append(starting_node)
        while to_visit:
            deq_node = to_visit.pop(0)
            print(deq_node)
            if deq_node not in visited:
                visited.add(deq_node)
                for child in self.vertices[deq_node]:
                    to_visit.append(child)

    def depth_first_traversal(self, starting_node):
        to_visit = []
        visited = set()
        to_visit.append(starting_node)
        while to_visit:
            deq_node = to_visit.pop()
            print(deq_node)
            for child in self.vertices[deq_node]:
                to_visit.append(child)