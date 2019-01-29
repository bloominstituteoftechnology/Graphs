"""
Simple graph implementation
"""
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0) # O(n), to be optimal better to use linked list
        # if self.size() > 0:
        #     return self.queue.pop(0)
        # else:
        #     return None
    
    # def size(self):
    #     return len(self.queue)

    # class Vertex:
    #     def __init__(self, value):
    #         self.value = value
    #         self.color = 'white'
    #         self.edge = set()

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
        # if self.size() > 0:
        #     return self.stack.pop()
        # else:
        #     return None

    # def size(self):
    #     return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # v is the vertex
    def add_vertex(self, v):
        if v not in self.vertices.keys():
            self.vertices[v] = set()
        else:
            raise IndexError(f'Vertex {v} already exists, vertex was not added.')
    
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

    # Depth-First Traversal using Recursion
    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_node)
        print('visted from stack recursion:', visited)
        for child in self.vertices[starting_node]:
            # call dft_r on all unvisisted children  
            if child not in visited:
                self.dft_r(child, visited)
        

    # Breadth-First Search
    def bfs(self, starting_node, target_node):
        #create queue
        q = Queue()
        visited = set()
        #enqueue the starting vertex
        q.enqueue(starting_node)
        #while the queue is not empty, 
        while len(q.queue) > 0:
            #dequeue a vertex from the queue 
            node = q.dequeue()
            # if node == target_node: return true
            if node not in visited:
                #mark it as visited 
                if node == target_node:
                    return True
                print('visited from bfs', visited)
                visited.add(node)
            #enqueue all of it's children that have not been visited 
            for next_node in self.vertices[node]:
                if next_node not in visited:
                    q.enqueue(next_node)
        # return false
        return False



