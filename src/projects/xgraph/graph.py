from collections import deque


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph."""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edges to the graph."""
        if v1 not in self.vertices:
            raise KeyError(f"{v1} is not a node in this graph!")
        elif v2 not in self.vertices:
            raise KeyError(f"{v2} is not a node in this graph!")
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex."""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise KeyError(f"{vertex_id} is not a node in this graph!")

    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order beginning from starting_vertex."""
        q = deque()
        q.append(starting_vertex)
        visited = set()  # every element is unique (no duplicates)
        while q:  # q will equate to FALSE if empty
            vert = q.popleft()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for next_vert in self.vertices[vert]:
                    q.append(next_vert)

    def dft(self, starting_vertex):
        """Print each vertex in depth-first order beginning from starting_vertex."""
        stack = deque()
        stack.append(starting_vertex)
        visited = set()
        while stack:  # stack will equate to FALSE if empty
            vert = stack.pop()  # take vertex off the top of stack (end of deque)
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    stack.append(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """Print each vertex in depth-first order beginning from starting_vertex."""
        if not visited:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)  # print before recurse/loop
        for next_vert in self.vertices[starting_vertex]:
            # if next_vert hasn't been visited yet -- let's visit it!
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = deque()
        q.append([starting_vertex])  # creating a series of lists
        # the queue contains each possible path from point a to point b
        visited = set()
        while q:
            path = q.popleft()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    new_path = path + [next_vert]
                    # new_path.append(next_vert)
                    q.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        stack.append([starting_vertex])  # stack will contain list of paths
        visited = set()
        while len(stack) > 0:
            path = stack.pop()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if not visited:
            visited = set()

        if not path:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child_vert in self.get_neighbors(starting_vertex):
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your xgraph
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
