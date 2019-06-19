'''

anc = -1
p_found = false

for anc in ancestors:
    if anc[1] == starting_node:
        p_found = true
        break
if not p_found:
    return anc

in_search = true
upd_list = []
a_list = [(3,6),(5,6)]

while in_search:
    in_search = false
    for c_p in a list:
        upd_list.append(get_child_parents(#)) #method should return one or two parent tuples
    if len(upd_list) != 0:
        a_list = upd_list
        upd_list = []
        in_search = true

# We should now have a list of the top ancestors  tuples(index0 is ancestor)
anc = a_list[0[0]]
for anc_t in a_list:
    if anc_t[0] < anc:
      anc = anc_t[0]
return anc

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

Example input
  6
  [parent|child]
  [1     |    3]
  [2     |    3]
  [3     |    6]
  [5     |    6]
  [5     |    7]
  [4     |    5]
  [4     |    8]
  [8     |    9]
  [11    |    8]
  [10    |    1]
Example output
  10
'''
from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    # print(graph)

    def dfs(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1

        distances = dict()

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]  # last element in path array
            if vertex not in visited:
                if vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]  # kinda like path.copy()
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            # works like a break but goes on to the next iteration
                            distances[neighbor] = len(path_new)
                            continue
                    visited.add(vertex)
        # print(distances)
        results = []
        max_length = -1
        for k, v in distances.items():  # we find the max length
            if v > max_length:
                max_length = v

        for k, v in distances.items():
            if v == max_length:
                results.append(k)

        return min(results)
        # print(results)

    return dfs(starting_node)


lca_index = 6
lca_arr = {
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1)
}

print(earliest_ancestor(lca_arr, lca_index))
