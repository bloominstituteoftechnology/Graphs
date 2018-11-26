# """
# Simple graph implementation compatible with BokehGraph class.
# """
# import random
# import collections


# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if (self.size()) > 0:
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
#         if (self.size()) > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):
#         """
#         Create an empty graph
#         """
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add an vertex to the graph
#         """
#         self.vertices[vertex_id] = Vertex(vertex_id)

#     def add_edge(self, v1, v2):
#         """
#         Add an undirected edge to the graph
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#             self.vertices[v2].edges.add(v1)
#         else:
#             raise IndexError("That vertex does not exist!")

#     def add_directed_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph
#         """
#         if v1 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#         else:
#             raise IndexError("That vertex does not exist!")

# def dft(self, starting_node, visited=None):
#     """
#     Depth first traversal using recursion
#     """
#     # Mark the node as visited
#     if visited is None:
#         # quese of visited nodes
#         visited = []
#     visited.append(starting_node)
#     # For each child, if that child hasn't been visited, call dft() on that node
#     for node in self.vertices[starting_node].edges:
#         if node not in visited:
#             self.dft(node, visited)
#     return visited

# Mark the node as visited, then for each child that hasn't been visited, call DFT() on that node.

# def bft(self, starting_node):
#     """
#     Breadth first traversal using a queue
#     """
#     # create an empty queue
#     visited, queue = set(), collections.deque([starting_node]) # Put starting vert in the queue
#     while queue:
#         vertex = queue.popleft() # Remove the first node from the queue...
#         if vertex not in visited: # If it has not been visited yet,...
#             visited.add(vertex) # Mark it as visited....
#             print(vertex)
#             for neighbor in self.vertices[vertex].edges: # Then put all it's children in the back of the queue
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#     return visited

# def bft(self, starting_node):
#     visited = []
#     # create an empty queue
#     q = Queue()
#     # Put starting vert in the queue
#     q.enqueue(starting_node)
#     while q.size() > 0:  # whlie queue is not empty...
#         dequeued = q.dequeue() # Dequeue the first element
#         visited.append(dequeued)  # Mark it as visited
#         print(dequeued)
#         for edge in self.vertices[dequeued].edges:  #For each child
#             if edge not in visited:  # If it hasn't been visited
#                 q.enqueue(edge)  # Add it to the back of the queue
#     return visited

# def dft_s(self, starting_node):
#     visited = []
#     # create an empty stack
#     s = Stack()
#     # Put starting vert on top of the stack
#     s.push(starting_node)
#     while s.size() > 0:  # whlie stack is not empty...
#         destacked = s.pop() # Pop the first element
#         visited.append(destacked)  # Mark it as visited
#         print(destacked)
#         for edge in self.vertices[destacked].edges:  #For each child
#             if edge not in visited:  # If it hasn't been visited
#                 s.push(edge)  # Add it to the top of the stack
#     return visited

# def dft_s(self, starting_node):
#     s = Stack()
#     s.push(starting_node)
#     visited = []
#     while s.size() > 0:
#         current = s.pop()
#         if current not in visited:
#             visited.append(current)
#             print(visited)
#             for edge in self.vertices[current].edges:
#                 s.push(edge)

# def bfs(self, starting_node, target_node):
#     visited = []
#     # create an empty queue
#     q = Queue()
#     # Put starting vert in the queue
#     q.enqueue(starting_node)
#     while q.size() > 0:  # whlie queue is not empty...
#         dequeued = q.dequeue() # Dequeue the first element
#         visited.append(dequeued)  # Mark it as visited
#         print(dequeued)
#         if dequeued == target_node:
#             return True
#         for edge in self.vertices[dequeued].edges:  #For each child
#             if edge not in visited:  # If it hasn't been visited
#                 q.enqueue(edge)  # Add it to the back of the queue
#     return False

# def dfs(self, starting_node, target_node, visited=None):
#     """
#     Depth first traversal using recursion
#     """
#     # Mark the node as visited
#     if visited is None:
#         # quese of visited nodes
#         visited = []
#     visited.append(starting_node)
#     if starting_node == target_node:
#         return True
#     # For each child, if that child hasn't been visited, call dft() on that node
#     for node in self.vertices[starting_node].edges:
#         if node not in visited:
#             if self.dfs(node, target_node, visited):
#                 return True
#     return False


# class Vertex:
#     def __init__(self, vertex_id, x=None, y=None):
#         """
#         Create an empty vertex
#         """
#         self.id = vertex_id
#         self.edges = set()
#         if x is None:
#             self.x = random.random() * 10 - 5
#         else:
#             self.x = x
#         if y is None:
#             self.y = random.random() * 10 - 5
#         else:
#             self.y = y

#     def __repr__(self):
#         return f"{self.edges}"

##############################################################
##############################################################
class Graph:
    def __init__(self):
        pass  # TODO	        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception("Error: adding vertex that already exists")
        if not set(edges).issubset(self.vertices):
            raise Exception("Error: cannot have edge to nonexistent vertices")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices to connect not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method="dfs"):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == "bfs" else -1
        visited = set([start])
        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])
        return visited

    def find_components(self):
        """Identify components and update vertex component ids."""
        visited = set()
        current_component = 0
        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component


class Vertex:
    """Represent a vertex with a label and possible connected component."""

    # pylint: disable=too-few-public-methods
    # Using class so it's hashable, even though it doesn't have public methods
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return "Vertex: " + self.label

