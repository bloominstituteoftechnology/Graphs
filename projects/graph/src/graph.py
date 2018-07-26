#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("Error: Vertex already exists")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: %s and/or %s do not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        """Search using bfs or dfs"""
        queue_stack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while queue_stack:
            current = queue_stack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            queue_stack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        """Identify components and update vertex component ids"""
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)