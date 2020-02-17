"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping
    labels to edges."""

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
            raise IndexError("That vertex does not exist.")

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
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Base case...
        if visited is None:
            # Create a Set to store visited verticies
            visited = set()
        # Add starting vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # Find neighbors to starting vertex
        for next_vert in self.vertices[starting_vertex]:
            # If vertex has not been added to visited...
            if next_vert not in visited:
                # Recursively call function on new verticies
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH to the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited verticies
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH to its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    # COPY THE PATH and append the new vertex
                    new_path = path.copy()
                    new_path.append(next_vert)
                    # Append the neighbor to the back
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH to the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited verticies
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH to its neighbors to the top of the stack
                for next_vert in self.get_neighbors(v):
                    # COPY THE PATH and append the new vertex
                    new_path = path.copy()
                    new_path.append(next_vert)
                    # Add the neighbor to the top of the stack
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Base case...
        if visited is None and path is None:
            # Create a Set to store visited verticies
            visited = set()
            # Create a list to store the path
            path = []
        # Add starting vertex to visited
        visited.add(starting_vertex)
        # Add starting vertex to the path
        path.append(starting_vertex)
        # Check if starting vertex is the target
        if starting_vertex == destination_vertex:
            return path
        # Find neighbors of starting vertex
        for next_vert in self.get_neighbors(starting_vertex):
            # If neighbor hasn't been visited...
            if next_vert not in visited:
                # Recursively call function
                new_path = self.dfs_recursive(
                    next_vert, destination_vertex, visited, path)
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
    print('\nGraph Verticies:\n', graph.vertices)

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
    print("\nBreadth First Traversal:")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nDepth First Traversal:")
    graph.dft(1)
    print("\nDepth First Traversal Recursively:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('\nBreadth First Search:\n', graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('\nDepth First Search:\n', graph.dfs(1, 6))
    # print('\nDepth First Search Recursively:\n', graph.dfs_recursive(1, 6))
