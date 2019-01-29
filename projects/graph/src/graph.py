"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex, value):
        # Add edge as a value to the vertex
        self.vertices[vertex].add(value)
        # Add vertex as a value to the edge
        self.vertices[value].add(vertex)
    
    def bfs(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

        return visited

    def dft(self, starting_node):
    # Initialize a Stack instance
    s = Stack()
    visited = []
    # Add starting node
    s.push(starting_node)
    # While the stack isn't empty
    while len(s.storage) > 0:
        # Pop a node from the stack
        node = s.pop()
        # Mark it as visited
        visited.append(node)
        # Push all of its children that have not been visited
        for child in self.vertices[node]:
            if child not in visited:
                s.push(child)

    return visited

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = []
        # If the node has not been visited
        if starting_node not in visited:
            visited.append(starting_node)
            # Mark the node as visited
            # Recursion through children
            for child in self.vertices[starting_node]:
                if child not in visited:
                    self.dft_r(child, visited)
        return visited
    
    ## DFS below ##

    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,v): 

        # A helper fxn used by dfs method 
        def DFSUtil(self,v,visited): 
            # Mark the current node as visited and print it 
            visited[v]= True
            print (v) 
            # Recursively do this for all the vertices adjacent to this vertex 
            for i in self.graph[v]: 
                if visited[i] == False: 
                    self.DFSUtil(i, visited)

        # Mark all the vertices as not visited 
        visited = [False]*(len(self.graph)) 
  
        # Call the recursive helper function to print 
        # DFS traversal 
        self.DFSUtil(v,visited) 

class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)

class Stack:
    def __init__(self):
        pass  # TODO
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()