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
        Adds a new vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Adds a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Gets all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Add starting vertex ID
        q.enqueue(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        s = Stack()

        # Add starting vertex ID
        s.push(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while s.size() > 0:

            # Dequeue a vert
            v = s.pop()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
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
        # Create a set to store visited vertices
        visited = set()

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a set to store visited vertices
        visited = set()

        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            current_path = s.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    # graph.dft_recursive(1)

    print("")

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
    # print(graph.dfs_recursive(1, 6))
