from collections import deque, defaultdict

def earliest_ancestor(ancestors, starting_node):
    #child pair with no parent
    graph = create_graph(ancestors)
    stack = deque()
    stack.append((starting_node, 0)) # distance from node
    visited = set()
    earliestAncestor = (starting_node, 0)

    while len(stack) > 0:
        current = stack.pop()
        current_node, distance = current[0], current[1]
        visited.add(current)

        if current_node not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = current
            elif distance == earliestAncestor[1] and current_node < earliestAncestor[0]:
                earliestAncestor = current
        else:
            for ancestor in graph[current_node]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def create_graph(edges):
    # every added dict should a deafult value set()
    graph = defaultdict(set)

    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)

    return graph