"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertice):
        if vertice in self.vertices:
            raise ValueError('Vertice is already in the graph')
        else:
            self.vertices[vertice] = set()

    def add_directed_edge(self, vertice, directed_edge):
        try:
            self.vertices[vertice].add(directed_edge)
        except KeyError:
            raise ValueError(f'We dont have a vertice of {vertice}')
        try:
            self.vertices[directed_edge].add(vertice)
        except KeyError:
            raise ValueError(f'We dont have a vertice of {directed_edge}')

    def breadth_first_search(self, starting_node):
        visited = [False] * (len(self.vertices) + 1)
        queue = []
        queue.append(starting_node)
        visited[int(starting_node)] = True
        while len(queue) > 0:
            node = queue.pop(0)
            for nodes in self.vertices[node]:
                if visited[int(nodes)] == False:
                    queue.append(nodes)
                    visited[int(nodes)] = True

    def depth_first_search(self, starting_node):
        visited = [False] * (len(self.vertices) + 1)
        stack = []
        visited[int(starting_node)] = True
        stack.append(starting_node)
        while stack:
            node = stack.pop(0)
            print(stack)
            for i in self.vertices[node]:
                if visited[int(i)] == False:
                    visited[int(i)] = True
                    stack.append(i)

    def recursive_dfs(self, starting_node, visited=[]):
        visited.append(starting_node)
        for node in self.vertices[starting_node]:
            if node not in visited:
                # print(self.vertices[starting_node], 'da stack s')
                self.recursive_dfs(node, visited)
        return visited

    def bfs_search(self, start, end):
        queue = []
        queue.append([start])
        # print(queue)
        while queue:
            print(queue, 'queue')
            path = queue.pop(0)
            print(path, 'path')
            node = path[-1]
            print(node, 'node')
            if node == end:
                return path
            for adjacent in self.vertices.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def dfs_search(self, start, end):
        # we just need to tweak our dfs function a little bit
        visited = []
        queue = [[start]]
        while queue:
            queue_nodes = queue.pop()
            print(queue, 'we will pop off the last one')
            print(queue_nodes, 'node to be worked on')
            node = queue_nodes[-1]
            if node == end:
                return queue_nodes
            for adjacent in self.vertices[node]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    new_path = list(queue_nodes)
                    new_path.append(adjacent)
                    queue.append(new_path)
