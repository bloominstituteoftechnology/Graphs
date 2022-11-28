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
        self.verts = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)
        
def earliest_ancestor(ancestors, starting_node):
    # build graph
    g = Graph()
    # add verts to graph in parent child pairs
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    # add edges
        g.add_edge(i[1], i[0])
    # start adding stuff to queue
    q = Queue()
    q.enqueue([starting_node])
    # set longest path and earliest to -1 if no neighbors
    longest_path = 1
    earliest = -1
    # while the Q has elements
    while q.size() > 0:
    # add first element to path
        path = q.dequeue()
    # set v to the last index of the path
        v = path[-1]
        if(len(path) >= longest_path and v < earliest) or (len(path) > longest_path):
            earliest = v
            longest_path = len(path)
        for next_item in g.verts[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest



    