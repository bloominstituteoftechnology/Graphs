arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    vertices = {}

    def dfs(start, end):
        if start == end:
            return []
        stack = []
        stack.append([start])
        visited = set()
        while stack:
            curr_path = stack.pop()
            curr_node = curr_path[-1]
            if curr_node == end:
                return curr_path
            elif curr_node not in vertices:
                continue
            if curr_node not in visited:
                visited.add(curr_node)
                for edge in vertices[curr_node]:
                    new_path = list(curr_path)
                    new_path.append(edge)
                    stack.append(new_path)
        return stack

    for start, end in ancestors:
        if start not in vertices:
            vertices[start] = set()
        vertices[start].add(end)
    max_len = 0
    res = -1
    for vertex in vertices:
        path = dfs(vertex, starting_node)
        if path:
            if len(path) > max_len:
                max_len = len(path)
                res = path[0]
            elif len(path) == max_len:
                res = path[0] if path[0] < res else res
    return res
        
print(earliest_ancestor(arr, 8))