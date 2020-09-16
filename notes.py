

"""
# Intro to Graphs

Used in facebook. User have different edges to represent the type of relationship: friends, family, blocked, etc.
Airport and flight numbers - edges going from one airport to another to represent flights between them
Data analytics - Node connects to other nodes to show relationship between the data. 

# components of Graphs

Vertexes - basically nodes. Object that contains data

Edge - connects to a pair of nodes. can be unidirectional (one way), bidrectional (two way), or have weights (edges with values)

# graph properties

Directed - vertex a points to vertex b, but b doesn't point to a

undirected - vertex a and b are connected mutually.

# cyclic vs acyclic

cyclic - vertex connects to vertices that leads back to itself

acyclic - one way traversal of graph

# dense v sparse

dense - close to maxiumum edges. vertices pointed to almost each other

sparse - close to minimum amount of edges.

adjancey list - a dictionary with key as vertex and value as a set with edges from that vertex to others. 

{
    0: { 1, 2 },
    1: { 3 },
    2: { 3 },
    3: { 0 }
}

# adjancey list vs adjancey matrix

overall, list > matrix, however, matrix is generally more space efficient in denser graphs.

# graph traversal

depth first and breadth first

traversal - goes through entire graph

search - stops once term is found

# depth-first traversal

Traverse graph first in a depth-ward motion using a stack / recursion

"""

class Graph:
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        return set()
    
    def dft(self, start):
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                print(curr)
                for edge in self.get_neighbors(curr):
                    stack.append(edge)

    def recursive_dft(self, vertex, visited=set()):
        if vertex in visited:
            return
        visited.add(vertex)
        print(vertex)
        for edge in self.get_neighbors(vertex):
            self.recursive_dft(edge, visited)
    
    # revise this to have 0 -> 1
    def dfs(self, start, end):
        stack = []
        stack.append([start])
        visited = set()
        while stack:
            curr_path = stack.pop() # [1,2,3]
            curr_node = curr_path[-1] # 3
            if curr_node == end:
                return curr_path
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_path)
                for edge in self.get_neighbors(curr_node):
                    # creates new arr with current path
                    new_path = list(curr_path)
                    # add edges into 
                    new_path.append(edge)
                    stack.append(new_path)
    
    def bft(self, start):
        queue = []
        visited = set()
        queue.append(start)
        while queue:
            curr_node = queue.pop(0)
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_node)
                for edge in self.get_neighbors(curr_node):
                    queue.append(edge)

g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,0)


print(g.dfs(0,1))
# g.bft(0)
print()
# g.recursive_dft(0)


