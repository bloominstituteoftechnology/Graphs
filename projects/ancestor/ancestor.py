from util import Queue

def get_ancestor(ancestors, child):
    heirs = []
    for heir in ancestors:
        if heir[1] == child:
            heirs.append(heir[0])
    return heirs

def earliest_ancestor(ancestors, starting_node):
    #create empty queue
    q = Queue()
    #add starting node to queue
    q.enqueue([starting_node])
    #create set to store visited vertices
    visited = set()
    #initialize path length
    path_len = 1
    #sets oldest parent as -1 for if no parent
    oldest_parent = -1
    
    #while size of q is greater than 0
    while q.size() > 0:
        # dequeue first path
        path = q.dequeue()
        # grab the last vertex from the path
        cur_node = path[-1]

        # if that vertex has not been visited
        if cur_node not in visited:
            # mark as visited
            visited.add(cur_node)

        # checks for need to update
        if len(path) >= path_len and cur_node < oldest_parent or len(path) > path_len:
            #updates path length
            path_len = len(path)
            #updates oldest parent
            oldest_parent = cur_node

        # then add a path to its parent to the back of the queue
        for parent in get_ancestor(ancestors, cur_node):
            #copy path
            path_copy = list(path)
            #append parent to back
            path_copy.append(parent)
            q.enqueue(path_copy)

    return oldest_parent

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)


# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()

#     def add_edge(self, v1, v2):
#         self.vertices[v1].add(v2)

#     def get_neighors(self, vertex):
#         return self.vertices[vertex]

# ## Build a path like we did in search
# ## But we don't know when to stop until we've seen everyone
# def build_graph(ancestors):
#     graph = Graph()
#     for parent, child in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)
#         graph.add_edge(child, parent)
#     return graph

# def earliest_ancestor(ancestors, starting_node):
#     graph = build_graph(ancestors)

#     s = Stack()

#     visited = set()

#     s.push([starting_node])

#     longest_path = [starting_node]
#     aged_one = -1

#     while s.size() > 0:
#         path = s.pop()
#         current_node = path[-1]

#         # if path is longer, or path is equal but the id is smaller
#         if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
#             longest_path = path
#             aged_one = longest_path[-1]

#         if current_node not in visited:
#             visited.add(current_node)

#             parents = graph.get_neighors(current_node)

#             for parent in parents:
#                 new_path = path + [parent]
#                 s.push(new_path)

#     return aged_one