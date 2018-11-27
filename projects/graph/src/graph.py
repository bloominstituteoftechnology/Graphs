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
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[vertex.node] = vertex.edges
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
            return True
        else:
            if v1 not in self.vertices:
                raise IndexError(
                    f"Vertex {v1} is nonexistent!"
                )  # IndexError more specific than Exception
            elif v2 not in self.vertices:
                raise IndexError(f"Vertex {v2} is nonexistent!")

    def bft(self, target):
        q = []
        visited = []
        q.append(int(target))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")

        while len(q) > 0:
            discovered = q.pop(0)
            if discovered not in visited:
                visited.append(discovered)
                for c in self.vertices[str(discovered)]:
                    q.append(int(c))

        print(f"vertices: {self.vertices}")
        return f"visited: {visited}"


# GRAPH 1
# graph = Graph()
# graph.add_vertex("0")
# graph.add_vertex("1")
# graph.add_vertex("2")
# graph.add_vertex("3")
# graph.add_vertex("4")
# graph.add_edge("0", "1")
# graph.add_edge("1", "2")
# graph.add_edge("2", "3")
# graph.add_edge("2", "4")
# graph.add_edge("5", "2")  # checks arg1, non-existent vertex 5 raises IndexError
# graph.add_edge("2", "5")  # checks arg2, non-existent vertex 5 raises IndexError
# print(graph.bft(4))  # returns 4
# print(graph.bft(5))  # non-existent vertex 5, returns False

# GRAPH 2
graph = Graph()
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_vertex("4")
graph.add_vertex("5")
graph.add_vertex("6")
graph.add_vertex("7")
graph.add_edge("1", "2")
graph.add_edge("2", "3")
graph.add_edge("2", "4")
graph.add_edge("3", "5")
graph.add_edge("4", "6")
graph.add_edge("4", "7")
graph.add_edge("5", "3")
graph.add_edge("6", "3")
graph.add_edge("7", "1")
graph.add_edge("7", "6")
# print(graph.bft(4))  # returns [4,7,6,2,1,3,5]
print(graph.bft(7))  # returns [7,1,6,4,2,3,5]
