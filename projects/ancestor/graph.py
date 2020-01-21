"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if not self.vertices.get(vertex_id):
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph if both currently exist in verticies.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Not Found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        already = set()
        q.enqueue(starting_vertex)
        while q.size():
            pop = q.dequeue()
            if pop not in already:
                print(pop)
                already.add(pop)
                for v in self.vertices[pop]:
                    q.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        already = set()
        s.push(starting_vertex)
        while s.size():
            now = s.pop()
            if now not in already:
                print(now)
                already.add(now)
            for v in self.vertices[now]:
                if v not in already:
                    s.push(v)

    def dft_recursive(self, starting_vertex, cache=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if cache is None:
            cache = set()
        print(starting_vertex)
        cache.add(starting_vertex)
        for v in self.vertices[starting_vertex]:
            if v not in cache:
                self.dft_recursive(v, cache)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        already = set()
        q = Queue()
        q.enqueue([starting_vertex])
        while q.size():
            path = q.dequeue()
            if destination_vertex in path:
                return path
            for v in self.vertices[path[-1]]:
                if v not in already:
                    q.enqueue(list(path)+[v])
                    already.add(v)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        already = set()
        s = Stack()
        s.push([starting_vertex])
        while s.size():
            path = s.pop()
            if destination_vertex in path:
                return path
            for v in self.vertices[path[-1]]:
                if v not in already:
                    s.push(list(path) + [v])
                    already.add(v)

    def dfs_recursive(self, starting_vertex, destination_vertex, cache=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if cache is None:
            cache = set()
        if path is None:
            path = []
        cache.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for v in self.vertices[starting_vertex]:
            if v not in cache:
                new_path = self.dfs_recursive(
                    v, destination_vertex, cache, path)
                if new_path:
                    return new_path
        return None

    def get_ancestor(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if self.vertices.get(starting_vertex) == set():
            return -1
        s = Stack()
        already = set()
        s.push(starting_vertex)
        current = starting_vertex
        while s.size():
            now = s.pop()
            if now not in already:
                if s.size() and self.vertices.get(now) == set():
                    now2 = s.pop()
                    if now2 < now:
                        now = now2
                current = now
                already.add(now)
            for v in self.vertices[now]:
                if v not in already:
                    s.push(v)
        return current


if __name__ == '__main__':
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
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
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
