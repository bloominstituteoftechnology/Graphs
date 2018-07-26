#!/usr/bin/python
"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, label, component= -1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def create_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have an edge for a vertex that does not exist')
        self.vertices[vertex] = set(edges)

    def create_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Those vertices are not in this graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def bfs(self, start, target=None):
        queue = [start]
        visited = set()

        while queue:
            current = queue.pop(0)
            if current == target:
                break
            visited.add(current)
            queue.extend(self.vertices[current] - visited)

        return visited

    def dfs(self, start, target=None):
        stack = [start]
        visited = set()

        while stack:
            current = stack.pop()
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[surrent] - visited)

        return visited
            
    
    def search(self, start, target=None, method='dfs'):
        quack = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            quack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
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

graph = Graph()
graph.create_vertex('0')
graph.create_vertex('1')
graph.create_vertex('2')
graph.create_vertex('3')
graph.create_vertex('4')
graph.create_vertex('5')
graph.create_vertex('6')
graph.create_vertex('7')
graph.create_edge('0', '1')
graph.create_edge('1', '2')
graph.create_edge('2', '3')
graph.create_edge('3', '4')
graph.create_edge('4', '5')
graph.create_edge('5', '6')
graph.create_edge('7', '0')
print(graph.vertices)