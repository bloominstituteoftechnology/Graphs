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
        # enqueue the starting node
        q.enqueue(starting_node)
        # while the queue is not empty
        while len(q.queue) > 0:
            # dequeue a node from the queue
            node = q.dequeue()
            # mark it as visited
            if node not in visited:
                visited.add(node)
                print('visited:', visited)
            # enqueue all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited:
                    q.enqueue(child)

    # def dfs(self, starting_node):
    #     # create a stack
    #     s = Stack()
    #     visited = set()
    #     # push the starting node
    #     s.Push(starting_node)
    #     # while the stack is not empty
    #         # pop a node from the stack
    #         # mark it as visited
    #         # push all of its children that have not been visited

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
    #     q.Enqueue(starting_v)
    #     #while the queue is not empty, 
    #         #dequeue a vertex from the queue 
    #         #mark it as visited 
    #         # ---*---- if node == target_node: return true
    #         #enqueue all of it's children that have not been visited 
    #     #return false 

