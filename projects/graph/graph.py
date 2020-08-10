"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of
    vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            self.vertices[v1].add(v2)
        except KeyError:
            return f'VERTEX {v1} IS NOT A VALID VERTEX'

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
        visited = [False] * (len(self.vertices)+1)

        traversal = []

        queue = Queue()
        queue.enqueue(starting_vertex)

        visited[starting_vertex] = True

        while queue:

            vertex = queue.dequeue()
            traversal.append(vertex)

            for x in self.vertices[vertex]:
                if visited[x] is False:
                    queue.enqueue(x)
                    visited[x] = True

        print('\n'.join(str(x) for x in traversal))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = [False] * (len(self.vertices)+1)

        traversal = []

        stack = Stack()
        stack.push(starting_vertex)

        visited[starting_vertex] = True

        while stack:

            vertex = stack.pop()
            traversal.append(vertex)

            for x in self.vertices[vertex]:
                if visited[x] is False:
                    stack.push(x)
                    visited[x] = True

        print('\n'.join(str(x) for x in traversal))

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if not visited:
            visited = [False] * (len(self.vertices)+1)

        visited[starting_vertex] = True

        print(starting_vertex, end='\n')

        for x in self.vertices[starting_vertex]:
            if visited[x] is False:
                self.dft_recursive(x, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = [False] * (len(self.vertices) + 1)

        traversal = []

        queue = Queue()
        queue.enqueue(starting_vertex)

        visited[starting_vertex] = True

        while queue and destination_vertex not in traversal:

            vertex = queue.dequeue()
            traversal.append(vertex)

            for x in sorted(self.vertices[vertex], reverse=True):
                if x is destination_vertex:
                    traversal.append(destination_vertex)
                    break
                if visited[x] is False:
                    queue.enqueue(x)
                    visited[x] = True

        return traversal

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = [False] * (len(self.vertices) + 1)

        traversal = []

        stack = Stack()
        stack.push(starting_vertex)

        visited[starting_vertex] = True

        while stack and destination_vertex not in traversal:

            vertex = stack.pop()
            traversal.append(vertex)

            for x in self.vertices[vertex]:
                if x is destination_vertex:
                    traversal.append(destination_vertex)
                    break
                if visited[x] is False:
                    stack.push(x)
                    visited[x] = True

        return traversal

    def dfs_recursive(self, starting_vertex, destination_vertex,
                      visited=None, traversal=None, stack=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if not visited:
        #     visited = [False] * (len(self.vertices) + 1)
        # if not traversal:
        #     traversal = []
        #
        # if starting_vertex is destination_vertex:
        #     traversal.append(starting_vertex)
        #     return traversal
        #
        # visited[starting_vertex] = True
        # if starting_vertex not in traversal:
        #     traversal.append(starting_vertex)
        #
        # for x in self.vertices[starting_vertex]:
        #     if x is destination_vertex:
        #         traversal.append(x)
        #         return traversal
        #     if visited[x] is False:
        #         self.dfs_recursive(starting_vertex=x,
        #                            destination_vertex=destination_vertex,
        #                            visited=visited, traversal=traversal)

        if not visited:
            visited = [False] * (len(self.vertices) + 1)

        if not traversal:
            traversal = []

        if not stack:
            stack = Stack()
            stack.push(starting_vertex)

        visited[starting_vertex] = True

        vertex = stack.pop()
        traversal.append(vertex)

        for x in self.vertices[vertex]:
            if x is destination_vertex:
                traversal.append(destination_vertex)
                break
            if visited[x] is False:
                stack.push(x)
                visited[x] = True

        while stack and destination_vertex not in traversal:
            self.dfs_recursive(stack.storage[-1], destination_vertex,
                               visited=visited, traversal=traversal,
                               stack=stack)

        return traversal


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
    graph.add_edge(0, 4)

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
