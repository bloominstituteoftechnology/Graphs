"""
Simple graph implementation compatible with BokehGraph class.
"""
import sys


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            sys.exit("Vertex {} already exists.".format(vertex))

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex1))
        elif vertex2 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex2))
        else:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)

    def Search(self, start, target=None, type="bfs"):
        """Search the graph using BFS/DFS based on type"""
        queue = [start]
        # remove first if a bfs (queue) and last if dfs (stack)
        remove_index = 0 if type == "bfs" else -1
        # if we make visited a set, can do set operations with the vertices
        visited = set([start])

        while queue:
            current = queue.pop(remove_index)
            if current == target:
                return True
            visited.add(current)
            # Add to visit vertices to queue
            queue.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

        return False


class Vertex:
    """Represent a vertex with an id, value, color, edges"""

    def __init__(self, vertex_id, value, color="red"):
        self.vertex_id = str(vertex_id)
        self.value = value
        self.color = color
        self.edges = []

    def __repr__(self):
        return 'Vertex: ' + self.vertex_id


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# print(graph.vertices)
print(graph.Search('0', '3', 'bfs'))
print(graph.Search('0', '3', 'dfs'))
