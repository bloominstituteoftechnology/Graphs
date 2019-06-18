class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

        raise IndexError("Stack empty cannot pop")

    def size(self):
        return len(self.stack)


class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            return

        raise IndexError("Vertices not found")

    def dfs(self, starting_vertex):
        # Create empty set
        vertices = set()
        # Create empty Stack
        stack = Stack()

        # Add vertex path to Stack
        initial_path = [starting_vertex]
        stack.push(initial_path)

        final_paths = []

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in vertices:
                vertices.add(vertex)

                # Available path at the end of traversal
                # shall be stored in output.
                if len(self.vertices[vertex]) == 0:
                    final_paths.append(path)

                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        new_path = path.copy()
                        new_path.append(next_vertex)

                        stack.push(new_path)

        max_path_len = float('-inf')
        parent_vertex = float('inf')

        for path in final_paths:
            if len(path) > max_path_len:
                max_path_len = len(path)
                parent_vertex = path[-1]

            if len(path) == max_path_len:
                parent_vertex = min(parent_vertex, path[-1])

        return parent_vertex


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(10)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(4)
    graph.add_vertex(11)
    graph.add_vertex(3)
    graph.add_vertex(5)
    graph.add_vertex(8)
    graph.add_vertex(6)
    graph.add_vertex(9)
    graph.add_vertex(7)

    graph.add_edge(6, 3)
    graph.add_edge(6, 5)
    graph.add_edge(7, 5)
    graph.add_edge(9, 8)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(5, 4)
    graph.add_edge(8, 4)
    graph.add_edge(8, 11)
    graph.add_edge(1, 10)

    # print(graph.dfs(6))
    # print(graph.dfs(9))
