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

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
            return True
        else:
            if vertex1 not in self.vertices:
                raise IndexError(f"Vertex {vertex1} is nonexistent!")
            elif vertex2 not in self.vertices:
                raise IndexError(f"Vertex {vertex2} is nonexistent!")

    def add_directed_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            return True
        else:
            if vertex1 not in self.vertices:
                raise IndexError(f"Vertex {vertex1} is nonexistent!")
            elif vertex2 not in self.vertices:
                raise IndexError(f"Vertex {vertex2} is nonexistent!")

    def bft(self, target):
        queue = []
        visited = []
        queue.append(int(target))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")

        while len(queue) > 0:
            discovered = queue.pop(0)
            if discovered not in visited:
                visited.append(discovered)
                for child in self.vertices[str(discovered)]:
                    queue.append(int(child))

        print(f"vertices: {self.vertices}")
        return f"bft: {visited}"

    def dft(self, target):
        stack = []
        visited = []
        stack.append(int(target))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")

        while len(stack) > 0:
            discovered = stack.pop()
            if discovered not in visited:
                visited.append(discovered)
                for child in self.vertices[str(discovered)]:
                    stack.append(int(child))

        print(f"vertices: {self.vertices}")
        return f"dft: {visited}"

    def dftr(self, target, visited=[]):
        while target not in visited:
            visited.append(target)
            for child in self.vertices[str(target)]:
                self.dftr(int(child), visited)
        return f"dftr: {visited}"

    def bfs(self, start_node, target):
        queue = []
        visited = []
        queue.append(int(start_node))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")
        elif str(start_node) not in self.vertices:
            raise IndexError(f"Vertex {start_node} is nonexistent")

        while len(queue) > 0:
            discovered = queue.pop(0)
            if discovered not in visited:
                visited.append(discovered)
                if discovered == target:
                    break
                for child in self.vertices[str(discovered)]:
                    queue.append(int(child))

        print(f"vertices: {self.vertices}")
        return f"bfs: {visited}"

    def dfs(self, start_node, target):
        stack = []
        visited = []
        stack.append(int(start_node))

        if str(target) not in self.vertices:
            raise IndexError(f"Vertex {target} is nonexistent!")
        elif str(start_node) not in self.vertices:
            raise IndexError(f"Vertex {start_node} is nonexistent")

        while len(stack) > 0:
            discovered = stack.pop()
            if discovered not in visited:
                visited.append(discovered)
                if discovered == target:
                    break
                for child in self.vertices[str(discovered)]:
                    stack.append(int(child))

        print(f"vertices: {self.vertices}")
        return f"dfs: {visited}"


graph1 = Graph()
graph1.add_vertex("0")
graph1.add_vertex("1")
graph1.add_vertex("2")
graph1.add_vertex("3")
graph1.add_vertex("4")
graph1.add_edge("0", "1")
graph1.add_edge("1", "2")
graph1.add_edge("2", "3")
graph1.add_edge("2", "4")
# graph1.add_edge("5", "2")  # checks arg1, non-existent vertex 5 raises IndexError
# graph1.add_edge("2", "5")  # checks arg2, non-existent vertex 5 raises IndexError
# print(graph1.bft(4))  # returns 4
# print(graph1.bft(5))  # non-existent vertex 5, returns False
# print(graph1.dft(4))  # returns 4
# print(graph1.dft(5))  # non-existent vertex 5, returns False

graph2 = Graph()
graph2.add_vertex("1")
graph2.add_vertex("2")
graph2.add_vertex("3")
graph2.add_vertex("4")
graph2.add_vertex("5")
graph2.add_vertex("6")
graph2.add_vertex("7")
graph2.add_directed_edge("1", "2")
graph2.add_directed_edge("2", "3")
graph2.add_directed_edge("2", "4")
graph2.add_directed_edge("3", "5")
graph2.add_directed_edge("4", "6")
graph2.add_directed_edge("4", "7")
graph2.add_directed_edge("5", "3")
graph2.add_directed_edge("6", "3")
graph2.add_directed_edge("7", "1")
graph2.add_directed_edge("7", "6")
# print(graph2.bft(1))  # returns [1, 2, 4, 3, 6, 7, 5]
# print(graph2.bft(7))  # returns [7, 6, 1, 3, 2, 5, 4]
# print(graph2.dft(1))  # returns [1, 2, 3, 5, 4, 6, 7]
# print(graph2.dft(7))  # returns [7, 1, 2, 3, 5, 4, 6]
# print(graph2.dftr(1))  # returns [1, 2, 4, 6, 3, 5, 7]
# print(graph2.dftr(7))  # returns [7, 6, 3, 5, 1, 2, 4]
# print(graph2.bfs(1, 7))  # returns [1, 2, 4, 3, 6, 7]
# print(graph2.bfs(7, 1))  # returns [7, 6, 1]
# print(graph2.dfs(1, 7))  # returns [[1, 2, 4, 7]
print(graph2.dfs(7, 1))  # returns [7, 1]
