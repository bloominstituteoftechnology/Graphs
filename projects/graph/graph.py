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
        # Make a set to store vertices we've visited
        visited = set()
        # While q is not empty
        while queue.size() > 0:
            # dequeue first path
            vertex = queue.dequeue()
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
                # Add each item to back of queue
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

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue
        queue = Queue()
        # enqueue a path to starting vertex id
        queue.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While q is not empty
        while queue.size() > 0:
            # Dequeue first path
            path = queue.dequeue()
            # Grab last vertex from the path
            vertex = path[-1]
            # If that vertex has not been visited
            if vertex not in visited:
                # Check if it's the target...
                # If it is, return the path
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                visited.add(vertex)
                # For each edge in item...
                # Add a path to its neighbors to the back of queue
                for next_vert in self.get_neighbors(vertex):
                    # Copy path
                    new_path = list(path)
                    # append neighbor to the back of queue
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty stack 
        stack = Stack()  # Stack imported above
        # Add starting point as first path in stack 
        stack.push([starting_vertex])
        # Create set to store visited vertices
        visited = set()
        # stack is not empty
        while stack.size() > 0:
            # Remove path at top of stack
            path = stack.pop()  
            # Grab last vertex from path
            vertex = path[-1]  
            # If vertex has not been visited...
            if vertex not in visited:
                # Check if it's the target...
                # If so, return path
                if vertex == destination_vertex:
                    return path  # Return path we've built so far
                # Mark it as visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                # by adding a path to neighbors to top of stack
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid 'pass by reference' bug
                    new_path = list(path)  # Makes copy rather than reference
                    new_path.append(next_vert)  # Add new vertex to copy
                    stack.push(new_path) 


    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if visited is None:
            # Initialize visited set
            visited = set()
        if path is None:
            # Initialize path as array b/c needs to be ordered
            path = []
        # Add starting_vertex to path
        visited.add(starting_vertex)
        # Add starting_vertex to path
        path = path + [starting_vertex]  
        # If at target, return path
        if starting_vertex == target_value:
            return path
        # Otherwise, call DFS_recursive on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_value, visited, path)
                if new_path:  # Catch if target does not exist
                    return new_path
        # for child_vert in self.vertices[starting_vertex]:
        #     if child_vert not in visited:
        #         new_path = self.dfs_recursive(child_vert, target_value, visited, path)
        #         if new_path:  # Catch if target does not exist
        #             return new_path
        return None  # Catch if target does not exist

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
    print("Printing graph.vertices")
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
    print("Running dft_recursive")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running BFS")
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running DFS")
    print(graph.dfs(1, 6))
    print("Running dfs_recursive")
    # print(graph.dfs_recursive(1, 6))
