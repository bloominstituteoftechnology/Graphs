from collections import deque

def earliest_ancestor(ancestors, starting_node):
    """
    Understand:
    Make a function that takes any given number in a dataset and returns the earliest known ancestor.

    Plan:

    1. Translate into graph terminoloy
    vertex = individual 
    edge = connection of parent and child
    weight = None

    2. Build the graph
    We will need to do a dfs to traverse the graph all the way down to the earliest (lowest) ancestor (number). We will stop once we find the earliest ancestor which is why we use a DFS.

    """
    class Stack():
        def __init__(self):
            self.stack = []
        def push(self, value):
            self.stack.append(value)
        def pop(self):
            if self.size() > 0:
                return self.stack.pop()
            else:
                return None
        def size(self):
            return len(self.stack)

    ancestors = {}

    visited = set()
    stack = deque()
    stack.append([starting_node])

    # while len(stack) > 0:
    #     currPath = stack.pop()
    #     currNode = currPath[-1]
    #     if currNode == destination_vertex:
    #         return currPath
    #     if currNode not in visited:
    #         visited.add(currNode)
    #         for neighbor in self.vertices[currNode]:
    #             newPath = list(currPath)
    #             newPath.append(neighbor)
    #             stack.append(newPath)

    while len(stack) > 0:
        currPath = stack.pop()
        currNode = currPath[-1]
        if currNode not in visited:
            visited.add(currNode)
            for individual in ancestors[currNode]:
                newPath = list(currPath)
                newPath.append(individual)
                stack.append(newPath)