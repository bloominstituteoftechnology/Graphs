import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        self.vertices[node] = set()
        return self.vertices

    def add_edge(self, from_node, to_node):
        self.vertices[from_node].add(to_node)
        self.vertices[to_node].add(from_node)
        return

    def add_directed_edge(self, ver1, ver2):
        if ver1 in self.vertices:
            self.vertices[ver1].add(ver2)
        else:
            raise IndexError(
                'That vertex value is not available. please add it first')


    # def bfs(adjList, node_id):
    #     frontier = []
    #     frontier.append(node_id)
    #     visited = []
    #     while len(frontier > 0):
    #         n = frontier.pop(0)
    #         if n not in visited:
    #             print(n)
    #             visited.append(n)
    #             for next_node in adjList[n]:
    #                 frontier.append(next_node)


    def get_connected_components(self):
        searched = []
        for index in self.vertices:
            if index not in searched:
                searched.append(self.dfs(index))
        return searched

    def dfs(self):
        start = self.vertices[:0]

        random_color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) 
        
        stack = []
        found = []
        stack.append(start)
        found.append(start)
        
        while (len(stack) > 0):
            v = stack.pop()
            if v not in found:
                found.append(v)
            for edge in v:
                if edge not in found:
                    stack.append(v)
        return found

    def __str__(self):
        return f"{self.vertices}"


