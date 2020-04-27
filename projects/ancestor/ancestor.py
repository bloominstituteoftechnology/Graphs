from graph import Graph
from util import Stack, Queue


# def earliest_ancestor(ancestors, starting_node):
#     oldest = -1
#     relatives = {}
#     for pair in ancestors:
#         if pair[1] == starting_node:
#             if pair[0] > oldest:
#                 oldest = pair[0]
#             relatives[pair[0]] = pair[1]
#     for pair in ancestors:
#         if pair[1] in relatives.keys():
#             if pair[0] > oldest:
#                 oldest = pair[0]
#             relatives[pair[0]] = pair[1]
#     if len(relatives) > 0:
#         oldest = list(relatives.keys())[-1]
#     print(relatives)
#     return oldest


def earliest_ancestor(ancestors, starting_node):
    oldest = -1
    relatives = Stack()
    met = set()

    # get parents
    for pair in ancestors:
        if pair[1] == starting_node:
            if pair not in met:
                relatives.push(pair)

    while relatives.size() > 0:
        current_pair = relatives.pop()
        oldest = current_pair[0]
        for pair in ancestors:
            if pair not in met:
                if pair[1] == oldest:
                    relatives.push(pair)
                    met.add(pair)

    return oldest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 8))
