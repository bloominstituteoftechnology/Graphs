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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("error: vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
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
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

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
        edges = self.get_neighbors(starting_vertex)
        if len(edges) == 0:
            return
        else:
            for edge in edges:
                if edge not in visited:
                    self.dft_recursive(edge, visited)
                else:

                    return
        #dft_recursive(1, set())
        #visited = set(1,2,3)
        #edges = set(2)
        #dft_recursive(2, set(1))
        #visited = {1, 2,3}
        #edges= set(3,5)
        #dft_recursive(3, {1,2})
        #visited = {1, 2, 3}
        #edges = set(4)
        # dft_recursive(4,{1,2,3})
        #visited = set(1,2,3,4)
        #edge = set(3)

    # Stack is depth first [1,2,3,4] always removing from the end FILO LIFO
    # QUEUE is breadth first [2,1]   always removing from the end FIFO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # pass  # TODO
        # (1,6)
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:  # while the queue size is greater than zero
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:  # while the queue size is greater than zero
            current_path = stack.pop()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        stack.push(path_copy)

    # dfs_recursive(1,6)         (2, 6, {1}, [1])        (3, 6, {1,2})
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # pass  # TODO
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # {1}                      {1,2}                    {1,2,3}
        visited.add(starting_vertex)
        # path = [1]               [1, 2]                   [1,2,3]
        path = path + [starting_vertex]
        # 1 == 6 / False           2 == 6 / False           3 == 6 / False
        if starting_vertex == destination_vertex:
            # [1,2,4,6]
            return path
        # self.vertices[1] = {2}   {3, 4}                   {5}
        for vert in self.vertices[starting_vertex]:
            # 2 not in [1] / True       3 not in [1, 2] /True   5 not in [1,2, 3]
            if vert not in visited:
                print("this is the path, ", path)
                final_path = self.dfs_recursive(
                    vert, destination_vertex, visited, path)
                # [1,2,4,6]
                if final_path:
                    return final_path
        else:
            return None
