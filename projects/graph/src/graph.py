"""
Simple graph implementation
"""
from collections import deque

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # below: a dictionary mapping vertex labels to edges
        self.vertices = {}

    # ---- DAY 1 goal -------
    # below: methods to add to/build the graph

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            print(f"No {vertex} vertex found")

    def bf_traversal(self, starting_v):
        # FUNCTION RETURNS : "prints the vertices in the order they were visited"
        #create queue - using built in library deque
        q = deque()
        # Enqueue starting vertex
        q.append(starting_v)
        visited = []

        #while the queue is not empty, 
        while q:
            #dequeue a vertex from the queue 
            current_v = q.popleft()
            #...and mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
                #enqueue all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    q.append(edge)

        print(visited)
       
    def df_traversal(self, starting_v):
        # FUNCTION RETURNS : "prints the vertices in the order they were visited"
        #create stack
        s = deque()
        #push starting vertex
        s.append(starting_v)
        visited = []
        #while the stack is not empty, 
        while s:
            #pop a vertex from the stack
            current_v = s.pop()
            #mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
            #push all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    s.append(edge)

        print(visited)

    def dft_stack():
        pass

    def dft_recursion(self, starting_v, visited=None):
        if visited is None:
            visited = set()
        #if the node has not been visited 
            #mark node as visited
            #call dft_recursion on all children 
            dft_recursion(child_v, visited)
        pass

     # ---- DAY 2 -------
    def bfs_search(self, starting_v, target_v):
        # FUNCTION RETURNS: "the shortest path from the start node to the destination node."
        #create queue
        q = Queue()
        visited = set()
        #enqueue the starting vertex
        q.Enqueue(starting_v)
        #while the queue is not empty, 
            #dequeue a vertex from the queue 
            #mark it as visited 
            # ---*---- if node == target_node: return true
            #enqueue all of it's children that have not been visited 
        #return false 
        pass

    def dft_search():
        pass

