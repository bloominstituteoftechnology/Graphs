"""
Simple graph implementation
"""
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # v is the vertex
    def add_vertex(self, v):
        if v not in self.vertices.keys():
            self.vertices[v] = set()
        else:
            print(f'{v} vertex already exists, vertex was not added.')
    
    # v1 is vertex1, v2 is vertex2
    def add_edge(self, v1, v2):
        if (v1 and v2) in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        elif not v1 in self.vertices:
            print(f'There is no {v1} vertex, edge was not added.')
        else:
            print(f'There is no {v2} vertex, edge was not added.')
            
    # Breadth-First Traversal
    def bft(self, starting_node):
        # create a queue
        q = Queue()
        visited = set()
        # visited = []
        # enqueue the starting node
        q.enqueue(starting_node)
        # while the queue is not empty
        while len(q.queue) > 0:
            # dequeue a node from the queue
            node = q.dequeue()
            # mark it as visited
            visited.add(node)
            print('visted from queue:', visited)
            # if node not in visited:
            #     visited.append(node)
            #     print('visted from queue:', visited)
            # enqueue all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited:
                    q.enqueue(child)

    # Depth-First Traversal
    def dft(self, starting_node):
        # create a stack
        s = Stack()
        visited = set()
        # visited = []
        # push the starting node
        s.push(starting_node)
        # while the stack is not empty
        while len(s.stack) > 0:
            # pop a node from the stack
            node = s.pop()
            # mark it as visited
            visited.add(node)
            print('visted from stack:', visited)
            # if node not in visited:
            #     visited.append(node)
            #     print('visted from stack:', visited)
            # push all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited:
                    s.push(child)

    # def dft_recursion(self, starting_node, visited=None):
    #     if visited is None:
    #         visited = set()
    #     #if the node has not been visited 
    #         #mark node as visited
    #         #call dft_recursion on all children 
    #         dft_recursion(child_node, visited)

    # def bfs_search(self, starting_node, target_node):
    #     #create queue
    #     q = Queue()
    #     visited = set()
    #     #enqueue the starting vertex
    #     q.Enqueue(starting_node)
    #     #while the queue is not empty, 
    #         #dequeue a vertex from the queue 
    #         #mark it as visited 
    #         # ---*---- if node == target_node: return true
    #         #enqueue all of it's children that have not been visited 
    #     #return false 



