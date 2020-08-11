"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
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
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("one of those vertices was not found")

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
        q = Queue()

        # Add starting vertex
        q.enqueue(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty:
        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create empty stack
        s = Stack()

        # Add starting vertex
        s.push(starting_vertex)

        # Create set for visited vertices
        visited = set()

        # While stack is not empty
        while s.size() > 0:

            # Pop a vertex
            v = s.pop()

            # If not visited
            if v not in visited:
                print(v)
                visited.add(v)

                # Add all neighbors to queue
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create empty stack
        s = Stack()

        # Add starting vertex
        s.push(starting_vertex)

        # Create set for visited vertices
        visited = set()

        def internal_dft(stack):
            if stack.size() < 1:
                return

            else:
                # Pop a vertex
                v = stack.pop()

                # If not visited
                if v not in visited:
                    print(v)
                    visited.add(v)

                    # Add all neighbors to queue
                    for neighbor in self.get_neighbors(v):
                        stack.push(neighbor)

                return(internal_dft(stack))

        return internal_dft(s)

    def bfs(self, starting_vertex, target_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        # Add path to starting vertex
        q.enqueue([starting_vertex])

        # Create set for visited verts
        visited = set()

        # While queue is not empty:
        while q.size() > 0:

            v = q.dequeue()

            # assign
            v1 = v[-1]

            # Look for last value in path
            if v1 not in visited:
                if v1 == target_vertex:
                    return v
                visited.add(v1)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(v1):
                    # add node to path
                    # make a copy of v to append neighbor
                    v_copy = v.copy()
                    v_copy.append(neighbor)
                    # enqueue the path
                    q.enqueue(v_copy)


    def dfs(self, starting_vertex, target_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        # Add path to starting vertex
        s.push([starting_vertex])

        # Create set for visited verts
        visited = set()

        # While queue is not empty:
        while s.size() > 0:

            v = s.pop()

            # assign
            v1 = v[-1]

            # Look for last value in path
            if v1 not in visited:
                if v1 == target_vertex:
                    return v
                visited.add(v1)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(v1):
                    # add node to path
                    # make a copy of v to append neighbor
                    v_copy = v.copy()
                    v_copy.append(neighbor)
                    # enqueue the path
                    s.push(v_copy)
    
    def dfs_recursive(self, starting_vertex, target_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()

        # Add path to starting vertex
        s.push([starting_vertex])

        # Create set for visited verts
        visited = set()

        def internal_dfs(stack):
            # While queue is not empty:
            if stack.size() < 1:
                return
            
            else:
                v = stack.pop()

                # assign
                v1 = v[-1]

                # Look for last value in path
                if v1 not in visited:
                    if v1 == target_vertex:
                        return v
                    visited.add(v1)

                    # add all neighbors to queue
                    for neighbor in self.get_neighbors(v1):
                        # add node to path
                        # make a copy of v to append neighbor
                        v_copy = v.copy()
                        v_copy.append(neighbor)
                        # enqueue the path
                        stack.push(v_copy)
                return internal_dfs(stack)
        
        return internal_dfs(s)

    # During lecture coding, with a default parameter
    # both approaches are fine
    # def dft_recursive(self, starting_vertex, visited=None):

    #     if visited is None:
    #         visited = set()

    #     visited.add(starting_vertex)

    #     print(starting_vertex)

    #     for neighbor in self.vertices[starting_vertex]:
    #         if neighbor not in visited:
    #             self.dft_recursive(neighbor, visited)

    # def dfs_recursive(self, starting_vert, ending_vert, visited=None, path=None):
    #     if visited is None:
    #         visited = set()
    #     if path is None:
    #         path = []

    #     visited.add(starting_vert)

    #     path = path + [starting_vert]  # subtly makes copy of the path

    #     # perhaps a clearer way of writing the above line:
    #     # new_path = list(path)
    #     # new_path.append(starting_vert)

    #     if starting_vert == ending_vert:
    #         return path

    #     for neighbor in self.get_neighbors(starting_vert):
    #         if neighbor not in visited:
    #             new_path = self.dfs_recursive(neighbor, ending_vert, visited, path)
    #             # only return if new path received
    #             if new_path is not None:
    #                 return new_path
        
    #     return None


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
    print("Vertices:")
    print(graph.vertices)
    print("\n")

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
    print("BFT:")
    graph.bft(1)
    print("\n")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT:")
    graph.dft(1)
    print("\n")

    print("DFT Recursive:")
    graph.dft_recursive(1)
    print("\n")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS:")
    print(graph.bfs(1, 6))
    print("\n")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS:")
    print(graph.dfs(1, 6))
    print("\n")

    print("DFS Recursive")
    print(graph.dfs_recursive(1, 6))
    print("\n")
