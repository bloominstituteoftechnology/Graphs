from util import Queue, Stack

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
            # print("Error:vertex does not exist")
            raise ValueError("vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        add an undirected edge to the graph
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
            # print("Error: Vertex does not exist")
            raise ValueError("vertex does not exist")

    

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO

        # Create a queue
        q = Queue()
        # Enequeue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices 
        visited = set()
        # While the queue is not empty...
        while q.size() > 0: 
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited...
            if v not in visited: 
            # if it hasn't been visited...
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
        # pass  # TODO
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
            # Check if it's been visited...
            if v not in visited: 
            # if it hasn't been visited...
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all its neighbors onto the stack
                for neighbor in self.get_neighbors(v): 
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None: 
            visited = set()
        #check if the node has been visited
        if starting_vertex not in visited: 
        #if not....
            visited.add(starting_vertex)
            print(starting_vertex)
        #Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        #

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        bfs_q = Queue()
        # Enqueue A PATH TO the starting vertex
        bfs_q.enqueue( [starting_vertex] )
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while bfs_q.size() > 0: 
            # Dequeue the first PATH
            path = bfs_q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            last_vertex = path[-1]
            # Check if it's been visited
            if last_vertex not in visited: 
            # If it hasn't been visited...
                # Mark it as visited
                visited.add(last_vertex)
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
                if last_vertex == destination_vertex: 
                    return path 
                    # copied_path = path 
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                    bfs_q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #create a stack
        s = Stack()
        #add starting vertex to the stack 
        s.push( [starting_vertex] )
        #create a set to store visted vertexes 
        visited = set()
        #while the stack is not empty...
        while s.size() > 0: 
            #pop the first path
            path = s.pop()
            #grab the vertex
            v = path[-1]
            if v not in visited: 
                visited.add(v)
                if v == destination_vertex: 
                    return path
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
        if visited is None: 
            visited = set()
        if path is None: 
            path = []
        if starting_vertex not in visited: 
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex: 
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None: 
                    return new_path
        return None


    def earliest_ancestor(ancestors, starting_node):

        q = Queue()
        q.enqueue( [starting_node] )

        earliest_ancestor = None
        longest_path = []
        visited = set()

        while q.size() > 0: 
            path = q.dequeue()
            current_vertex = path[-1]

            if len(path) > len(longest_path):
                longest_path = path
            if current_vertex not in visited: 
                for neighbor in graph.get_neighbors(current_vertex): 
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        if len(longest_path) > 1:
            print("longest path")
            return longest_path[-1]
        else: 
            return -1 

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
    print("this is dft recursive")

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
    
built_in_test = [(1, 3),(2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]