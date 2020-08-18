import collections

# Naive First Pass Iterative Solution

# def earliest_ancestor(ancestors, node):
#     # we want the earliest ancestor aka the deepest ancestor so I will use a dfs search
#     # loop through ancestors to create graph
#     # standard dfs add starting node to stack
#     # while stack isn't empty pop last
#     # loop through parents adding them to a list
#     # keep track of generations by using a 2d list and adding parents list into 2d list
#     # get last list in 2d list and check count
#     # if count is 2 compare which value is smaller
#     stack = []
#     dict = {}
#     for parent, child in ancestors:
#         if child not in dict:
#             dict.setdefault(child, list([parent]))
#         else:
#             dict[child].append(parent)
#     print(dict)
#     stack.append(node)
#     generations = []
#     while stack:
#         child = stack.pop()
#         parents = []
#         if child in dict:
#             for parent in dict[child]:
#                 if parent in dict:
#                     stack.append(parent)
#                 if len(parents) < 2:
#                     parents.append(parent)
#             generations.append(parents)
#             print(f"Parents: {generations}")
#         else: 
#             generations.append(parents)
#             break
#     earliest_gen = generations[-1]
#     print(f"Earliest gen: {earliest_gen}")
#     earliest_ancestor = None
#     if len(earliest_gen) is 0:
#         return -1
#     else:
#         for parent in earliest_gen:
#             if earliest_ancestor is None:
#                 earliest_ancestor = parent
#             if parent < earliest_ancestor:
#                 earliest_ancestor = parent
#     print(f"Earliest Ancestor: {earliest_ancestor}")
#     return earliest_ancestor

# Second Pass Recursive Solution

# def earliest_ancestor(ancestors, node, dict=None, generations=None):
#     if dict is None:
#         dict = {}
#         generations = []
#         for parent, child in ancestors:
#             if child not in dict:
#                 dict.setdefault(child, list([parent]))
#             else:
#                 dict[child].append(parent)
#     if node in dict:
#         if len(dict[node]) is 2:
#             smallest = dict[node][0]
#             if dict[node][1] < smallest:
#                 smallest = dict[node][1]
#             generations.append(smallest)
#             if dict[node][0] in dict:
#                 return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#             if dict[node][1] in dict:
#                 return earliest_ancestor(ancestors, dict[node][1], dict, generations)
#         else:
#             generations.append(dict[node][0])
#             if dict[node][0] in dict:
#                 return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#     else:
#         generations.append(-1)
#     return generations[-1]

# 3rd Pass Recursive Solution Accounting for some edge cases

# def earliest_ancestor(ancestors, node, dict=None, generations=[]):
#     if dict is None:
#         dict = {}
#         for parent, child in ancestors:
#             if child not in dict:
#                 dict.setdefault(child, list([parent]))
#             else:
#                 dict[child].append(parent)
#     if node in dict:
#         if len(dict[node]) is 2:
#             if dict[node][0] < dict[node][1]:
#                 generations.append(dict[node][0])
#             else:
#                 generations.append(dict[node][1])
#             if dict[node][0] and dict[node][1] in dict:
#                 earliest_ancestor(ancestors, dict[node][0], dict, generations)
#                 return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#             elif dict[node][0] in dict and dict[node][1] not in dict:
#                 return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#             elif dict[node][1] in dict and dict[node][0] not in dict:
#                 return earliest_ancestor(ancestors, dict[node][1], dict, generations)
#         else:
#             generations.append(dict[node][0])
#             if dict[node][0] in dict:
#                 return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#     else:
#         generations.append(-1)
#     return generations[-1]

# 4th pass just restructured existing code from 3

# def earliest_ancestor(ancestors, node, dict=None, generations=[]):
    # if dict is None:
    #     dict = {}
        # for parent, child in ancestors:
        #     if child not in dict:
        #         dict.setdefault(child, list([parent]))
        #     else:
        #         dict[child].append(parent)
#     if node not in dict:
#         generations.append(-1)
#     elif len(dict[node]) is 1:
#         generations.append(dict[node][0])
#         if dict[node][0] in dict:
#             return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#     else:
#         if dict[node][0] < dict[node][1]:
#             generations.append(dict[node][0])
#         else:
#             generations.append(dict[node][1])
#         if dict[node][0] and dict[node][1] in dict:
#             earliest_ancestor(ancestors, dict[node][0], dict, generations)
#             return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#         elif dict[node][0] in dict and dict[node][1] not in dict:
#             return earliest_ancestor(ancestors, dict[node][0], dict, generations)
#         elif dict[node][1] in dict and dict[node][0] not in dict:
#             return earliest_ancestor(ancestors, dict[node][1], dict, generations)
        
#     return generations[-1]

# My dfs solutions passed the test but did not account for some edge cases
# After a little advice from a friend implemented a bfs solution
# Fifth Pass Solution Breadth First Search

def earliest_ancestor(ancestors, node):
    dict = {}
    generations = []
    for parent, child in ancestors:
        if child not in dict:
            dict.setdefault(child, list([parent]))
        else:
            dict[child].append(parent)
    queue = collections.deque([])
    queue.append(node)
    if node not in dict:
        return -1
    while queue:
        child = queue.popleft()
        if child in dict:
            if len(dict[child]) is 2:
                queue.append(dict[child][0])
                queue.append(dict[child][1])
                if dict[child][0] < dict[child][1]:
                    generations.append(dict[child][0])
                else:
                    generations.append(dict[child][1])
            elif len(dict[child]) is 1:
                queue.append(dict[child][0])
                generations.append(dict[child][0])
            else:
                generations.append(-1)

    return generations[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (20, 4), (21, 20)]
# print(earliest_ancestor(test_ancestors, 6)) # should be 21
print(earliest_ancestor(test_ancestors, 9))