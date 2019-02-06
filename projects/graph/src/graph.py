"""
Simple graph implementation
"""
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
        self.vertices = {} #nodes
        # vertex: edges

    def add_vertex(self, vertex): #creates nodes
        self.vertices[vertex] = set()

    def add_edge(self, from_vertex, to_vertex): #draws lines between nodes that exist
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)
            self.vertices[to_vertex].add(from_vertex)
            # undirected graph
        else: 
            raise IndexError(f'{from_vertex} and {to_vertex} are not in this graph')
    def add_directed(self, v1, v2):
        # lines that go in one direction between nodes
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError(f'{v2} and {v2} are not in this graph')

    def breadth_first_traversal(self, start_vertex):
        #empty Queue FIFO
        queue = Queue()
        #keeps track of order to be printed at the end
        visited = [] #must be an array b/c sets aren't ordered
        #add start_vertex to Queue
        queue.enqueue(start_vertex) #{3}
        # while Queue.length > 0
        while queue.size():
            #dequeue first item in queue
            #mark node as visited
            vertex = queue.dequeue() #current vertex #queue {}
            if vertex not in visited:
                visited.append(vertex) # visted = [3, 0, 4, 1, 5]
                #if neighbor, add to the queue
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor) #add neighbor queue {}
        return visited

    def depth_first_traversal(self, start_vertex):
        stack = Stack() # FILO
        visited = []
        stack.push(start_vertex)
        while stack.size(): # stack
            vertex = stack.pop() #value of current node {}
            if vertex not in visited: # [3, 4, 5, 0, 1]
                visited.append(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    stack.push(neighbor)
        return visited

    def depth_first_recursive(self, start_vertex, visited = None):
        if visited is None:
            visited = []  #set()
        visited.append(start_vertex)
        # visited.add(start_vertex)
        # print(start_vertex)
        for neighbor in self.vertices[start_vertex]:
            if neighbor not in visited:
                self.depth_first_recursive(neighbor, visited) 
                #base case is when no more neigbors/children nodes left
        return visited

    def breadth_first_search(self, start_vertex, destination):
        queue = Queue()
        visited = []
        queue.enqueue(start_vertex)
        while queue.size() > 0: # base case
            vertex = queue.dequeue() # leads to base case
            if vertex not in visited:
                visited.append(vertex)
                if vertex == destination:
                # if current node/vertex is the target destination
                # return visited and the destination should be the last node
                    print(f'{vertex} is at the target with BFS')
                    return visited
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)
        print(f'{destination} vertex is not found in this graph')

    def depth_first_search(self, start_vertex, destination):
        stack = Stack()
        visited = []
        stack.push(start_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                if vertex == destination:
                    print(f'{vertex} is at the target with DFS')
                    return visited
                for neigbor in self.vertices[vertex]:
                    if neigbor not in visited:
                        stack.push(neigbor)
        print(f'{destination} vertex is not found in this graph')          
