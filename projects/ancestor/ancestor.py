import sys
from collections import defaultdict


def dfs(individual, family):
        if individual not in family:
            return individual
        # if not visited:
        #     visited = set()
        # if individual not in visited:
        #     visited.add(individual)
        # print(individual, family[individual])
        parent = family[individual][0]
        # print(parent, dfs(parent))
        ancestor = dfs(parent, family)
        print(parent, ancestor)


def earliest_ancestor(dataset, individual):
    family = defaultdict(list)
    for parent, child in dataset:
        family[child].append(parent)
    print(family)
    if individual not in family:
        return -1
    ancestor = dfs(individual, family)
    return ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)