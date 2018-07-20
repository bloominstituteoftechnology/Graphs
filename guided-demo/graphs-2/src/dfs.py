from sys import argv

class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight


class Vertex:
    def __init__(self, value='vertex'):
        self.value = value
        self.edges = set()
        self.color = None


class Graph:
    def __init__(self):
        self.vertices = set()

    def add_edge(self, vertex_a, vertex_b):
        """Add a *bidirectional* edge between two vertices."""
        if vertex_a not in self.vertices or vertex_b not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        vertex_a.edges.add(vertex_b)
        vertex_b.edges.add(vertex_a)

    def dfs(self, start, target=None):
        if start not in self.vertices:
            raise Exception('Start vertex not in graph!')

        visit_stack = [start]
        visited = set()
        while visit_stack:
            visiting = visit_stack.pop()
            visited.add(visiting)
            visiting.color = 'gray'
            if target and visiting == target:
                print('Found target:', visiting)
                return
            visit_stack.extend(visiting.edges - visited)

        if target:
            print('Target not found!')


def main(num_vertices=8, num_edges=8):
    """Build demo graph and execute DFS."""
    graph = Graph()
    for num in range(num_vertices):
        graph.vertices.add(Vertex(str(num)))

    # Add some random edges
    from random import sample
    for _ in range(num_edges):
        vertices = sample(graph.vertices, 2)
        graph.add_edge(vertices[0], vertices[1])

    # DFS with random start/target
    start, target = sample(graph.vertices, 2)
    graph.dfs(start, target)


if __name__ == '__main__':
    if len(argv) == 3:
        num_vertices = argv[1]
        num_edges = argv[2]
        main(num_vertices, num_edges)
    else:
        main()  # accept defaults
