"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError(
                f'at least one of ({v1},{v2}) vertexes does not exist')

    def bfs_iterate(self, q, cb, visited):

        #  using parents q cv level saving nodes in child q
        #  parents q = child q
        child_q = Queue()
        while q.size() > 0:
            index = q.dequeue()
            for neigbor in self.vertices[index]:
                if neigbor not in visited:
                    visited.add(neigbor)
                    child_q.enqueue(neigbor)
                    cb(neigbor)

        if child_q.size() > 0:
            self.bfs_iterate(child_q, cb, visited)

    def bft(self, starting_vertex, cb=None):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if cb is None:
            def cb(x): return print(x, end=' ')
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                cb(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        print('bft')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v, end=' ')
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        print('dft')

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        first = (visited is None)
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex, end=' ')
            visited.add(starting_vertex)
            for neigbor in self.vertices[starting_vertex]:
                self.dft_recursive(neigbor, visited)
        if first:
            print('dft_recursive')

    def bft_recursive(self, starting_vertex):
        visited = {starting_vertex}
        q = Queue()
        q.enqueue(starting_vertex)
        def cb(x): return print(x, end=' ')
        cb(starting_vertex)
        self.bfs_iterate(q, cb, visited)
        print('bft_recursive')

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v == destination_vertex:
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    path_copy = [*path, neighbor]
                    q.enqueue(path_copy)

        raise IndexError(f"bfs {starting_vertex} doesn't connect to {destination_vertex}")                    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v == destination_vertex:
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    path_copy = [*path, neighbor]
                    s.push(path_copy)

        raise IndexError(f"dfs {starting_vertex} doesn't connect to {destination_vertex}")


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)


    """
    Valid BFT recursive paths:   

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

    graph.bft_recursive(1)    

    '''
    Valid BFS path:

        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6), 'BFS Path')
    try:
        print(graph.bfs(6, 7), 'bad BFS Path')
    except Exception as e:
        print('Exception ',e)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6), 'DFS Path')
    try:
        print(graph.dfs(6, 7), 'bad DFS Path')
    except Exception as e:
        print('Exception ',e)    
