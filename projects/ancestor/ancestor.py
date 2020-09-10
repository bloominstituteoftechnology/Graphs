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

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
     
    graph = Graph()
   
    # create vertices
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
   
    # create edges to the vertices
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

   
    # create empty queue
    q = Queue()
   
    # add starting vertex
    q.enqueue([starting_node])
   
    # create set for visited verticies
    visited = set()
    result = []
   
    # while queue is not empty
    while q.size() > 0:
   
        # dequeue list
        path = q.dequeue()
   
        # remove a vert, set the last one to variable
        v = path[-1]
   
        # check if it is in visit, if not add to visited
        if v not in visited:
            visited.add(v)
   
        # creates copy, adds neighbors to queue
        for neighbor in graph.get_neighbors(v):
   
            # makes copy of path
            path_copy = list(path)
   
            # puts neighbor in path copy
            path_copy.append(neighbor)\
   
            # puts path copy in queue
            q.enqueue(path_copy)
   
            # append last element to result
            result.append(path_copy[-1])
            print(path_copy)
   
        # if empty return -1
        if result == []:
            return -1

    return result[-1]