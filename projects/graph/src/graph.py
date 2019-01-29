"""
Simple graph implementation
"""
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0) # O(n), to be optimal better to use linked list
        else:
            return None
    
    def size(self):
        return len(self.queue)

    # # Adds color to vertexes
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

    def add_vertex(self, v):
        if v not in self.vertices.keys():
            self.vertices[v] = set()
        else:
            raise IndexError(f'Vertex {v} already exists, vertex was not added.')
    
    # Directional Edge
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndentationError(f'There is no {v1 if not self.vertices else v2} vertex, edge ({v1},{v2}) was not added.')
    
    # Uniderectional Edge
    def add_undirected_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndentationError(f'There is no {v1 if not self.vertices else v2} vertex, edge ({v1},{v2}) was not added.')    
            
    # Breadth-First Traversal
    def bft(self, starting_node):
        # create a queue
        q = Queue()
        visited = set()
        # visited = [] # the array metod
        # enqueue the starting node
        q.enqueue(starting_node)
        # while the queue is not empty
        while q.size() > 0:
            # dequeue a node from the queue
            node = q.dequeue()
            # mark it as visited
            if node not in visited:
                print('visted from bft:', node)
                visited.add(node)
                # visited.append(node) # the array metod
            # enqueue all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited:
                    q.enqueue(child)

    # Depth-First Traversal
    def dft(self, starting_node):
        # create a stack
        s = Stack()
        visited = set()
        # visited = [] # the array metod
        # push the starting node
        s.push(starting_node)
        # while the stack is not empty
        while s.size() > 0:
            # pop a node from the stack
            node = s.pop()
            # mark it as visited
            if node not in visited:
                print('visted from dft:', node)
                visited.add(node)
                # visited.append(node) # the array metod
            # push all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited:
                    s.push(child)

    # Depth-First Traversal using Recursion
    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        print('visted from dft_r:', starting_node)
        visited.add(starting_node)
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
        while q.size() > 0:
            #dequeue a vertex from the queue 
            node = q.dequeue()
            # if that node has not been visited..
            if node not in visited:
                #mark it as visited 
                if node == target_node:
                    return True
                print('visited from bfs:', node)
                visited.add(node)
                #enqueue all of its children that have not been visited 
                for next_node in self.vertices[node]:
                        q.enqueue(next_node)
        # return false
        return False

    # Depth-First Search
    def dfs(self, starting_node, target_node):
        #create stack
        s = Stack()
        visited = set()
        #push the starting vertex
        s.push(starting_node)
        #while the stack is not empty, 
        while s.size() > 0:
            #pop a vertex from the stack 
            node = s.pop()
            # if that node has not been visited..
            if node not in visited:
                #mark it as visited 
                if node == target_node:
                    return True
                print('visited from bfs:', node)
                visited.add(node)
                #push all of it's children that have not been visited 
                for next_node in self.vertices[node]:
                        s.push(next_node)
        # return false
        return False

    
    # Breadth-First Search Path
    def bfs_p(self, starting_node, target_node):
        # create queue
        q = Queue()
        visited = []
        # enqueue starting vertex
        q.enqueue(starting_node)
        # while queue is not empty
        while q.size() > 0:
            # path is the first duplicate path from the queue
            path = q.dequeue()
            print('path', path)
            # node is the last index from the path
            node = path[-1]
            print('node', node)
            # if that node has not visited...
            if node not in visited:
                # mark it as visited by returning shortest path
                if node == target_node:
                    return path
                visited.append(node)
                print('visited', visited)
                # enqueue all of its children that have not been visited
                for children in self.vertices[node]:
                        # creates duplicate list
                        duplicate_path = list(path)
                        # adds child(ren) to duplicate path
                        duplicate_path.append(children)
                        print('duplicate_path', duplicate_path)
                        # add duplicate list to queue
                        q.enqueue(duplicate_path)
        return None



