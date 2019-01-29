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
            frontier = next_level   # Queue of next level of siblings
            i += 1                  # Increments level by 1 
        return path[::-1] if path else False  # path from s_v => t or F for no t
    # # Returns path if target is in it else it returns false
    # # It can be modified to return all paths
    # def bfs(self, starting_vertex, target): 
    #     if starting_vertex == target:       
    #         return [starting_vertex, target]
    #     visited = []
    #     queue = deque()
    #     queue.append(starting_vertex)
    #     paths = []
    #     while queue:
    #         # set node to the last element of the path
    #         vertex = queue.popleft()

    #         # NEED TO DUPLICATE
    #         # dupl_list = list(l)
    #         # append child
    #         # add all dupl_list to paths
    #         # pop of list from queue
    #         if vertex not in visited:
    #             print(vertex)
    #             visited.append(vertex)
    #             # paths.append(vertex) # queue ?
    #             paths.append(queue) # queue ?
    #             print('paths', paths)
    #             if vertex == target:
    #                 return True
    #             next_layer = self.vertices[vertex]
    #             for node in next_layer:
    #                 # duplicate the path then append each child to en.. ?
    #                 # 
    #                 if node not in queue and node not in visited:
    #                     queue.append(node)
        


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


# bfs wrong
#     def bfs(self, starting_vertex, target): 
#         if starting_vertex == target:       
#             return [starting_vertex, target]
#         visited = []
#         queue = deque()
#         queue.append(starting_vertex)
#         paths = []
#         while queue:
#             vertex = queue.popleft()
#             if vertex not in visited:
#                 visited.append(vertex)
#                 next_layer = self.vertices[vertex]
#                 for node in next_layer:
#                     if node == target:
#                         print(visited, queue)
#                         print('True', paths)
#                         return True
#                     if node not in queue and node not in visited:
#                         queue.append(node)
#                         if vertex == starting_vertex:
#                             paths.extend(['path', vertex, node])
#                             print('initial path', paths)
#                         elif vertex in paths:
#                             for i in range(len(paths)):
#                                 if paths[i] == vertex:
#                                     paths.insert(i+1, node)
#                             print('next path', paths)
#         path_str = ''.join(paths)
#         all_paths = path_str.split('path')
#         all_paths = list(filter(None, all_paths))
#         print(all_paths)
#         targeted_path = [path for path in all_paths if target in path]
#         return list(targeted_path[0]) if targeted_path else False