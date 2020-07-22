from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    parent_dict = defaultdict(list)
    for pair in ancestors:
        parent_dict[pair[1]].append(pair[0])

    if starting_node not in parent_dict:
        return -1

    def recursive_ancestor(child, level=0):
        nonlocal parent_dict
        if child not in parent_dict:
            return (child, level)
        else:
            candidates = []
            for parent in parent_dict[child]:
                candidates.append(recursive_ancestor(parent, level + 1))
            return sorted(candidates, key=lambda x: (-x[1], x[0]))[0]

    return recursive_ancestor(starting_node)[0]
