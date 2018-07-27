
#!/usr/bin/python
"""Graph representation using adjacency list."""
class Vertex:
    """Vertices have a label and a set of edges and possible connected component."""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return self.label


"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception("Error: vertex already exists!")
        self.vertices[vertex] = set(edges)
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("supplied vertex not in graph!!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                return "Target {} found".format(target)
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