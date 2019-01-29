from collections import deque
"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, id):
        if id not in self.vertices:
            self.vertices[id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("No vertex")

    def bft(self, starting_vertex):
        visited = []
        queue = deque()
        queue.append(starting_vertex)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
                next_layer = self.vertices[vertex]
                for node in next_layer:
                    if node not in queue and node not in visited:
                        queue.append(node)
        return visited


    def dft(self, starting_vertex):
        visited = []
        # Create a stack
        stack = [starting_vertex]
        # Mark first vertex as visited
        # push the starting node
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.append(current)
                next_layer = self.vertices[current]
                for node in next_layer:
                    if node not in stack and node not in visited:
                        stack.append(node)
        return visited

    def dft_recursive(self, starting_vertex, visited=[]):
        visited = visited + [starting_vertex]
        print(starting_vertex)
        for next_level in self.vertices[starting_vertex]:
            if next_level not in visited:
                visited =  self.dft_recursive(next_level, visited)
        return visited

    # Returns path if target is in it else it returns false
    # It can be modified to return all paths
    def bfs(self, starting_vertex, target): 
        if starting_vertex == target:       
            return [starting_vertex, target]
        visited = []
        queue = deque()
        queue.append(starting_vertex)
        paths = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                next_layer = self.vertices[vertex]
                for node in next_layer:
                    if node not in queue and node not in visited:
                        queue.append(node)
                        if vertex == starting_vertex:
                            paths.extend(['path', vertex, node])
                        elif vertex in paths:
                            for i in range(len(paths)):
                                if paths[i] == vertex:
                                    paths.insert(i+1, node)
        path_str = ''.join(paths)
        all_paths = path_str.split('path')
        all_paths = list(filter(None, all_paths))
        print(all_paths)
        targeted_path = [path for path in all_paths if target in path]
        return list(targeted_path[0]) if targeted_path else False


    def dfs(self, starting_vertex, target):
        print('TARGET', target)
        if starting_vertex == target:
            return target
        visited = []
        # Create a stack
        stack = [starting_vertex]
        # Mark first vertex as visited
        # push the starting node
        while stack:
            current = stack.pop()
            if current not in visited:
                if current == target:
                    return visited
                print(current)
                visited.append(current)
                next_layer = self.vertices[current]
                for node in next_layer:
                    if node not in stack and node not in visited:
                        stack.append(node)
        return visited

    def dfs_recursive(self, starting_vertex, target, visited=[]):
        print('TARGET', target)
        visited = visited + [starting_vertex]
        if starting_vertex == target:
            return visited
        print(starting_vertex)
        for next_level in self.vertices[starting_vertex]:
            if next_level not in visited:
                visited =  self.dft_recursive(next_level, visited)
        return visited
