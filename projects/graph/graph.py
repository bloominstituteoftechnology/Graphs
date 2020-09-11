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
        self.vertices[vertex_id] =set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

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
        next_in_line = Queue()

        visited = set()

        next_in_line.enqueue(starting_vertex)

        while next_in_line.size() > 0:
            v = next_in_line.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                neighbors = self.get_neighbors(v)

                for n in neighbors:
                    next_in_line.enqueue(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        next_in_line = Stack()

        visited = set()

        next_in_line.push(starting_vertex)

        while next_in_line.size() > 0:
            v = next_in_line.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                neighbors = self.get_neighbors(v)

                for n in neighbors:
                    next_in_line.push(n)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        neighbors = self.get_neighbors(starting_vertex)
        visited.add(starting_vertex)
        print(starting_vertex)

        for n in neighbors:
            if n not in visited:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        next_in_line = Queue()

        visited = set()

        next_in_line.enqueue([starting_vertex])

        while next_in_line.size() > 0:
            p = next_in_line.dequeue()
            v = p[-1]
            if v not in visited:
                visited.add(v)
                neighbors = self.get_neighbors(v)

                for n in neighbors:
                    next_in_line.enqueue(p+[n])

                if v == destination_vertex:
                    return p

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        next_in_line = Stack()

        path = []

        visited = set()

        next_in_line.push(starting_vertex)

        while next_in_line.size() > 0:
            v = next_in_line.pop()
            path.append(v)
            if v not in visited:
                visited.add(v)
                neighbors = self.get_neighbors(v)

                for n in neighbors:
                    next_in_line.push(n)

                if v == destination_vertex:
                    return path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        neighbors = self.get_neighbors(starting_vertex)
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for n in neighbors:
            if n not in visited:
                new_path = self.dfs_recursive(n, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

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
