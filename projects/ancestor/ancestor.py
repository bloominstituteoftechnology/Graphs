from collections import deque

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    # will try flipping order so that children are
    # vertecies and parents are edges. This should 
    # be a better implemention by allowing for faster
    # lookups









    # brute force method is to compare each value to the
    # starting node and add its key to a stack to check next
    # so that while there is a stack, we keep traversing level
    # by level until the stack is empty and we've reached the end

    # ancestors are tuples containing (parent,child) items
    for parent,child in ancestors:      
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = {child}

    # search graph using children
    def search_by_val(val, d):
        keys = [] # list for children with more than 1 parent
        for k,v in d.items():
            if val in v and k not in keys:
                keys.append(k)

        return keys
    
    # stack for dfs
    stack = deque()
    stack.append([starting_node])

    # list to hold all routes traversed
    geneology = []

    # dfs algo varient
    while len(stack) > 0:
        path = stack.pop()
        child = path[-1]

        # similar to check neighbors
        parents = search_by_val(child, graph) 

        # create and add paths to be searched to que
        if len(parents) > 0:
            for parent in parents:
                new_path = list(path)
                new_path.append(parent)
                stack.append(new_path)
        # if no parent found, traversal along this path is complete
        else:
            geneology.append(path)

    # for more than 1 parent for same child
    result = {}
    for path in geneology:
        l = len(path)
        if l not in result:
            result[l] = [path[-1]]
        else:
            result[l].append(path[-1])
    
    anc = max(result, key = result.get)

    # path should include a min child and parent
    if anc < 2:
        return -1
    else:
        return result[anc][-1]


'''
quick test data
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10

Graph Representation
{
    1 : 3
    2 : 3
    3 : 6
    5 : 6, 7
    4 : 5, 8
    8 : 9
    11: 8
    10: 1
}
'''
geneology = [
    (1,3), (2,3), (3,6), (5,6),
    (5,7), (4,5), (4,8), (8,9),
    (11,8), (10,1)
            ]
print(earliest_ancestor(geneology, 8))

    
