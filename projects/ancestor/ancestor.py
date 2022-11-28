class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
 

# 1. Describe the problem in graph terminology
## What are our nodes? -> numbers/people
## What are our edges? -> if a descendant/parent
## Directed graph

# 2. Build your graph or write getNeighbors()
## Can do either

# 3. Choose your fighter
## Which algorithm would you use in this situation?
### BFS, DFS, BFT, DFT

## Search or a traversal?
### more like a traversal: visit every node possible from your starting node

## Depth vs Breadth
## BF --> shortest path
## DF --> heads to leaves first

## DF can be recursive, but not BF

# build dictionary of child: [parents]
# loaded up into graph class
# iterate through all ancestors
# (parent, child)

def getParents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1] == node:
            parents.append(pair[0])
    return parents

def dft_recursive(ancestors, node, distance):
    parents = getParents(ancestors, node)

    aged_one = (node, distance)

    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance + 1)
        if pair[1] > aged_one[1]:
            aged_one = pair

    return aged_one

def earliest_ancestor(ancestors, starting_node, distance=0):
    aged_one = dft_recursive(ancestors, starting_node, distance)

    if aged_one[0] == starting_node:
        return -1

    return aged_one[0]
    ## iterate over all ancestors,
    ## add each node to the graph
    ## add each edge to the graph

    ## run a traversal
    ## modify it so as you go, you keep track of the node that's farthest away

    # g = Graph()
    # q = Queue()
    
    # q.enqueue([starting_node])
    # max_length = 1
    # earliest = -1

    # for pair in ancestors:
    #     g.add_vertex(pair[0])
    #     g.add_vertex(pair[1])
    #     g.add_edge(pair[1], pair[0])

    # while q.size() > 0:
    #     path = q.dequeue()
    #     curr = path[-1]

    #     if len(path) > max_length:
    #         max_length = len(path)
    #         earliest = curr
    #     elif len(path) == max_length and curr < earliest:
    #         earliest = curr

    #     for neighbor in g.get_neighbors(curr):
    #         q.enqueue(path + [neighbor])

    # return earliest