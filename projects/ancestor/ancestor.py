class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)

# This will be similar to depth first
# def earliest_ancestor(ancestors, starting_node):
#     # build the graph
#     g = Graph()

#     # Add the parents
#     for parent in ancestors:
#         g.add_vertex(parent[0])
#         g.add_vertex(parent[1])

#         # add in the edge
#         g.add_edge(parent[0], parent[1])

#     # start the queue to handle the path
#     q = Queue()
#     q.enqueue([starting_node])

#     # initialize with -1 for no neighbors
#     longest_path = 1
#     earliest = -1

#     while q.size() > 0:
#         path = q.dequeue()
#         last_vertex = path[-1]

#         if (len(path) >= longest_path and last_vertex < earliest) or \
#             (len(path) > longest_path):
#             earliest = last_vertex
#             longest_path = len(path)
#         # look at neighbors
#         for next_item in g.vertices[last_vertex]:
#             path_copy = list(path)
#             path_copy.append(next_item)
#             q.enqueue(path_copy)
#     return earliest

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors: # tuple
        # add vertexes into graph, then edges
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edge(pair[0], pair[1])
        
        # now we need to traverse the graph
        # optionally BFS. DFS probably more efficient
        q = Queue()
        q.enqueue([starting_node])

        # set some vars to compare 
        max_path_length = 1
        earliest_ancestor = -1

        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]

            # if gone the wrong way, we want the lowest possible value
            if (len(path) >= max_path_length and last_vertex < earliest_ancestor) or len(path) > max_path_length:
                earliest_ancestor = last_vertex
                max_path_length = len(path)

                # get neighbors
                for neighbor in graph.vertices[last_vertex]:
                    path_copy = list(path)
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)

    return earliest_ancestor
