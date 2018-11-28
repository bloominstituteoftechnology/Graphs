"""
Simple graph implementation compatible with BokehGraph class.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
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


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, start):
        # Create empty Queue
        q = Queue()
        # Create an empty visited list
        visited = set()
        # Add the start node to the queue
        q.enqueue(start)
        # While the Queue is not empty...
        while q.size() > 0:
            # Remove the first node from the Queue
            node = q.dequeue()
            # If it hasn't been visited
            if node not in visited:
                # Mark it as visited
                print(node)
                visited.add(node)
                # then put all it's children in the queue
                for child in self.vertices[node].edges:
                    q.enqueue(child)

    def dft(self, start):
        # Create empty Stack
        s = Stack()
        # Create an empty visited list
        visited = set()
        # Add the start node to the stack
        s.push(start)
        # While the Stack is not empty...
        while s.size() > 0:
            # Remove the first node from the Queue
            node = s.pop()
            # If it hasn't been visited
            if node not in visited:
                # Mark it as visited
                print(node)
                visited.add(node)
                # then put all it's children in the stack
                for child in self.vertices[node].edges:
                    s.push(child)

    # I could probably simplify this more
    def dft_r(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        for child in self.vertices[start].edges:
            if child not in visited:
                self.dft_r(child, visited)

    def bfs(self, start, destination):
        # Create empty Queue
        q = Queue()
        # Create an empty visited list
        visited = set()
        # Add the start node to the queue
        q.enqueue([start])

        # While the Queue is not empty...
        while q.size() > 0:
            # Remove the first node from the Queue
            node = q.dequeue()
            # If it hasn't been visited
            if node[-1] not in visited:
                # Mark it as visited
                if destination == node[-1]:
                    return node
                visited.add(node)
                # then put all it's children in the queue
                for child in self.vertices[node[-1]].edges:
                    new_path = list(node)
                    new_path.append(child)
                    q.enqueue(child)
        return None

    def dfs(self, start, destination):
        # Create empty Stack
        s = Stack()
        # Create an empty visited list
        visited = set()
        # Add the start node to the stack
        s.push([start])
        # While the Stack is not empty...
        while s.size() > 0:
            # Remove the first node from the Queue
            path = s.pop()
            # If it hasn't been visited
            if path[-1] not in visited:
                if destination == path[-1]:
                    return path
                visited.add(path[-1])
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    s.push(new_path)
        return None

    def dfs_r(self, start, visited=None, destination=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []
        visited.add(start)
        extended_path = list(path)
        extended_path.append(start)
        if start == destination:
            return extended_path
        for child in self.vertices[start].edges:
            if child not in visited:
                new_path = self.dfs_r(child, destination, visited, extended_path)
                if new_path:
                    return new_path

        return None


"""
First pass representation of Graph - without Vertex class
"""


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.verticies = {}
#
#     def add_vertex(self, value):
#         self.verticies[value] = set()
#
#     def add_edge(self, value1, value2):
#         # Check's if the node exists, if not, return
#         if value2 not in self.verticies:
#             return
#
#         val = self.verticies[value1]
#         val.add(value2)
#         self.verticies[value1] = val
#
#         val2 = self.verticies[value2]
#         val2.add(value1)
#         self.verticies[value2] = val2
#
#     def dfs(self, start):
#         # Keep track of all the visited nodes and setup a stack
#         visited, stack = set(), [start]
#
#         # Keep looping until there are nodes still to be checked
#         while stack:
#             vertex = stack.pop()
#             # Add the node if it is not in visited
#             if vertex not in visited:
#                 visited.add(vertex)
#                 stack.extend(self.verticies[vertex] - visited)
#         return visited
#
#     # Recursive solution
#     def dfs_recursive(self, start, visited=None):
#         # Set visited as a new set if not already
#         if visited is None:
#             visited = set()
#
#         # Add the node
#         visited.add(start)
#
#         # Repeat until no more nodes left
#         for next in self.verticies[start] - visited:
#             self.dfs_recursive(next, visited)
#         return visited
#
#     def bfs(self, start, goal):
#         # Keep track of all visited nodes
#         explored = []
#         # Keep track of nodes to be checked
#         queue = [[start]]
#
#         # Keep looping until there are nodes still to be checked
#         while queue:
#             # Pop shallowest node (first node) from queue
#             path = queue.pop(0)
#             node = path[-1]
#             if node not in explored:
#                 # Add node to list of checked nodes
#                 neighbours = self.verticies[node]
#
#                 # Add neighbors of node to queue
#                 for neighbour in neighbours:
#                     new_path = list(path)
#                     new_path.append(neighbour)
#                     queue.append(new_path)
#                     if neighbour == goal:
#                         return new_path
#
#                 explored.append(node)
#         return explored


# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('0', '5')
# print(graph.verticies)
#
# print(graph.bfs('1'))
# print(graph.dfs('1'))
# print(graph.dfs_recursive('1'))
