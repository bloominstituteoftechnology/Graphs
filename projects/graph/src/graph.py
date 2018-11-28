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

   #### Recursion ####
    # DFT Recursion

    def dft_r(self, starting_node):
        # Mark starting_node as visited
        # Then call dft_r on each child
        stack = Stack()
        visited_list = set()
        visited_list.add(node)
        for child in self.vertices[node].edges:
            dft_r(child)

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()


# ## Part 1: Graph, Vertex, Edge Classes

# In the file `graph.py`, implement a `Graph` class that supports the API expected
# by `draw.py`. In particular, this means there should be a field `vertices` that
# contains a dictionary mapping vertex labels to edges. For example:

# ```python
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
# ```

# This represents a graph with four vertices and two total (bidirectional) edges.
# The vertex `'2'` has no edges, while `'0'` is connected to both `'1'` and `'3'`.

# You should also create `add_vertex` and `add_edge` methods that add the
# specified entities to the graph. To test your implementation, instantiate an
# empty graph and then try to run the following:

# ```python
# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
# ```

# You should see something like the first example. As a stretch goal, add checks
# to your graph to ensure that edges to nonexistent vertices are rejected.

# ```python
# # Continuing from previous example
# graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
# ```
    
