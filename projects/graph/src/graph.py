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
                    # print(f" add child: {child}")
                    s.push(child)
    
    #DFT Recursion
    #why do we set the default of visited to None? 

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
            # Mark startig_node as visited
        print(starting_node)
        visited.add(starting_node)
        for child in self.vertices[starting_node].edges:
            # Mark starting_node as visited
            if child not in visited:
                # call dft_r on that child
                self.dft_r(child, visited)


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
                    # print(f" add child: {child}")
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
    # visited = [1, 2, 3, 4]
    # queue = [[1,2,3,5], [1,2,4,6], [1,2,4,7]]
    # we go down each path starting with just 1, then 1,2, then 1,2,3, but that is just one path
    # we get through all of the paths, looking at the last path item in queue, if it hasn't be
    # visited then it is marked as visited by being pushing it into the visited list, 
    # all visited items are ignored.

    def bfs(self, starting_node, destination_node):
        #Create an empty Queue
        q = Queue()
        #Create an empty visited list
        visited = set()
        #Add the start node to the queue
        q.enqueue([starting_node])
        #while the Queue is not empty...
        while q.size() > 0:
            #remove the first node from the Queue
            node = q.dequeue()
            #If it the last item in the path list ([node[-1]]) b/c it goes by index hasn't been visited
            if node[-1] not in visited:
                #Mark it as visited, by visited.add(node[-1])
                if destination_node == node[-1]:
                    return node
                visited.add(node[-1])
                # then put all its children in the queue
                for child in self.vertices[node[-1]].edges:
                    new_path = list(node)
                    new_path.append(child)
                    q.enqueue(new_path)
        return None

    # DFS Search
    def dfs(self, starting_node, destination_node):
        #Create an empty stack
        s = Stack()
        #Create an empty visited list
        visited = set()
        #Add the start node to the queue
        s.push([starting_node])
        #while the stack is not empty...
        while s.size() > 0:
            #remove the first node from the stack
            path = s.pop()
            #If it hasn't been visited
            if path[-1] not in visited:
                #Mark it as visited
                # print(node)
                if destination_node == path[-1]:
                    return path
                visited.add(path[-1])
                # then put all its children in the stack
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    s.push(new_path)
        return None
        
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()