"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """
    Represent a directed graph as a dictionary of vertices mapping labels to
    sets of outgoing edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge v1 -> v2 to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (outgoing edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order beginning from
        starting_vertex.
        """
        printed = set()     # Nodes already printed.
        to_print = Queue()  # Nodes to print, in FIFO order for BFT.

        to_print.enqueue(starting_vertex)
        while to_print.size() > 0:
            vertex = to_print.dequeue()

            # The print queue can contain duplicate nodes, so we need to check
            # that a node hasn't already been printed before outputting it.
            if vertex not in printed:
                print(vertex)
                printed.add(vertex)

            # Append unvisited neighbors to the queue for future printing.
            for edge in self.vertices[vertex]:
                if edge not in printed:
                    to_print.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order beginning from starting_vertex.
        """
        printed = set()     # Nodes already printed.
        to_print = Stack()  # Nodes to print, in LIFO order for DFT.

        to_print.push(starting_vertex)
        while to_print.size() > 0:
            vertex = to_print.pop()

            # The print stack can contain duplicate nodes, so we need to check
            # that a node hasn't already been printed before outputting it.
            if vertex not in printed:
                print(vertex)
                printed.add(vertex)

            # Push unvisited neighbors to the stack for future printing.
            for edge in self.vertices[vertex]:
                if edge not in printed:
                    to_print.push(edge)

    def dft_recursive(self, starting_vertex, printed=None):
        """
        Print each vertex in depth-first order beginning from starting_vertex,
        using recursion.
        """
        # Special case for initial function call.
        if printed is None:
            printed = set()

        # Print the current vertex.
        print(starting_vertex)
        printed.add(starting_vertex)

        # Recursively print a DFT of each previously unvisited neighbor.
        for edge in self.vertices[starting_vertex]:
            if edge not in printed:
                self.dft_recursive(edge, printed)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from starting_vertex to
        destination_vertex in breath-first order.
        """
        visited = {}         # Maps visited node to the previous node in path.
        to_search = Queue()  # Tuples of (node, previous node) to be searched.

        to_search.enqueue((starting_vertex, None))
        while to_search.size() > 0:
            (vertex, prev) = to_search.dequeue()

            # Only unvisited nodes still need to be searched.
            if vertex not in visited:

                # Add vertex -> previous vertex entry to dictionary of visited
                # nodes.
                visited[vertex] = prev

                # If the destination vertex has been found, return the path by
                # which it was reached.
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    # Work backwards node-by-node to reconstruct the path.
                    while step is not None:
                        path.append(step)
                        step = visited[step]
                    # Reverse to return in order from start to destination.
                    return path[::-1]

                # Otherwise, continue searching. Add unvisited neighbors to the
                # queue, with the current node as the previous step.
                for edge in self.vertices[vertex]:
                    if edge not in visited:
                        to_search.enqueue((edge, vertex))

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from starting_vertex to
        destination_vertex in depth-first order.
        """
        visited = {}         # Maps visited node to the previous node in path.
        to_search = Stack()  # Tuples of (node, previous node) to be searched.

        to_search.push((starting_vertex, None))
        while to_search.size() > 0:
            (vertex, prev) = to_search.pop()

            # Only unvisited nodes still need to be searched.
            if vertex not in visited:

                # Add vertex -> previous vertex entry to dictionary of visited
                # nodes.
                visited[vertex] = prev

                # If the destination vertex has been found, return the path by
                # which it was reached.
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    # Work backwards node-by-node to reconstruct the path.
                    while step is not None:
                        path.append(step)
                        step = visited[step]
                    # Reverse to return in order from start to destination.
                    return path[::-1]

                # Otherwise, continue searching. Add unvisited neighbors to the
                # stack, with the current node as the previous step.
                for edge in self.vertices[vertex]:
                    if edge not in visited:
                        to_search.push((edge, vertex))

    def dfs_recursive(self,
                      starting_vertex,
                      destination_vertex,
                      visited=None):
        """
        Return a list containing a path from starting_vertex to
        destination_vertex in depth-first order, using recursion.
        """
        # Special case for initial function call.
        if visited is None:
            visited = []

        # Base case: destination vertex reached.
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        # Recursive case: continue searching.
        else:
            visited.append(starting_vertex)

            # Recursively search each unvisited neighbor in turn.
            for edge in self.vertices[starting_vertex]:
                if edge not in visited:
                    path = self.dfs_recursive(edge,
                                              destination_vertex,
                                              visited)
                    # Stop and return at the first successful search, if any.
                    if path is not None:
                        return [starting_vertex] + path

            # If no path to destination found through any neighbor of the
            # current node, drop back to the parent function call, returning
            # None.


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
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    print('DFT recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))
    print(f'If not in graph: {graph.bfs(1, 9)}\n')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS')
    print(graph.dfs(1, 6))
    print(f'If not in graph: {graph.dfs(1, 9)}\n')
    print('DFS recursive')
    print(graph.dfs_recursive(1, 6))
    print(f'If not in graph: {graph.dfs_recursive(1, 9)}')
