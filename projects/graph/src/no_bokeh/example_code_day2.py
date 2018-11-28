# """
# Simple graph implementation
# """

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)



# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = Vertex(vertex_id)
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#             self.vertices[v2].edges.add(v1)
#         else:
#             raise IndexError("That vertex does not exist")
#     def add_directed_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#         else:
#             raise IndexError("That vertex does not exist")
#     def bft(self, starting_node):
#         # Create an empty Queue
#         q = Queue()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the queue
#         q.enqueue(starting_node)
#         # While the Queue is not empty...
#         while q.size() > 0:
#             # remove the first node from the Queue
#             node = q.dequeue()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 print(node)
#                 visited.add(node)
#                 # then put all its children in the queue
#                 for child in self.vertices[node].edges:
#                     q.enqueue(child)

#     def dft(self, starting_node):
#         # Create an empty Stack
#         s = Stack()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the stack
#         s.push(starting_node)
#         # While the Stack is not empty...
#         while s.size() > 0:
#             # remove the first node from the Stack
#             node = s.pop()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 print(node)
#                 visited.add(node)
#                 # then put all its children in the stack
#                 for child in self.vertices[node].edges:
#                     s.push(child)

#     def dft_r(self, starting_node):
#         # Mark starting_node as visited
#         # Then call dft_r on each child
#         pass


#     visited = [1, 2, 3, 4]
#     queue = [[1, 2, 3, 5], [1, 2, 4, 6], [1, 2, 4, 7]]

#     def bfs(self, starting_node, destination_node):
#         # Create an empty Queue
#         q = Queue()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the queue
#         q.enqueue(starting_node)
#         # While the Queue is not empty...
#         while q.size() > 0:
#             # remove the first node from the Queue
#             node = q.dequeue()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 if destination_node == node:
#                     return True
#                 visited.add(node)
#                 # then put all its children in the queue
#                 for child in self.vertices[node].edges:
#                     q.enqueue(child)
#         return False

# class Vertex:
#     def __init__(self, vertex_id):
#         self.id = vertex_id
#         self.edges = set()