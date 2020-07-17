
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
    # build graph to traverse
    g = Graph()
     # populate w verts
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
         # build edges
        g.add_edge(i[1], i[0])
    # init a Q and add starting vertex as a list
    q = Queue()
    q.enqueue([starting_node])
    # set max path and earliest ancestor -1 for return if no neighbors
    max_path = 1
    earliest = -1
    # while the Q has elements
    while q.size() > 0:
        # we pull the first element into our path
        path = q.dequeue()
        # set v to the last index of path
        v = path[-1]
        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        for next_item in g.verts[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest

