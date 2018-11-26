"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = { }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex_a, vertex_b ):
        if vertex_a in self.vertices.keys() and vertex_b in self.vertices.keys():
            self.vertices[vertex_a].add(vertex_b)
            self.vertices[vertex_b].add(vertex_a)
        else:
            print ("Can't find all vertices")

    def bfs(self, element):
        start_v = list(self.vertices.keys())[0]
        queue = [start_v]
        visited = []

        while queue:
            current = queue[0]
            if current == element:
                return True
            for v in self.vertices[current]:
                if v not in visited and v not in queue:
                    queue.append(v)
            visited.append(queue.pop(0))
            print ('queue:', queue)
            print ('visited:', visited)
        return False

    def dfs(self, element):
        start_v = list(self.vertices.keys())[0]
        stack = [start_v]
        visited = []
        count = 3
        while stack:
            current = stack[0]
            if current == element:
                return True
            for v in self.vertices[current]:
                if v not in visited and v not in stack:
                    stack.insert(0, v)
            visited.append(current)
            stack.remove(current)
            print ('stack:', stack)
            print ('visited:', visited)
            count += 1
        return False

