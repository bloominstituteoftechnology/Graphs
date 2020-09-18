from collections import deque
#Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.

def earliest_ancestor(vertices, starting_node):
    # the destination is always the 0 index
    graph = buildGraph(vertices)
    # print(graph)

    # if the input has no parents
    if starting_node not in graph: #-> 10, 2, 4, 11
        print('node is not key in graph')
        return -1 #highest ancestor
    # if parent[0] == destination:
    #         print(parent[0])
        # if v == starting_node:
        #     print(v)
    # loop through all vertices
    # queue = deque()
    # queue.append(starting_node)
    # print(f'The queue has {queue}')
    # visited = set()
    # while len(queue) > 0:
    #     node = queue.pop()
    #     if node not in visited:
    #         # print(f'the node is {node}')
    #         visited.add(node)
    #         # If the input individual has no parents, the function returns -1
    #         if node not in vertices:
    #             # we want to find parent which is the key, the child is the value
    #             return -1
    #         for neighbor in vertices[node]:
    #             # print(f'The neighbor is {neighbor}')
    #             queue.append(neighbor)
    # # return ancestor that is the farthest distance away and lowest ID, 9's furthest ancester is 4
    
    # return queue

# def findAncestor(self, node, destination):
#     for i in range(len(vertices)):
#         if vertices[i][1] == node:
#             return vertices[i]
#         else:
#             if vertices[0] == vertices[1]:
#                 print(vertices[0])

def buildGraph(test_ancestors):
    graph = {}
    for edge in test_ancestors:
        child, parent = edge[1], edge[0]
        # if there is a deplicate key
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = { parent }
    return graph


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 4)) # 10)
# print(earliest_ancestor(vertices, 2)) # -1)
# print(earliest_ancestor(vertices, 3)) # 10)
# print(earliest_ancestor(vertices, 4)) # -1)
# print(earliest_ancestor(vertices, 5)) # 4)
# print(earliest_ancestor(test_ancestors, 6)) # 10)
# print(earliest_ancestor(vertices, 7)) # 4)
# print(earliest_ancestor(vertices, 8)) # 4)
# print(earliest_ancestor(vertices, 9)) # 4)
# print(earliest_ancestor(vertices, 10)) # -1)
# print(earliest_ancestor(vertices, 11)) # -1)
