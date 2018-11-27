"""
Simple graph implementation compatible with BokehGraph class.
"""

# super really basic vec2 class
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # add
    def add(self, other):
        self.x += other.x
        self.y += other.y

    # subtract
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y

    # multiply
    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y

    # divide (integer)
    def divide(self, other):
        self.x //= other.x
        self.y //= other.y

## decided to add a 3d vector class too you never know when things might get crazy :)
class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # add
    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    # subtract
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    # multiply
    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z

    # divide (integer)
    def divide(self, other):
        self.x //= other.x
        self.y //= other.y
        self.z //= other.z

# Queue for BFS
class Queue:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop(0) if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)


# Stack for DFS (copied my queue class and removed the argument from pop)
class Stack:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop() if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)




# implement the basics of a vertex class
class Vertex:
    def __init__(self, id, pos = None, colour = None, data = None):
        self.id = int(id)
        self.pos = Vec2(0, 0) if pos is None else pos
        self.colour = "white" if colour is None else colour
        self.data = F"v{self.id}" if data is None else data
        self.edges = set() # refactored vertex to hold its connecting edges

    def __str__(self):
        return F"Vertex( id: {self.id}, x: {self.pos.x}, y: {self.pos.y}, edge_connections: {self.edges}, data: {self.data})"




class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = None):
        self.vertices = {} if vertices is None else vertices

    # add_vertex method
    def add_vertex(self, id, pos, data):
        self.vertices[id] = Vertex(id, pos, data = data)

    # add_edge method (bi directional as default to start with)
    def add_edge(self, vertex_a, vertex_b, bidir = True):
        self.vertices[vertex_a].edges.add(vertex_b)
        if bidir:
            self.vertices[vertex_b].edges.add(vertex_a)

    # Traversals

    # Depth first Traversal
    def dft(self, start_vert, visited=[]):
        visited.append(start_vert)
        print(self.vertices[start_vert].id, ': ', self.vertices[start_vert].data)

        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                self.dft(child_vert, visited)

    # Breadth first Traversal
    def bft(self, start_vert_id):
        queue = Queue()
        queue.enqueue(start_vert_id)
        visited = []

        while queue.size() > 0:
            vert = queue.dequeue()
            
            if vert not in visited:
                print(self.vertices[vert].id, ": ", self.vertices[vert].data)
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    queue.enqueue(next_vert)

    # Searches

    # Depth first search (leveraging off the DFT method)
    def dfs(self, start_vert_id, target_data, visited=[]):
        visited.append(start_vert_id)
        if start_vert_id == target_data:
            return True

        for child_vert in self.vertices[start_vert_id].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_data, visited):
                    return True

        return False

    # Breadth first search 
    def bfs(self, start_vert_id, target_data):
        queue = Queue()
        queue.enqueue(start_vert_id)
        visited = []
        while queue.size() > 0:
            vert = queue.dequeue()
            if vert not in visited:
                if self.vertices[vert].data == target_data:
                    return True
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    queue.enqueue(next_vert)
        return False

    # paths

    # Path for DFS (Recursive Search)
    def path_d(self, start_vert_id, target_data, visited=[], path=[]):
        visited.append(start_vert_id)
        path = path + [start_vert_id]
        if self.vertices[start_vert_id].data == target_data:
            return path
        for child_vert in self.vertices[start_vert_id].edges:
            if child_vert not in visited:
                new_path = self.path_d(child_vert, target_data, visited, path)
                if new_path:
                    return new_path

        return None

    # Path for BFS (Recursive Search)
    def path_b(self, start_vert_id, target_data):
        queue = Queue()
        queue.enqueue([start_vert_id])
        visited = []
        while queue.size() > 0:
            path = queue.dequeue()
            vert = path[-1]
            if vert not in visited:
                if self.vertices[vert].data == target_data:
                    return path
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    # q.enqueue(next_vert) is no more
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        return None


# some basic tests for the vertex class

#constructor test
v0 = Vertex(0, Vec2(3, 4))
v1 = Vertex(1, Vec2(1, 3), colour = "orange")
v2 = Vertex(2, Vec2(3, 5))

# raw positional data manipulation test
v0.pos.x = 23

# vector add test
v0.pos.add(Vec2(10, 10))

# vertex print test
print(v0)
print(v1)
g0 = Graph()
g0.add_vertex(v0.id, v0.pos, "Node0")
g0.add_vertex(v1.id, v1.pos, "Node1")
g0.add_vertex(v2.id, v2.pos, "Node2")
g0.add_vertex(3, v2.pos, "Node3")
g0.add_vertex(4, v2.pos, "Node4")
g0.add_vertex(5, v2.pos, "Node5")
g0.add_vertex(6, v2.pos, "Node6")
g0.add_vertex(7, v2.pos, "Node7")
g0.add_vertex(8, v2.pos, "Node8")
g0.add_vertex(9, v2.pos, "Node9")
g0.add_vertex(10, v2.pos, "Node10")
g0.add_vertex(11, v2.pos, "Node11")
g0.add_edge(0, 1)
g0.add_edge(0, 2)
g0.add_edge(1, 3)
g0.add_edge(2, 7)
g0.add_edge(3, 6)
g0.add_edge(1, 4)
g0.add_edge(1, 5)
g0.add_edge(4, 9)
g0.add_edge(4, 8)

print(g0.vertices[0])
print(g0.vertices[1])
print("BFT")
g0.dft(1)
print("DFT")
g0.bft(1)

print(g0.dfs(2, 4))

# loop over the vertices
for vertex, vert in g0.vertices.items():
    print(vertex, ": ", vert.data, ", connections ", vert.edges)

print("\nRecursive DFS with path to destination mapping \n[0 to Node9]")
print(g0.path_d(0, "Node9"))

print("\nRecursive BFS with path to destination mapping \n[7 to Node1]")
print(g0.path_b(7, "Node1"))