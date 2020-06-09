class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex_and_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
            return
        self.vertices[v1] = set()
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in range(len(ancestors)):
        graph.add_vertex_and_edge(ancestors[i][1], ancestors[i][0])

    try:
        graph.get_neighbors(starting_node)
        pass
    except KeyError:
        return -1

    stack = []
    stack.append(starting_node)

    visited = set()


    while len(stack) > 0:
        curr = stack.pop()

        if curr not in visited:
            visited.add(curr)

            try:
                vert = min(graph.get_neighbors(curr))
                stack.append(vert)
            except KeyError:
                return curr