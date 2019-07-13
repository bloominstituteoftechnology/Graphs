from util import Stack, Queue
from collections import defaultdict


def dfs(starting_vertex, relative):
    # make a visited list
    visited = []
    # Create a stack
    stack = Stack()
   # put starting vertext in our stack
    stack.push([starting_vertex])
# While the stack isn't empty
    while stack.size() > 0:
         # Let pop off the path
        path = stack.pop()
        # Get the last node or vertex from the path
        node = path[-1]
        # If that node has not been visited
        if node not in visited:
             # Mark the node as visited
            visited.append(node)
            # for each each family member of the relative node
            for family in relative[node]:
                # put the path to that family member node in the stack
                copy_path = path.copy()
                # Add new family members to top of the stack
                copy_path.append(family)

                stack.push(copy_path)
    return visited[-1]


def earliest_ancestor(ancestors, member):
    # create a dictionary list of all relatives
    relatives = defaultdict(list)
    # for every parent and child in ancestors
    for parent, child in ancestors:
        # create a an edge between parent and child
        relatives[child].append(parent)
        # if the member is not in relatives then return negative 1
    if member not in relatives:
        return -1
    # check earliest anscestors with depth first search function recursively
    ancestor = dfs(member, relatives)
    # lets return the ancestor closest to the family member
    return ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                  (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
