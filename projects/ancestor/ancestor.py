"""
Plan
1. Translate in graph terminology
  vertices - each index in dataset
  edges - connect children to parents
  weights - none
  path - youngest to oldeest

2. Build your graph if needed
  adjacency list


3. Traverse your graph
  farthest distance = depth first
  - hash table to store lengths of the path from starting node

"""
from collections import deque

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    for pair in ancestors:
        parent, child = pair[0], pair[1]

        if parent not in graph:
            graph[parent] = set()

        if child not in graph:
            graph[child] = { parent }
        else:
            graph[child].add(parent)

    stack = deque()
    visited = set()
    path_lengths = {starting_node: 0}

    stack.append(starting_node)

    while len(stack) > 0:
        curr_node = stack.pop()

        if curr_node not in visited:
            visited.add(curr_node)

            for neighbor in graph[curr_node]:
                stack.append(neighbor)
                path_lengths[neighbor] = 1 + path_lengths[curr_node]

    longest_path = max(path_lengths.values())

    solution = min([key for key, value in path_lengths.items() if value == longest_path])

    if solution == starting_node:
        solution = -1

    return solution