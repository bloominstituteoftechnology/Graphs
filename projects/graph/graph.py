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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

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
        # Create an empty queue
        q = Queue()
        output = []

        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)

        # Create an empty set to store visited nodes
        s = set()

        # While the queue is not empty:
        while q.size() > 0:

            # Dequeue the first vertex
            dq = q.dequeue()

            # Check it its been visited
            if dq not in s:
                # If it has not mark it as visited, append to output
                s.add(dq)
                output.append(dq)

                # Then add all neighbors to the queue
                for v in self.get_neighbors(dq):
                    q.enqueue(v)

        print(output)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        output = []

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                output.append(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        
        print(output)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create a set if none exists
        if visited is None:
            visited = set()

        # check if vertex is visited
        if starting_vertex not in visited:
            # if not, mark visited
            visited.add(starting_vertex)
            # and print the vertex id
            print(starting_vertex)
            # then call dft_recursive on each of the neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue
        q = Queue()
        # Add a PATH TO the starting vertex_id to the queue
        q.enqueue( [starting_vertex] )
        #Create an empty set
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            #Dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
            # check if it's the target
            if v == destination_vertex:
                # if so, return the path
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path before adding
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize a stack
        s = Stack()
        #Add path to starting vertex to the stack
        s.push( [starting_vertex] )
        # create empty set 
        visited = set()

        # while stack not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # get last vertex from path
            v = path[-1]
            # see if it's the destination
            if v==destination_vertex:
                # if so, return the path
                return path
            # if it hasn't been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # and push a path to all neighbors to the stack 
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited
        if visited is None:
            visited = set()
        # initialize path
        if path is None:
            path = []
        #check if starting vertex has been visited
        # If not...
        if starting_vertex not in visited:
            # mark visited, add to path
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # If starting vertex is destination
            if starting_vertex == destination_vertex:
                return path_copy
            # Call DFS recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path


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
    print(f'Vertices: {graph.vertices}')
    print('---'*10)

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
    print('BFT:')
    graph.bft(1)
    print('---'*10)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT:')
    graph.dft(1)
    print('DFT Recursive:')
    graph.dft_recursive(1)
    print('---'*10)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS Path: ')
    print(graph.bfs(1, 6))
    print('---'*10)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS: ')
    print(graph.dfs(1, 6))
    print('DFS Recursive: ')
    print(graph.dfs_recursive(1, 6))
