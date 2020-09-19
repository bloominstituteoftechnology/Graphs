
class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

#Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.

def earliest_ancestor(vertices, starting_node):
    graph = buildGraph(vertices)
    # if the input has no parents
    if starting_node not in graph: #-> 10, 2, 4, 11
        return -1
    # loop through all vertices
    queue = Queue()
    queue.enqueue([starting_node])
    visited = set()
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
        if current_node not in visited:
            visited.add(current_node)
            # If the input individual is highest ancestor, return node
            if current_node not in graph:
                continue

            for neighbor in graph[current_node]:
                newPath = list(current_path)
                newPath.append(neighbor)
                queue.enqueue(newPath) 
    return current_node

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
print(earliest_ancestor(test_ancestors, 6)) # 10)
print(earliest_ancestor(test_ancestors, 2)) # -1)
print(earliest_ancestor(test_ancestors, 3)) # 10)
print(earliest_ancestor(test_ancestors, 4)) # -1)
print(earliest_ancestor(test_ancestors, 5)) # 4)
print(earliest_ancestor(test_ancestors, 6)) # 10)
print(earliest_ancestor(test_ancestors, 7)) # 4)
print(earliest_ancestor(test_ancestors, 8)) # 4)
print(earliest_ancestor(test_ancestors, 9)) # 4)
print(earliest_ancestor(test_ancestors, 10)) # -1)
print(earliest_ancestor(test_ancestors, 11)) # -1)
