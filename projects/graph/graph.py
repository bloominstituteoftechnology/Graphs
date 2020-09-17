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
        # check if vertex in dict:
        if vertex_id not in self.vertices:
            self.vertices = set()
        else:
            print('Duplicate! Vertex not updated!')

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if v1 in graph
        if v1 in self.vertices:
            # check if v2 in graph
            if v2 in self.vertices:
                self.vertices[v1].add(v2)      
        else:
            return 'One or more vertices not found!'       
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # check if vertex in graph
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return set()

    # default function to use in traversals 
    def print_path(self, vertex):
        print(str(vertex) + '\n' + ' |' + '\n' + '\/')

    # adding func to allow for variation in operation application
    def bft(self, starting_vertex, func = self.print_path):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()

        # check if starting vertex in graph and add to begin traversal
        if starting_vertex in self.vertices:
            queue.enqueue(starting_vertex)
        else:
            return 'Starting vertex not found!'

        while queue:
            vertex = queue.dequeue()
            
            # check if current vertex has been visited
            if vertex not in visited:

                # get all vertices to be visted next added to queue
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)
                
                # perform function operation on current vertex
                func(vertex)

            # add current vertex to visited set avoid collisions with neighboring edges
            visited.add(vertex)
            

    
    # adding func to allow for variation in operation application
    def dft(self, starting_vertex, func = self.print_path):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()

        # check if starting vertex in graph and add to begin traversal
        if starting_vertex in self.vertices:
            stack.push(starting_vertex)
        else:
            return 'Starting vertex not found!'

        while stack:
            vertex = stack.pop()
            
            # check if current vertex has been visited
            if vertex not in visited:

                # get all vertices to be visted next added to queue
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)
                
                # perform function operation on current vertex
                func(vertex)

            # add current vertex to visited set avoid collisions with neighboring edges
            visited.add(vertex)
        

    # adding func to allow for variation in operation application
    def dft_recursive(self, starting_vertex, func = self.print_path):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check starting vertex is valid
        if starting_vertex not in self.vertices:
            return f'Staring vertex {starting_vertex} not found!'

        # load neighbors
        neighbors = self.get_neighbors(starting_vertex)

        # check if vertex has neighbors
        if neighbors:
            for neighbor in neighbors:
                   func(neighbor)
                   self.dft_recursive(neighbor)


        
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        queue = Queue()
        
        # add current vertex to queue
        queue.enqueue([starting_vertex])

        while queue:
            vertex = queue.dequeue



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

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
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
