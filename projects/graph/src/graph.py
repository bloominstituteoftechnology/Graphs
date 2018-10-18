"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import collections

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node, visited=None):
        """
        Depth first traversal using recursion
        """
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited

    # Mark the node as visited, then for each child that hasn't been visited, call DFT() on that node.


    # def bft(self, starting_node):
    #     """
    #     Breadth first traversal using a queue
    #     """
    #     # create an empty queue
    #     visited, queue = set(), collections.deque([starting_node]) # Put starting vert in the queue
    #     while queue:
    #         vertex = queue.popleft() # Remove the first node from the queue...
    #         if vertex not in visited: # If it has not been visited yet,...
    #             visited.add(vertex) # Mark it as visited....
    #             print(vertex)
    #             for neighbor in self.vertices[vertex].edges: # Then put all it's children in the back of the queue
    #                 if neighbor not in visited:
    #                     queue.append(neighbor)
    #     return visited

    def bft(self, starting_node):
        visited = []
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        while q.size() > 0:  # whlie queue is not empty...
            dequeued = q.dequeue() # Dequeue the first element
            visited.append(dequeued)  # Mark it as visited
            print(dequeued)
            for edge in self.vertices[dequeued].edges:  #For each child
                if edge not in visited:  # If it hasn't been visited
                    q.enqueue(edge)  # Add it to the back of the queue
        return visited



    # def dft_s(self, starting_node):
    #     visited = []
    #     # create an empty stack
    #     s = Stack()
    #     # Put starting vert on top of the stack
    #     s.push(starting_node)
    #     while s.size() > 0:  # whlie stack is not empty...
    #         destacked = s.pop() # Pop the first element
    #         visited.append(destacked)  # Mark it as visited
    #         print(destacked)
    #         for edge in self.vertices[destacked].edges:  #For each child
    #             if edge not in visited:  # If it hasn't been visited
    #                 s.push(edge)  # Add it to the top of the stack
    #     return visited

    def dft_s(self, starting_node):
        s = Stack()
        s.push(starting_node)
        visited = []
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    s.push(edge)

    def bfs(self, starting_node, target_node):
        visited = []
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        while q.size() > 0:  # whlie queue is not empty...
            dequeued = q.dequeue() # Dequeue the first element
            visited.append(dequeued)  # Mark it as visited
            print(dequeued)
            if dequeued == target_node:
                return True
            for edge in self.vertices[dequeued].edges:  #For each child
                if edge not in visited:  # If it hasn't been visited
                    q.enqueue(edge)  # Add it to the back of the queue
        return False

    # Instead of storing just nodes in our queue, we store an entire path
    def bfs_path(self, starting_node, target_value):
        q = Queue()  # Create an empty Queue
        q.enqueue([starting_node]) # Put the first node in the queue as a path
        visited = []
        while q.size() > 0: # Then, while the queue is not empty
            path = q.dequeue()  # Dequeue the first path in the queue
            v = path[-1]  # Get the current vertex (the last element in the path)
            if v not in visited:  # If that vertex has not been visited...
                if v == target_value:  # Check if it's the target value
                    return path
                visited.append(v) # ...mark as visited...
                for next_vert in self.vertices[v].edges:  # Then put all the children in the queue
                    new_path = list(path)
                    new_path.append(next_vert)  # ...as a path.
                    q.enqueue(new_path)
        return None


    def dfs(self, starting_node, target_node, visited=None):
        """
        Depth first traversal using recursion
        """
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        print(starting_node)
        if starting_node == target_node:
            return True
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                if self.dfs(node, target_node, visited):
                    return True
        return False

    def dfs_path(self, start_vert, target_value, visited=None, path=None):
        # Initialize starting visited/path lists
        if visited is None:
            visited = []
        if path is None:
            path = []
        # Mark the first node as visited
        visited.append(start_vert)
        print(start_vert)
        # Add the node to the path
        extended_path = list(path)
        extended_path.append(start_vert)  # ...as a path.
        # Return the path if we find our target node
        if start_vert == target_value:
            return extended_path
        # Otherwise, for each child
        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:  # If it hasn't been visited yet
                # Call dfs_path on the children
                new_path = self.dfs_path(child_vert, target_value, visited, extended_path)
                # Return the path if it's valid
                if new_path:
                    return new_path
        return None



class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"