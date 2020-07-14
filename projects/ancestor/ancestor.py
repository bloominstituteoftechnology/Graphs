
## Build a Queue Class
class Queue():
    ## Initialize Method
    def __init__(self):
        self.queue = []

    ## Enqueue Method
    def enqueue(self, value):
        self.queue.append(value)

    ## Dequeue Method
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    ## Sizing Method
    def size(self):
        return len(self.queue)


## Build a Graph Class
class Graph():
    ## Initialize Method
    def __init__(self):
        self.verts = {}

    ## Add Vertex Method
    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()

    ## Add Edge Method
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    #pass

    ancestors = []
