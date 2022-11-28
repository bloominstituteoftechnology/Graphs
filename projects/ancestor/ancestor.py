import collections

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # So I need to build a graph from the input data, or at least a way to get the parents of each node
    # Let's loop through the ancestors and build a dictionary of parents to children, since we will be
    # traversing from the child up to the earliest ancestor

    # Then I need to find the path that is the longest, rather than the shortest
    # If I use breadth first traversal and return the LAST path in the queue, that should be the longest path

    parents_by_child = {}

    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else:
            parents_by_child[child] = [parent]

    # Early exit if the starting node has no parents
    if starting_node not in parents_by_child:
        return -1

    path_queue = collections.deque() # doubly ended queue

    last_path = [starting_node] # this will let us save the last path dequeued

    path_queue.append(last_path)

    while len(path_queue) > 0:
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parents_by_child:
            parents_by_child[oldest_ancestor].sort(reverse=True) # make sure lowest id goes in queue last
            for parent in parents_by_child[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)

    return last_path[-1]

# def earliest_ancestor(ancestors, node):
#     dict = {}
#     generations = []
#     for parent, child in ancestors:
#         if child not in dict:
#             dict.setdefault(child, list([parent]))
#         else:
#             dict[child].append(parent)
#     queue = collections.deque([])
#     queue.append(node)
#     if node not in dict:
#         return -1
#     while queue:
#         child = queue.popleft()
#         if child in dict:
#             if len(dict[child]) is 2:
#                 queue.append(dict[child][0])
#                 queue.append(dict[child][1])
#                 if dict[child][0] < dict[child][1]:
#                     generations.append(dict[child][0])
#                 else:
#                     generations.append(dict[child][1])
#             elif len(dict[child]) is 1:
#                 queue.append(dict[child][0])
#                 generations.append(dict[child][0])
#             else:
#                 generations.append(-1)
#     return generations[-1]

# Dylan DFS

# class Graph:
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertex):
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)

# def earliest_ancestor(data_set, starting_vertex):
#     graph = Graph()
#     for pair in data_set:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         graph.add_edge(pair[1], pair[0])
#     print(graph.vertices)
#     if graph.vertices[starting_vertex] == set():
#         return -1
#     stack = Stack()
#     stack.push([starting_vertex])
#     oldest = []
#     while stack.size() > 0:
#         path = stack.pop()
#         vertex = path[-1]
#         if len(path) > len(oldest):
#             oldest = path
#         if len(path) == len(oldest) and path[-1] < oldest[-1]:
#             oldest = path
#         for neighbor in graph.vertices[vertex]:
#             new_path = path.copy()
#             new_path.append(neighbor)
#             stack.push(new_path)
#     return oldest[-1]