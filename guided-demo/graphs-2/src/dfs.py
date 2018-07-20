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
        vertex.b.edges.add(vertex_a)

    def dfs(self, start, target=None):
        if start not in self.vertices:
            raise Exception('Start vertex not in graph!')

        visit_stack = [start]
        while visit_stack:
            visiting = visit_stack.pop()
            visiting.color = 'gray'
            if target and visiting == target:
                print('Found target:', visiting)
                break
            visit_stack.extend(visiting.edges)


def main():
    """Build demo graph and execute DFS."""
    graph = Graph()
    # Construct graph with numbers 0-7 as vertices
    for num in range(8):
        graph.vertices.add(Vertex(str(num)))

    # Add some edges
    graph.add_edge(graph.vertices[0], graph.vertices[1])
    graph.add_edge(graph.vertices[1], graph.vertices[3])
    graph.add_edge(graph.vertices[0], graph.vertices[2])
    graph.add_edge(graph.vertices[2], graph.vertices[3])
    graph.add_edge(graph.vertices[2], graph.vertices[5])
    graph.add_edge(graph.vertices[6], graph.vertices[5])
    graph.add_edge(graph.vertices[4], graph.vertices[5])
    graph.add_edge(graph.vertices[7], graph.vertices[5])
    graph.add_edge(graph.vertices[7], graph.vertices[4])

    graph.dfs(graph.vertices[4], graph.vertices[0])



if __name__ == '__main__':
    main()
