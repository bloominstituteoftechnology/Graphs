from collections import deque, defaultdict


def earliest_ancestor(ancestors, starting_node):
    graph = create_graph(ancestors)
    stack = deque()
    paths = []
    
    stack.append([starting_node])

    while len(stack):
        current_path = stack.pop()
        current_vertex = current_path[-1]

        if current_vertex in graph:
            for neighbor in graph[current_vertex]:
                new_path = list(current_path)
                new_path.append(neighbor)
                stack.append(new_path)
        elif current_vertex != starting_node:
            if not len(paths):
                paths.append(current_path)
            elif len(current_path) > len(paths[0]) or (
                len(current_path) == len(paths[0]) and current_path[-1] < paths[0][-1]
            ):
                paths = [current_path]

    return paths[0][-1] if len(paths) else -1

def create_graph(edges):

    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph


    

