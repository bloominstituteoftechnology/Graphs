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
        else:
            raise ValueError("vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, theset=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if not has been visited
        # if not..
            # mark it as visited
            # call dft_recursive on each neighbor
        if theset is None:
            theset = set()
        if starting_vertex not in theset:
            theset.add(starting_vertex)
            print(starting_vertex)
            for i in self.vertices[starting_vertex]:
                self.dft_recursive(i, theset)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            lastq = q.dequeue()
            v = lastq[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v == destination_vertex:
                return(lastq)
            else:
                if v not in visited:
                    # Mark it as visited
                    visited.add(v)
                    # Enqueue all it's neighbors
                    for neighbor in self.get_neighbors(v):
                        temp = lastq.copy()
                        temp.append(neighbor)
                        q.enqueue(temp)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # Push the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            lastst = s.pop()
            v = lastst[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v == destination_vertex:
                return(lastst)
            else:
                if v not in visited:
                    # Mark it as visited
                    print(v)
                    visited.add(v)
                    # Push all it's neighbors onto the stack
                    for neighbor in self.get_neighbors(v):
                        temp = lastst.copy()
                        temp.append(neighbor)
                        s.push(temp)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        res = []
        def inner_dfs(starting_vertex, destination_vertex, theset = None, carryover = None):
            if theset is None:
                theset = set()
            if carryover is None:
                carryover = []
            if starting_vertex == destination_vertex:
                res.append(carryover)
                
                
            carryover.append(starting_vertex)
            starting_vertex = carryover[-1]
            if starting_vertex != destination_vertex:
                
            
                if starting_vertex not in theset:
                    theset.add(starting_vertex)
                    
                    for i in self.vertices[starting_vertex]:

                        carrycopy = carryover.copy()
                        intoset = theset.copy()
                        inner_dfs(i, destination_vertex, intoset, carrycopy)
        inner_dfs(starting_vertex, destination_vertex)
        return(res[0])
  

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
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
    #graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    #print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
