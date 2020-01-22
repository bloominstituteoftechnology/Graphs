
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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
                    return path  # Return path we've built so far
                # Add to visited
                visited.add(vertex)
                # Get neighbors for each edge in item
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
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]  # Add starting_vertex to path
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:  # Catch if target does not exist
                    return new_path
        return None  # Catch if target does not exist