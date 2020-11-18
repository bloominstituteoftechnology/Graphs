
from collections import deque, defaultdict

def earliest_ancestor(ancestors,starting_node):
    graph = createGraph(ancestors)

    earliest_ancestor = (starting_node,0)

    stack = deque()
    stack.append((starting_node,0))
    visited = set()

    while len(stack)>0:
        curr = stack.pop()
        currNode, dist = curr[0],curr[1]
        visited.add(curr)

        if currNode not in graph:
            if dist > earliest_ancestor[1]:
                earliest_ancestor = curr
            elif ((dist == earliest_ancestor[1]) and (currNode < earliest_ancestor[0])):
                earliest_ancestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor,dist+1))
    
    if earliest_ancestor[0] != starting_node:
        return earliest_ancestor[0]
    else:
        return -1

# vertices = {}   
# ancestors = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[8,9],[11,8],[10,1]]

def createGraph(paths):
        graph = defaultdict(set)
        for edge in paths:
            origin,dest = edge[0],edge[1]
            graph[dest].add(origin) 
        return graph

