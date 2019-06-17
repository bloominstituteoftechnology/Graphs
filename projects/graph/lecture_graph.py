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
            raise IndexError("That vertex does not exist!")


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Stack and push the starting vertex
        s = Stack()
        s.push(starting_vertex)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)




    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty set to store visited nodes
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        # While the queue is not empty...
            # Dequeue the first PATH
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # IF VERTEX = TARGET, RETURN PATH
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add A PATH TO all of its neighbors to the back of the queue
                    # Copy the path
                    # Append neighbor to the back of the copy
                    # Enqueue copy



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
