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
    
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
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
    
    def dft_recursive2(self, starting_node, seen=None):
        if seen is None:
            seen = [] # or set to set() but return set not in order
        print(starting_node)
        seen.append(starting_node) # and change to add
        for next_level in self.vertices[starting_node]:
            if next_level not in seen:
                self.dft_recursive2(next_level, seen)
        return seen
    
    def bfs(self, starting_vertex, target): 
        level = {starting_vertex: 0}      #dict of levels for vertex visited
        parent = {starting_vertex: None} #dict of parents for vertex visited
        i = 1                           # sets level used in level to 1
        frontier = [starting_vertex]  # Queue of siblings at each level
        path = []
        while frontier:
            next_level = []
            for u in frontier:  # (parent) vertex visited in order of level
                for v in self.vertices[u]: # children of vertex in above order
                    if v not in level:
                        level[v] = i        # add level for each vertex
                        parent[v] = u       # add parent for each vertex
                        next_level.append(v) # groups all children at same level
                        if v == target:
                            def parents(v, curr_level, path=[target]):
                                if v == starting_vertex or curr_level == 0:
                                    return path  # path of child to parent
                                path.extend(parent[v])
                                curr_level -= 1 # decreases level -> 0
                                v = parent[v]   # sets child to parent -> s_v
                                print(curr_level, v)
                                return parents(v, curr_level, path)
                            path = (parents(v, level[v])) # path t => s_v
                            return path[::-1]
            frontier = next_level   # Queue of next level of siblings
            i += 1                  # Increments level by 1 
        # return path[::-1] if path else False  # path from s_v => t or F for no t
        return False

    def bfs2(self, starting_vertex, target): 
        visited = []
        queue = deque()
        queue.append([starting_vertex])
        
        while queue:     
            path = queue.popleft()
            last_node = path[-1:][0]
            if last_node not in visited:
                print(last_node, path)
                if last_node == target:
                    return path
                visited.append(last_node)
                for v in self.vertices[last_node]:
                    new_list = list(path)
                    new_list.append(v)
                    queue.append(new_list)
        return False

        


    def dfs(self, starting_vertex, target):
        visited = []
        stack = []
        stack.append([starting_vertex])
        
        while stack:     
            path = stack.pop()
            last_node = path[-1:][0]
            if last_node not in visited:
                print(last_node, path)
                if last_node == target:
                    return path
                visited.append(last_node)
                for v in self.vertices[last_node]:
                    new_list = list(path)
                    new_list.append(v)
                    stack.append(new_list)
        return False

    # def dfs_recursive(self, starting_vertex, target, visited=[]):
    #     print('TARGET', target)
    #     visited = visited + [starting_vertex]
    #     if starting_vertex == target:
    #         return visited
    #     print(starting_vertex)
    #     for next_level in self.vertices[starting_vertex]:
    #         if next_level not in visited:
    #             visited =  self.dft_recursive(next_level, visited)
    #     return visited
