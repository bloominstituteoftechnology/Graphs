
def earliest_ancestor(ancestors, starting_node):
    # create a hash table called vertices to store ancestors
    vertices = {}
    # add all ancestors to vertices dict
    for ancestor in ancestors:
        vertices[ancestor[1]] = set()
        vertices[ancestor[0]] = set()
    # add all ancestors' edges (ancestors)
    for ancestor in ancestors:
        vertices[ancestor[1]].add(ancestor[0])
    # if starting vertex has no ancestors
    if not vertices[starting_node]:
        return -1
    # if it has ancestors
    else:
        # create an empty list for stack
        stack = []
        # keep track of depth
        depth = {starting_node:0}
        # add the starting vertex to the stack
        stack.append(starting_node)
        # while there are ancestors in the stack
        while stack:
            # pop off the most recently added vertex
            current_vert = stack.pop()
            # get a list of its ancestors
            edges = vertices[current_vert]
            # loop through vertex's edges
            for edge in edges:  
                # track the edge's depth as being one greater than the current node's
                depth[edge] = depth[current_vert] + 1
                # add edge to top of the stack
                stack.append(edge)
        # return the max depth(s)
        max_value = max(depth.values())
        # return the minimum key 
        return min([k for k, v in depth.items() if v == max_value])


if __name__ == '__main__':

    # ancestors
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), 
    (4, 8), (8, 9), (11, 8), (10, 1)]
    
    print(earliest_ancestor(test_ancestors, 9))