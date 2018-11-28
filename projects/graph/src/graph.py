"""
Simple graph implementation compatible with BokehGraph class.
"""

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
    
#     #add a node point
#     def add_vertex(self, vertex_id, vertices):
#         self.vertices[vertex_id] = vertices(vertex_id)

#     #add connections between nodes, if connection is possible
#     def add_edge(self, vert1, vert2):
#         if vert1 in self.vertices and vert2 in self.vertices:
#             self.vertices[vert1].edges.add(vert2)
#             self.vertices[vert2].edges.add(vert1)
#         else:
#             raise IndexError("That vertex does not exist!")

#     #making a one way street between nodes
#     def add_directed_edge(self, vert1, vert2):
#         if vert1 in self.vertices:
#             self.vertices[vert1].edges.add(vert2)
#         else:
#             raise IndexError("That vertex does not exist!")

    # #### Recursion HMWk ####
    #     # DFT Recursion

    #     def dft_r(self, node):
    #         # Mark starting_node as visited
    #         # Then call dft_r on each child
    #         stack = Stack()
    #         visited_list = set()
    #         visited_list.add(node)
    #         for child in self.vertices[node].edges:
    #             dft_r(child)
#####################################################################################

###### Lecture Notes- Solution ######
class Queue:
    def __init__(self):
        self

class Graph:
    def __init__(self):
        #we establish an empty dictionary
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    ##### BFT is horizontal (Queue), DFT is verticle (Stack) ####
    #DFT is like navigating a maze, you draw a line until you hit a dead end then you
    #back track, until there are no more paths to follow
    #BFT is the shortest to find an item

    def dft(self, starting_node):
        #Create an empty Stack
        s = Stack()
        #Create an empty visited list
        visited = set()
        #Add the start node to the stack
        s.push(starting_node)
        #while the Stack is not empty...
        while s.size() > 0:
            #remove the first node from the Stack
            node = s.pop()
            #If it hasn't been visited
            if node not in visited:
                #Mark it as visited
                print(node)
                visited.add(node)
                #then put all its children in the queue
                for child in self.vertices[node].edges:
                    print(f" add child: {child}")
                    s.push(child)

    def bft(self, starting_node):
        #Create an empty Queue
        q = Queue()
        #Create an empty visited list
        visited = set()
        #Add the start node to the queue
        q.enqueue(starting_node)
        #while the Queue is not empty...
        while q.size() > 0:
            #remove the first node from the Queue
            node = q.dequeue()
            #If it hasn't been visited
            if node not in visited:
                #Mark it as visited
                print(node)
                visited.add(node)
                #then put all its children in the queue
                for child in self.vertices[node].edges:
                    print(f" add child: {child}")
                    q.enqueue(child)

    #Another way to do this BFT                
#     class Queue:
    #   def __init__(self):
    #     self.size = 0
    #     self.storage = []

    #   def enqueue(self, item):
    #     self.storage.append(item)
    #     print(f'{item} added to q')
    
    #   def dequeue(self):
    #     if len(self.storage) == 0:
    #       return None
    #     else:
    #       return self.storage.pop(0)

    #   def len(self):
    #     if len(self.storage) == 0:
    #       return 0
    #     else:
    #       return len(self.storage)


    # BF Search

    def bfs(self, starting_node, destination_node):
        #Create an empty Queue
        q = Queue()
        #Create an empty visited list
        visited = set()
        #Add the start node to the queue
        q.enqueue(starting_node)
        #while the Queue is not empty...
        while q.size() > 0:
            #remove the first node from the Queue
            node = q.dequeue()
            #If it hasn't been visited
            if node not in visited:
                #Mark it as visited
                print(node)
                if destination_node == node:
                    return True
                visited.add(node)
                #then put all its children in the queue
                for child in self.vertices[node].edges:
                    print(f" add child: {child}")
                    q.enqueue(child)

    #Lecture Solution
    #DFT Recursion
    #why do we set the default of visited to None? 

    def dft_r(self, starting_node, visited=None):
        # Mark starting_node as visited
        # Then call dft_r on each child
        if visited is None:
            visited = set()
        visited.add(starting_node)
        for child in self.vertices[starting_node].edges:
            
        
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()