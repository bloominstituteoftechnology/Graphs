from collections import deque

def earliest_ancestor(ancestors, starting_node):
    
    if len(ancestors) == 0:
        return "empty list"

    graph = create_graph(ancestors)
    visited = set()
    stack = deque()
    stack.append(starting_node)
    print(graph)
    count = 0

    while len(stack) > 0:
        currNode = stack.pop()
        parents = set()
        count = count + 1

        if currNode not in visited:
            visited.add(currNode)
            for node in graph:
                if graph[node].__contains__(currNode):
                    parents.add(node)

            if parents:
                stack.append(min(parents))
            else:
                if count == 1:
                    print(-1)
                    return -1
                print(currNode)
                return currNode
               


def create_graph(ancestors):
    graph = {}
    for parent, child in ancestors:
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = {child}
    return graph


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 10)