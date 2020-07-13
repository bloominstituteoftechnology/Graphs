"""
Simple graph implementation
"""
from util import Queue  # These may come in handy
from util import Stack


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()  # TODO
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)

            for edge in self.vertices[vertex]:
                if edge not in visited:
                    queue.enqueue(edge)

        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()  # TODO
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)

            for edge in self.vertices[vertex]:
                if edge not in visited:
                    stack.push(edge)

        return visited

    def dft_recursive(self, starting_vertex, cache=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)  # TODO

        if cache is None:
            cache = set()

        cache.add(starting_vertex)

        for i in self.get_neighbors(starting_vertex):
            if i not in cache:
                self.dft_recursive(starting_vertex=i, cache=cache)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = {}  # TODO
        queue = Queue()
        queue.enqueue([starting_vertex, None])
        while queue.size() > 0:
            (vertex, prev) = queue.dequeue()
            if vertex not in visited:
                visited[vertex] = prev
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    while step is not None:
                        path.append(step)
                        step = visited[step]
                    return path[::-1]

            for edge in self.vertices[vertex]:
                if edge not in visited:
                    queue.enqueue((edge, vertex))

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        visited = {}  # TODO
        stack = Stack()
        stack.push([starting_vertex, None])
        while stack.size() > 0:
            (vertex, prev) = stack.pop()
            if vertex not in visited:
                visited[vertex] = prev
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    while step is not None:
                        path.append(step)
                        step = visited[step]

                    return path[::-1]

            for edge in self.vertices[vertex]:
                if edge not in visited:
                    stack.push((edge, vertex))

    def dfs_recursive(
        self, starting_vertex, destination_vertex, path=None, visited=None
    ):

        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:  # TODO
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                new_path = self.dfs_recursive(
                    starting_vertex=i,
                    destination_vertex=destination_vertex,
                    path=path,
                    visited=visited,
                )

                if new_path:
                    return new_path

        return None


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
