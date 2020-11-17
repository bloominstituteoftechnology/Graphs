"""
UPER:
Earliest Ancestor
Understand:
Edges denoting parent child relationship


Plan:
1. Translate the problem into graph terminology
* vertices - user (parent/child)
* edges - parent child relationship between two users
* weights - no
* paths - a user's family tree

2. Build your graph (if needed)
build graph based on edges we're given
directed edge to its ancestor/parents

3. Traverse the graph
traverse all paths starting from starting node
keep track of furthest node found with loweet user id
output that node

"""
from collections import deque
from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    earliestAncestor = (starting_node, 0) # node and distance
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        if currNode not in graph:
            if distance > earliestAncestor:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append(ancestor, distance + 1)

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def createGraph(edges):
        graph = defaultdict(set)
        for edge in edges:
            ancestors, child = edge[0], edge[1]
            graph[child].add(ancestor)
        return graph
