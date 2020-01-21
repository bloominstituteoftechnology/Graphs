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
        If both exist, add a connection from v1 to v2.
        If not, raise an error via Python exception.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

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
        # Create queue
        queue = Queue()
        # Put the starting point in it
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in q
        while queue.size() > 0:
            # Pop first item
            vertex.queue.dequeue()
            # ALTERNATE for queue ONLY: check first
            # queue[0]  
            # If not visited
            if vertex not in visited:
                # Do the thing! (e.g. stop searching)
                print(vertex)
                # # ALTERNATE for queue ONLY: print(queue[0])
                # Add to visited
                visited.add(vertex)
                # ALTERNATE for queue ONLY: visited.add(queue[0])
                # For each edge in item
                for next_vert in self.get_neighbors(vertex):
                    ## ALTERNATE for queue ONLY: for next_vert in self.get_neighbors(queue[0])
                    # Add edge to q
                    queue.enqueue(next_vert)
                    # ALTERNATE for queue ONLY: queue.dequeue  # Get rid of it here
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack 
        stack = Stack()  # Stack imported above
        # Put the starting point in it
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in stack
        while stack.size() > 0:
            # Pop first item
            vertex = stack.pop()
            # If not visited
            if vertex not in visited:
                # DO THE THING! (e.g. stop searching)
                print(vertex)
                # Add to visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                for next_vert in self.get_neighbors(vertex):
                    # Add edge to stack
                    stack.push(next_vert)

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
        # Create queue
        queue = Queue()
        # Put the starting point in it
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in q
        while queue.size() > 0:
            # Pop first item
            path = queue.dequeue()
            vertex = path[-1]
            # If not visited
            if vertex not in visited:
                # Do the thing! 
                if vertex == destination_vertex:
                    return path
                # Add to visited
                visited.add(vertex)
                # For each edge in item
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create stack 
        stack = Stack()  # Stack imported above
        # Put the starting point in it
        # 'enstack' a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in stack
        while stack.size() > 0:
            # Pop first item
            path = stack.pop()  # Path is first item in stack
            vertex = path[-1]  # Vertex is last item in path
            # If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # DO THE THING! 
                    return path  
                # Add to visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid 'pass by reference' bug
                    new_path = list(path)  # Makes copy rather than reference
                    new_path.append(next_vert)  # Add new vertex to copy
                    stack.push(new_path) 


    def dfs_recursive(self, starting_vertex):
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
    print("graph vertices")
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
    print("Running bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Running dft")
    graph.dft(1)
    print("Running dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running dfs")
    print(graph.dfs(1, 6))
    print("Running dfs recursive")
    print(graph.dfs_recursive(1, 6))
