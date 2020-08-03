from collections import deque
class Graph():
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()
    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)
    
    def get_neighbors(self, node):
        return self.graph[node]
    
    def size(self):
        return len(self.graph)
​class Stack():
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
​
​
def build_graph(ancestors):
    g = Graph()
    for parent, child in ancestors:
        # add the nodes
        g.add_node(parent)
        g.add_node(child)
        # connect child to parent
        g.add_edge(child, parent)
​
    return g
​
def dft_recursive(vertex, g):
    node_id, distance = vertex
    parents = g.get_neighbors(node_id)
​
    if len(parents) == 0:
        return vertex
​
    ancient_one = vertex
​
    for parent in parents:
        parent_node = (parent, distance + 1)
        pair = dft_recursive(parent_node, g)
​
        if pair[1] > ancient_one[1]:
            ancient_one = pair
        elif pair[1] == ancient_one[1] and pair[0] < ancient_one[0]:
            ancient_one = pair
        
    return ancient_one 
​
    # track distance with a tuple: (node_id, distance)
    # Base case: return if we hit a leaf
    # Compare as we iterate
    # Return after we iterate
​
## Algorithms that build on our traversals, and work on weighted graphs:
    # Dijkstra's
    # A*
​
def dft_recursive_2(path, g):
    current_node = path[-1]
​
    parents = g.get_neighbors(current_node)
​
    if len(parents) == 0:
        return path
​
    longest_path = path
​
    for parent in parents:
        path_copy = list(path)
        path_copy.append(parent)
​
        result = dft_recursive_2(path_copy, g)
​
        if len(result) > len(longest_path):
            longest_path = result
​
        elif len(result) == len(longest_path):
            if result[-1] < longest_path[-1]:
                longest_path = result
​

def earliest_ancestor(ancestors, starting_node):
    g = build_graph(ancestors)
    node = (starting_node, 0)
    ancient_one = dft_recursive(node, g)
​
    if ancient_one[0] == starting_node:
        return -1
    else:
        return ancient_one[0]


