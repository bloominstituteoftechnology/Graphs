##### Attempt 3 #######

"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
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
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Vertex: 
    def __init__(self,vertex_id, x = None, y = None, value= None, color = None): #you use vertex_id to uniquely identify the vertex. In value, you can have a number, a name, a location, etc 
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id /10 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            #what is the run time complexity of making the color string below? O(1)
            hexValues = ['0', '1', '2','3', '4', '5','6', '7', '8','9', 'A', 'B','C', 'D','E', 'F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues)-1)]
            self.color = colorString

class Graph: 
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  #dictionary 
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id) #we're indexing the vertex in the dictionary by id, and we're setting the value to a vertex object. 
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    
    #Recursion method
    def dft(self, start_vert_id, visited = []):
        # Visited checks if we've visited the vertex before
        visited.append(start_vert_id)
        # Touch visited vertex (you can change color here)
        print(self.vertices[start_vert_id].value)
        #call DFS on each child (that hasn't been visited)
        for child_vert in self.vertices[start_vert_id].edges:
            #check if child has been visited
            if child_vert not in visited:
                #If not, call dfs
                self.dft(child_vert)
    
    # Stack method
    def dft_stack(self, start_vert_id):
        # Create empty stack
        stack = Stack()
        # Put starting vert in the stack
        stack.push(start_vert_id)
        # Declare visited list
        visited = []
        # While the stack is not empty..
        while stack.size() > 0:
            while stack.size()>0:
                # remove the first item from the stack...
                v = stack.pop()
                # ... then  if it has not been visited
                if v not in visited:
                    # ... print its value...
                    print(self.vertices[v].value)
                    visited.append(v) # ... mark as visited
                    # ... then put its children into the stack
                    for next_vert in self.vertices[v].edges:
                        stack.push(next_vert)
    
    def bft(self, start_vert_id):
        # create empty queue
        q = Queue()
        # put starting vert in the queue
        q.enqueue(start_vert_id)
        # declare visited list
        visited = []
        # While the queue is not empty...
        while q.size() > 0:
            # ... remove the first item from the queue...
            v = q.dequeue()
            # ... then if it has not been visited...
            if v not in visited:
                # ... print its value...
                print(self.vertices[v].value)
                visited.append(v) # ...mark as visited...
                # ... then put its children in the queue
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)

    def dfs(self,start_vert_id, target_value, visited=[]):
        visited.append(start_vert_id)
        # print(self.vertices[start_vert].value)
        if self.vertices[start_vert_id].value == target_value:
            return True
        for child_vert in self.vertices[start_vert_id].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_value, visited):
                    return True
        return False
    
    def bfs(self, start_vert_id, target_value):
        q = Queue()
        q.enqueue(start_vert_id)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(self.vertices[v].value)
                if self.vertices[v].value == target_value:
                    return True
                visited.append(v) # ...mark as visited...
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)
        return False
    
    def dfs_path(self,start_vert_id, target_value, visited=[], path=[]):
        visited.append(start_vert_id)
        path=path+[start_vert_id]
        if self.vertices[start_vert_id].value == target_value:
            return path
        for child_vert in self.vertices[start_vert_id].edges:
            print(path)
            if child_vert not in visited:
                new_path = self.dfs_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None
    
    def bfs_path(self, start_vert_id, target_value):
        q = Queue()
        q.enqueue([start_vert_id])
        visited = []
        while q.size() > 0:
            print(q.queue) #prints every path checked before shortest path is found
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return path
                visited.append(v) # ...mark as visited...
                for next_vert in self.vertices[v].edges:
                    # q.enqueue(next_vert)
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None





































#### Attempt two in graph1.py --> Wasn't able to get this to work with bokeh. Going to just copy code while following 
#### along in lecture
# """
# Simple graph implementation compatible with BokehGraph class.
# """

# class Vertex:
#     def __init__(self, value = None, x = None, y = None):
#         self.value = value
#         self.x = x
#         self.y = y
#         self.adjVertices = set()

#         if self.x is None:
#             self.x = self.value
#         if self.y is None:
#             self.y = self.value

#     def getAdjVertices(self):
#         adjVerticesValues = set()
#         for i in self.adjVertices:
#             adjVerticesValues.add(i.value)
#         return adjVerticesValues

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self, vertices = dict()):
#         self.vertices = vertices

#     def add_vertex(self, vertexValue):
#         vertex = Vertex(vertexValue)
#         self.vertices[vertex] = vertex
    
#     def add_edge(self, originVertexValue, destinationVertexValue):
#         inVertices1 = False
#         inVertices2 = False

#         for vertex in self.vertices:
#             if originVertexValue == vertex.value:
#                 inVertices1 = True
#                 originVertex = vertex
#             if destinationVertexValue == vertex.value:
#                 inVertices2 = True
#                 destinationVertex = vertex
        
#         if inVertices1 == True and inVertices2 == True:
#             originVertex.adjVertices.add(destinationVertex)
#             destinationVertex.adjVertices.add(originVertex)
#         else:
#             raise IndexError("That vertex does not exist!")


# # ### Test ###
# # # To test, instantiate empty graph and run the following:
# # graph = Graph()  # Instantiate your graph
# # graph.add_vertex(0)
# # graph.add_vertex(1)
# # graph.add_vertex(2)
# # graph.add_vertex(3)
# # graph.add_edge(0, 1)
# # graph.add_edge(0, 3)
# # # print(graph.vertices)

# # for i in graph.vertices:
# #     print("Value: ", i.value, " ; AdjVertices: ", i.getAdjVertices())















# ######### Initial Attempt ###########

# """
# Simple graph implementation compatible with BokehGraph class.
# """

# class Vertex:
#     def __init__(self, value):
#         self.value = value
#         self.adjVertices = set()

#     def getAdjVertices(self):
#         adjVerticesValues = set()
#         for i in self.adjVertices:
#             adjVerticesValues.add(i.value)
#         return adjVerticesValues

# # The code for the graph data structure below is different than that above in 
# # that it first requires that you instantiate vertex objects before adding them
# # as vertices to the graphs. Thebetter approach is to instantiate the vertex object 
# # within the Graph class by passing in the desired value of the vertex to the add 
# # vertex method in the Graph data structure. 
# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self, vertices = dict()):
#         self.vertices = vertices

#     def add_vertex(self, vertex):
#         self.vertices[vertex] = vertex
    
#     def add_edge(self, originVertex, destinationVertex):
#         originVertex.adjVertices.add(destinationVertex)
#         destinationVertex.adjVertices.add(originVertex)

# # To add an edge, the add_edge method should receive an origin Vertex and a destination Vertex.
# # This method should add a vertex to the adjVertices of the origin and destination vertices

# # v1 = Vertex(10)
# # v2 = Vertex(5)
# # v3 = Vertex(14)

# # g1 = Graph()

# # g1.add_vertex(v1)
# # g1.add_vertex(v2)
# # g1.add_vertex(v3)
# # # print(g1.vertices[v1].value)

# # g1.add_edge(v1,v3)
# # g1.add_edge(v1,v2)
# # print(v1.getAdjVertices())


# # The code below yields errors because my initial approach to the graph class first required that 
# # one instantiate the vertices before passing them in to the graph class. The initial graph code passes 
# # the desired vertex values to the graph class instead of passing in a vertex object. 

# # graph = Graph()  # Instantiate your graph
# # graph.add_vertex(0)
# # graph.add_vertex(1)
# # graph.add_vertex(2)
# # graph.add_vertex(3)
# # graph.add_edge(0, 1)
# # graph.add_edge(0, 3)
# # print(graph.vertices)