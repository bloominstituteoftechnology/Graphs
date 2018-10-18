"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, num1, num2):
        if num1 in self.vertices and num2 in self.vertices:
            self.vertices[num1].add(num2)
            self.vertices[num2].add(num1)
            return
        print("Invalid edges")
    def add_oneway_edge(self, num1, num2):
        if num1 in self.vertices and num2 in self.vertices:
            self.vertices[num1].add(num2)
            return
        print("Invalid edges")

    def searchPath(self, sourceVextix, searchItem):
        # breadth first search
        visited = []
        queue = []
        if sourceVextix == searchItem:
            return True
        visited.append(sourceVextix)

        for key in self.vertices[sourceVextix]:
            queue.append(key)
        while(len(queue) is not 0):
            currentKey = queue.pop(0)
            visited.append(currentKey)
            if currentKey == searchItem:
                return True
            for childkey in self.vertices[currentKey]:
                if childkey not in visited:
                    queue.append(childkey)
        return False
    def DFS(self, sourceVextix):
        