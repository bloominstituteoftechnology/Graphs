"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        
        return

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            return None
        else:
            self.vertices[v1].add(v2)

        return

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        q = Queue()

        visited = set()
        q.enqueue(starting_vertex)

        # While the queue is not empty
        # continue looping
        while q.size() > 0:
            # dequeue the first item
            v = q.dequeue()
            
            # while the current_vertex is in the list
            # of already visited nodes, dequeue again
            if v not in visited:
                # enqueue all the next verticies to the queue
                for x in self.get_neighbors(v):
                    q.enqueue(x)

                # Add the current node to the list of visited nodes
                visited.add(v)

        for x in visited:
            print(x)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = set()
        s.push(starting_vertex)

        # While the queue is not empty
        # continue looping
        while s.size() > 0:
            # dequeue the first item
            v = s.pop()
            
            # while the current_vertex is in the list
            # of already visited nodes, dequeue again
            if v not in visited:
                print(v)
                # Add the current node to the list of visited nodes
                visited.add(v)
                # enqueue all the next verticies to the queue
                for x in self.get_neighbors(v):
                    s.push(x)

    def dft_recursive(self, starting_vertex, cache=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        if cache is None:
            cache = set()
        
        cache.add(starting_vertex)

        for x in self.get_neighbors(starting_vertex):
            if x not in cache:
                self.dft_recursive(starting_vertex=x, cache=cache)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # if the last vertex is not in visited
            # we need to check its neighbors
            if last_vertex not in visited:
                # If the last vertex is the destination, return the path
                if last_vertex == destination_vertex:
                    return path
                # else, we create new paths with each neighbor
                # of the last vertex and enqueue them to be searched
                else:
                    for x in self.get_neighbors(last_vertex):
                        q.enqueue(path + [x])
                visited.add(last_vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # if the last vertex is not in visited
            # we need to check its neighbors
            if last_vertex not in visited:
                # If the last vertex is the destination, return the path
                if last_vertex == destination_vertex:
                    return path
                # else, we create new paths with each neighbor
                # of the last vertex and enqueue them to be searched
                else:
                    for x in self.vertices[last_vertex]:
                        s.push(path + [x])
                visited.add(last_vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        
        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        for x in self.get_neighbors(starting_vertex):
            if x not in visited:
                new_path = self.dfs_recursive(starting_vertex=x, destination_vertex=destination_vertex, path=path, visited=visited)

                if new_path:
                    return new_path
        
        return None
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
