"""
Simple graph implementation compatible with BokehGraph class.
"""
class Queue():
    def __init__(self):
        self.queue = []
    def enq(self,value):
        self.queue.append(value)
    def deq(self):
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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # Initialize an empty set when adding a vertex to the graph
    def add_vertex(self,vertex_id, color="white"):
        self.vertices[vertex_id] = set()
    # def get_edges(self,vertex_id):
    #     self.vertices[vertex_id]
    
    # When adding an edge, assume its undirected and check for membership
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('That vertex value is not available. please add it first')
    
    # When adding an directed edge, only check source node/vertex for membership
    def add_directed_edge(self,v1,v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex value is not available. please add it first')

    # Recursive DFT
    # Give it a starting node and a list to hold visited
    # The visited list, is how to keep track of stuff through recursion, pass it along!            
    def dft(self, current_vert, visited):
        print(f"DFT Recurse Listing: {current_vert}")
        # Add the current_vert to the visited list
        visited.append(current_vert)
        # print(f"DFT Recurse Visited: {visited}")
        # Vertices is a dictionary where the key is a vertex and the value is a list of child vertices
        # Loop through the child vertices
        for child_vert in self.vertices[current_vert]:
            # if the child is not in visited, call dft on the child
            if child_vert not in visited:
                self.dft(child_vert, visited)
    
    
    # def dft(self, start_vert, visited=[]):
    #     visited.append(start_vert)
    #     print(self.vertices[start_vert].value)
    #     for child_vert in self.vertices[start_vert].edges:
    #         if child_vert not in visited:
    #             self.dft(child_vert)
    #             # Should be self.dft(child_vert, visited)

    def dfs(self, adjList,vertex_id, visited, search):
        if vertex_id == search:
            return True
        visited.append(vertex_id)
        for child in adjList[vertex_id]:
            if child not in visited:
                self.dfs(adjList,child,visited, search)
        return False


    # BFT using a list
    def bftl(self, start_vert):
        frontier = []
        frontier.append(start_vert)
        visited = []
        while len(frontier) > 0:
            n = frontier.pop(0)
            if n not in visited:
                print(f"BFT Listing: {n}")
                visited.append(n)
                for next_vertex in self.vertices[n]:
                    frontier.append(next_vertex)

    #BFT using a Queue class that is based off of a list
    def bftq(self, start_vert):
        # Create a queue
        q = Queue()
        # Enque the start_vert
        q.enq(start_vert)
        # Initialize the visited list
        visited = []
        # while the queue size is > 0:
        while q.size() > 0:
            # Dequeue a vertex from the queue
            n = q.deq()
            # if that vertex is not visited:
            if n not in visited:
                # place in visited
                visited.append(n)
                print(f"BFT Listing: {n}")
                # Enque all of the this vert's children
                for next_vertex in self.vertices[n]:
                    q.enq(next_vertex)

    # DFT using a stack is exactly like BFT but with a stack instead!
    def dfts(self, start_vert):
        # Create a queue
        s = Stack()
        # Enque the start_vert
        s.push(start_vert)
        # Initialize the visited list
        visited = []
        # while the queue size is > 0:
        while s.size() > 0:
            # Dequeue a vertex from the queue
            n = s.pop()
            # if that vertex is not visited:
            if n not in visited:
                # place in visited
                visited.append(n)
                print(f"BFT Listing: {n}")
                # Enque all of the this vert's children
                for next_vertex in self.vertices[n]:
                    s.push(next_vertex)

# class Vertex:
#     def __init__(self, vertex_id, value, color="white"):
#         self.id = vertex_id
#         self.value = value
#         self.color = color
#         self.edges = []


# Testing
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
print(graph.vertices)
graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('0', '3')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('2', '6')
graph.add_edge('2', '7')
graph.add_edge('3', '8')
graph.add_edge('3', '9')

# Add this edge to turn the tree to a graph:
# graph.add_edge('9', '7')
print(graph.vertices)
print('\n DFT:')
graph.dft('0',[] )

print('\n DFT Stack:')
graph.dfts('0')

print('\n BFT Q:')
graph.bftq('0')

print('\n BFT List:')
graph.bftl('0')

print('\n Search:')
print(graph.dfs(graph.vertices, '0',[], '2'))
