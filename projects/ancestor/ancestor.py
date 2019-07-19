
def earliest_ancestor(ancestors, starting_node):
    '''Create graph from pairs - reverse relations for DFT'''
    vertices = {}
    for i in ancestors:
        if i[1] not in vertices:
            vertices[i[1]] = set()
        if i[0] not in vertices:
            vertices[i[0]] = set()
        vertices[i[1]].add(i[0])
    return vertices

def earliest_ancestor(test_ancestors, starting_vertex, visited=None):
    ancestors = createGraph(test_ancestors)
    visited = [False]*(len(ancestors)+1)
    stack = []
    stack.append(starting_vertex)
    path = []
    s = starting_verte    
    
    while stack:
        starting_vertex = stack[-1]
        stack.pop()
        if (not visited[starting_vertex]):
            path.append(starting_vertex)
            visited[starting_vertex] = True
        for node in ancestors[starting_vertex]:
            if (not visited[node]):
                stack.append(node)

    if s == path[-1]:
        return -1
    else:
        if path[-1] not in ancestors[path[-2]] and path[-2] < path[-1]:
            return path[-2]
        else:
            return path[-1]



 print(earliest_ancestor(test_ancestors, 8))    