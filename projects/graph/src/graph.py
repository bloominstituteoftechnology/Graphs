"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
    #day 1
    def bf_traversal(self, starting_v):
        #create queue
        q = Queue()
        visited = set()
        #enqueue the starting vertex
        q.Enqueue(starting_v)
        #while the queue is not empty, 
            #dequeue a vertex from the queue 
            #mark it as visited 
            #enqueue all of it's children that have not been visited 
    
    def df_traversal(self, starting_v):
        #create stack
        s = Stack()
        visited = set()
        #push starting vertex
        s.Push(starting_v)
        #while the stack is not empty, 
            #pop a vertex from the stack
            #mark it as visited 
            #push all of it's children that have not been visited 
    
    def dft_stack():
    
    def dft_recursion(self, starting_v, visited=None):
        if visited is None:
            visited = set()
        #if the node has not been visited 
            #mark node as visited
            #call dft_recursion on all children 
            dft_recursion(child_v, visited)
    
    #day 2
    def bfs_search(self, starting_v, target_v):
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
    
    
    def dft_search():

