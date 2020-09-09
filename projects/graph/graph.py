"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #  Create a queue to hold nodes to visit
        bft_queue = Queue()
        #  Create a set to hold visited nodes
        visited = set()

        #  Add the starting node to the queue
        bft_queue.enqueue(starting_vertex)

        #  Loop whie the queue is not empty
        while bft_queue.size() > 0:
            # Grab first vertex
            vertex = bft_queue.dequeue()

            #  Check if previously visited
            if vertex not in visited:
                # Print the node
                print(f'bft vertex: {vertex}')
                # Add to visited list
                visited.add(vertex)
                # Add all neighbors to queue
                for neighbor in self.get_neighbors(vertex):
                    bft_queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #  Create a stack to hold nodes to visit
        bft_stack = Stack()
        #  Create a set to hold visited nodes
        visited = set()

        #  Add the starting node to the stack
        bft_stack.push(starting_vertex)

        #  Loop whie the queue is not empty
        while bft_stack.size() > 0:
            # Grab first vertex
            vertex = bft_stack.pop()

            #  Check if previously visited
            if vertex not in visited:
                # Print the node
                print(f'dft vertex: {vertex}')
                # Add to visited list
                visited.add(vertex)
                # Add all neighbors to queue
                for neighbor in self.get_neighbors(vertex):
                    bft_stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(f'dft_recuresive vertex: {starting_vertex}')

        neighbors = self.get_neighbors(starting_vertex)
        visited.add(starting_vertex)
        
        for vertex in neighbors:
            if vertex not in visited:
                self.dft_recursive(vertex, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        path = Queue()

        # Add the starting vertex to the path
        path.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while path.size() > 0:
            # Dequeue the first PATH
            new_path = path.dequeue()
            # Grab the last vertex from the PATH
            edge = new_path[-1]
            # If that vertex has not been visited...
            if edge not in visited:
                # CHECK IF IT'S THE TARGET
                if edge is destination_vertex:
                    # IF SO, RETURN PATH
                    return new_path
                visited.add(edge)
                # Then add A PATH TO its neighbors to the back of the queue
                neighbors = self.get_neighbors(edge)
                for neighbor in neighbors:
                    # Copy the path
                    path_copy = new_path.copy()
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)
                    path.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        path = Stack()

        # Add the starting vertex to the path
        path.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        #  Add the starting vertex to the set
        visited.add(starting_vertex)

        # Loop while the stack is not empty
        while path.size() > 0:
            # Pop the first element
            new_edge = path.pop()
            # Add the popped element to the visited set
            visited.add(new_edge)

            # Get all neighbors
            neighbors = self.get_neighbors(new_edge)
           
           # Put all the neighbors on the stack
            for neighbor in neighbors:
                if neighbor not in visited:
                   path.push(neighbor)
                if neighbor is destination_vertex:
                    visited.add(neighbor)
                    return list(visited)


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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
