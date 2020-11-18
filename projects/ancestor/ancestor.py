"""
Understand

Plan
1. Translate the problem into graph terminology
vertex - user
edges - parent-child relationship between two nodes
weights - n/a
path - a user's family tree

2. Build your graph (if needed)
build graph based on edges we're given, each user has a directed edge to its ancestor/parent

3. Traverse the graph
traverse all paths starting from starting_node, keep track of farthest node found with the lowest user id
simply output that node
"""
from collections import deque
from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    earliestAncestor = (starting_node, 0) # id, distance
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        if currNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

def createGraph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
