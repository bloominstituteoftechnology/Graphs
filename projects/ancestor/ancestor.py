"""
Understand
    1   2
     \ /
      3
       \
        6
input: [(1, 3), (2, 3), (3, 6)]

starting node: 6
output: 1 (1 and 2 are tied but 1 has a lower id)

starting node: 1
output: -1 (1 has no ancestor)

Plan
1. Translate the problem into graph terminology
vertex - a person (in this case, we're given their ids)
edge - parent-child relationship between two people
path - a person's family tree
weight - not needed, all edges are equal and have no value/cost related to them

2. Build your graph
Build a graph by using the parent-child relationships/edges we're given. Each node in the
graph will have an outgoing/directed edge to its parent/ancestor.

3. Traverse the graph
We traverse the graph while keeping track of the node's distances from the starting node
and keep track of the terminal node with the lowest id and greatest distance.
A terminal node will have no outgoing edges, meaning it has no more ancestors. A terminal node
doesn't mean it's the earliest ancestor though, so we need to consider the terminal node that is
the greatest distance from the starting node (that also has the lowest id).

In this case, we can use a depth-first traversal (DFT) to traverse all of the starting node's
ancestors and return the earliest one with the lowest id.
"""
from collections import deque
from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    # A tuple with a node and its distance from the starting node
    # At the beginning, the starting node's earliest ancestor is itself
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        # This checks if the node is a terminal node
        if currNode not in graph:
        # Only consider terminal nodes that have a greater distance than the ones we've found so far
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            # If there's a tie then choose the ancestor with the lower id
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    # If the starting node's earliest ancestor is itself, then just return -1
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

# Creates a graph where the keys are a node and its values are its ancestors
def createGraph(edges):
    # This convenience method simply allows us to initialize default values when assigning
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
