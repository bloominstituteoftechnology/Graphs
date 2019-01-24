"""
Simple graph implementation
"""

class Vertex:
    def __init__(self, value):
        self.node = value
        self.edges = set() 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}
    def add_vertex(self, vertex_id):
        self.verticies[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
            self.verticies[v2].add(v1)
        else:
            raise IndexError("No vertex!")

    def bfs(self, target):
        queue = [target]  # create a queue and initiate with target
        visited = []  # create a visited list

        # print(self.vertices)
        # print(str(target))

        print(queue)
        if target in queue:
            return True
        else:
            return False
    
    
    def dft(self, target):
        s = []
        visited = []
        s.append(int(target))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")

        while len(s) > 0:
            discovered = s.pop()
            if discovered not in visited:
                visited.append(discovered)
                for c in self.vertices[str(discovered)]:
                    s.append(int(c))

        print(f"vertices: {self.vertices}")
        return f"visited: {visited}"



graph = Graph()
graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
# graph.add_edge("0", "4")
# print(graph.vertices)
print(graph.bfs(2))

print(queue)
if target in queue