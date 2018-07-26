#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Represent a vertex with a label and possible connected component."""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    def __init__(self):
        self.vertices = dict()
        self.components = 0

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception('Error no edges to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        """Identify components and update vertex component ids."""
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

def main():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

if __name__ == "__main__":
    main()