"""
Simple graph implementation compatible with BokehGraph class.
"""
class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    def getNeighbors(self):
        return self.neighbors
    def isNeighbor(self, node):
        return node in self.neighbors

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
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot set edges to non-existent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error: Verticies to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS"""
        chosen_data_structure = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set([start])

        while chosen_data_structure:
            current = chosen_data_structure.pop(pop_index)
            if current == target:
                break
            visited.add(current)

            chosen_data_structure.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

        return visited

graph = Graph()
print(graph.vertices)
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_edge('1', '2')
graph.add_vertex('3')
graph.add_edge('1', '3')
graph.add_edge('2','3', False)
print(graph.vertices)

print(graph.search('1', method='bfs'))
