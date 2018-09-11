class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        self.vertices[node] = set()
        return self.vertices

    def add_edge(self, from_node, to_node):
        self.vertices[from_node].add(to_node)
        self.vertices[to_node].add(from_node)
        return

    def add_directed_edge(self, ver1, ver2):
        if ver1 in self.vertices:
            self.vertices[ver1].add(ver2)
        else:
            raise IndexError(
                'That vertex value is not available. please add it first')

    def dfs(adjList, node_id, visited=[]):
        visited.append(node_id)
        for child_node in adjList[node_id]:
            if child_node not in visited:
                dft(adjList, child_node, visited)
        if target:
            print('Target not found!')

    def bft(adjList, node_id):
        frontier = []
        frontier.append(node_id)
        visited = []
        while len(frontier > 0):
            n = frontier.pop(0)
            if n not in visited:
                print(n)
                visited.append(n)
                for next_node in adjList[n]:
                    frontier.append(next_node)

    def __str__(self):
        return f"{self.vertices}"
