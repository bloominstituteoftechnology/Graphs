import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self, value):
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
        self.stack.push(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {} # dictionary

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
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
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected

    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected

    def bfs(self, starting_node, target_node): # breadth first search (NOT RECURSIVE)- finds an element and returns true
        queue = [starting_node]
        visited = [starting_node]
        while len(queue) > 0:
            print(f"queue: { queue }")
            cur_node = queue.pop(0)
            if cur_node == target_node:
                return True
            for edge in self.vertices[cur_node].edges:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)
        print(f"visited: { visited }")
        return False

    def bft(self, starting_node): # breadth first traversal
        queue = [starting_node]
        visited = [starting_node]
        while len(queue) > 0:
            print(f"queue: { queue }")
            cur_node = queue.pop(0)
            for edge in self.vertices[cur_node].edges:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)
        print(f"visited: { visited }")
        return visited

    def bfs_path(self, starting_node, target_node): # BFS PATH NOT RECURSIVE
        q = []
        q.append([starting_node])
        visited = []
        while len(q) > 0:
            path = q.pop(0)
            v = path[-1] # get the current vertex (the last element in the path)
            if v not in visited:
                print(path)
                if v == target_node:
                    return path
                visited.append(v) #...marked as visited
                for edge in self.vertices[v].edges:
                    new_path = list(path)
                    new_path.append(edge) #...as a path
                    q.append(new_path)
        return None
            
    def dft(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            visited = []
        visited.append(starting_node)
        print(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for edge in self.vertices[starting_node].edges:
            if edge not in visited:
                self.dft(edge, visited)
        return visited

    def dfs(self, starting_node, target_node, visited=None): # Depth First Search Recursive
        if visited is None:
            visited = []
        visited.append(starting_node)
        if starting_node == target_node:
            return True
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                if self.dfs(node, target_node, visited):
                    return True
        return False

    def dfs_path(self, starting_node, target_node, visited=None, path=None):
        # Initialize starting visited/path lists
        if visited is None:
            visited = []
        if path is None:
            path = []
        # Mark the first node as visited
        visited.append(starting_node)
        # Add the node to the path
        extended_path = path + [starting_node]
        print("Extended path", extended_path)
        # Return the path if we find our target node
        if starting_node == target_node:
            return extended_path
        # Otherwise, for each child ...
        for node in self.vertices[starting_node].edges:
            if node not in visited: # If it hasn't been visited yet
                # Call dfs_path on the children
                new_path = self.dfs_path(node, target_node, visited, extended_path)
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
        if y is None:
            self.y = random.random() * 10 - 5 

    def __repr__(self):
        return f"{self.edges}"