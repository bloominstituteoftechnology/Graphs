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
        if not vertex_id in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Trying to link a non-existing edge')

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
        q.enqueue(starting_vertex)
        visited_vertices = set()
        while q.size() > 0:
            vertex = q.dequeue()
            if not vertex in visited_vertices:
                visited_vertices.add(vertex)
                print(vertex)
                for v in self.get_neighbors(vertex):
                    q.enqueue(v)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_vertices = set()
        while stack.size() > 0:
            vertex = stack.pop()
            if not vertex in visited_vertices:
                visited_vertices.add(vertex)
                print(vertex)
                for v in self.get_neighbors(vertex):
                    stack.push(v)

    def dft_recursive(self, starting_vertex, visited_vertices=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        if visited_vertices is None:
            visited_vertices = set()
        
        if not starting_vertex:
            return 
        elif starting_vertex:
            visited_vertices.add(starting_vertex)
            print(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                if not edge in visited_vertices:
                    self.dft_recursive(edge, visited_vertices)
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited_vertices = set()

        # While the queue is not empty...
        while q.size() > 0:

            # Dequeue the first PATH eg -> [a, b, c, r, g]
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited_vertices:

                for neighbor in self.get_neighbors(last_vertex):

                    # Create a new path of neighbors
                    new_path = list(path)
                    new_path.append(neighbor)

                    # CHECK IF IT'S THE TARGET
                    if neighbor == destination_vertex:
                        # IF SO, RETURN PATH
                        return new_path
                    # Then add A PATH TO its neighbors to the back of the queue
                    q.enqueue(new_path)
                # Mark it as visited...
                visited_vertices.add(last_vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        stack = Stack()
        stack.push([starting_vertex])
        # Create a Set to store visited vertices
        visited_vertices = set()

        # While the queue is not empty...
        while stack.size() > 0:

            # Dequeue the first PATH eg -> [a, b, c, r, g]
            path = stack.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited_vertices:

                for neighbor in self.get_neighbors(last_vertex):

                    # Create a new path of neighbors
                    new_path = list(path)
                    new_path.append(neighbor)

                    # CHECK IF IT'S THE TARGET
                    if neighbor == destination_vertex:
                        # IF SO, RETURN PATH
                        return new_path
                    # Then add A PATH TO its neighbors to the top of the stack
                    stack.push(new_path)
                # Mark it as visited...
                visited_vertices.add(last_vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if path is None:
            path = [starting_vertex]
        
        if starting_vertex == destination_vertex:
            return path

        neighbors = self.get_neighbors(starting_vertex)
        
        # Get the vertices that are not in path but in neighbors
        diff = neighbors.difference(set(path))
    
        for neighbor in diff:

            new_path = self.dfs_recursive(neighbor, destination_vertex, path+[neighbor])

            if new_path:
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
