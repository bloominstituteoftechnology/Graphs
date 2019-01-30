from collections import deque
"""
Simple graph implementation
"""
class Queue():
    __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    #big O(n) b/c have to move everything (n) over. n is prob small enough not to matter for now. more readable might be more important. 
    def dequeue(self):
        if self.size > 0:
            self.queue.pop()
        else:
            return None
    def size(self):
        return(len(self.queue))

class Stack():
    __init__(self):
        self.stack = []
        #these are big O of 1
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size > 0:
            self.stack.pop()
        else:
            return None
    def size(self):
        return(len(self.stack))

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        #if vertex in indices
        if v1 in vertices and v2 in vertices:
            self.vertices[v1].add[v2]
            #for undirected edge add second
            self.vertices[v2].add[v1]
            return 
        else: 
            print("At least one vertex does not exist.")
            return 

    def bft(self, s):
        #create a queue
        q = deque()
        visited = set()
        #mark the first node as visited
        #enqueue the starting node
        q.append(s)
        #visited[s] = True
        #while the queue is not empty
        while q:
            #dequeue a node from the queue
            dequeued = q.pop(0)
            #mark that node as visited
            if dequeue not in visited:
                visited.add(dequeued)
            #enqueue all of its children that have not already been added to queue
            for i in self.vertices(dequeued):
                if i not in visited:
                    q.append(i)

        return visited

    def dft(self, starting_node):
        #create a queue
        s = Stack()
        visited = set()
        #push the starting node
        s.push()
        #while the node is not empty
        while s:
            #pop a node from the stack
            popped = s.pop(0)
            #mark it as visited
            if popped not in visited:
                visited.append(popped)
            #push all of the children that have not been visited. 
            for i in self.vertices(popped):
                if i not in visited: 
                    s.append(i)

    def dft_recursive(self, starting_vertex, visited=None):
        pass

    def bfs(self, starting_vertex, target):
        #create a queue
        q = Queue()
        visited = set()
        #enqueue starting vertex
        q.enqueue(starting_vertex)
        #while the queue is not empty
        while q: 
            #dequeue a vertex from the queue
            dequeued = q.dequeue()
            #if that vertex has not been visited
            if dequeued not in visited:
                #mark it as visited
                if dequeued == target:
                    return True
                print(dequeued)
                visited.add(dequeued)
                #enqueue all of its children
                for children in self.vertices(dequeued):
                    q.enqueue(children)
        return False



