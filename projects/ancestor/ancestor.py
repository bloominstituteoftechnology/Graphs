# from util import Queue
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
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    
    # queue = Queue()
    # current_node = starting_node
    # relationships = {}
    
    # for ancestor in ancestors: 

    #     parent = ancestor[0]
    #     child = ancestor[1]

    #     if child not in relationships:
    #         relationships[child] = set()
    #     relationships[child].add(parent)

    # if starting_node in relationships:
    #     queue.enqueue(relationships[current_node])
    # else:
    #     return -1

    # while True:
    #     relations = queue.dequeue()
    #     current_node = min(relations)
    #     if current_node not in relationships:
    #         return current_node
    #     else:
    #         queue.enqueue(relationships[current_node])

# create the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
# do a BFS storing the path
    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        print(path)
        v = path[-1]
        if (len(path) >= max_path_length and v < earliest_ancestor):
            earliest_ancestor = v
        if(len(path) > max_path_length):
            max_path_length = len(path)
            earliest_ancestor = v
        for neighbor in graph.get_neighbors(v):
            print(graph.get_neighbors(v))
            path_copy = list(path)
            path_copy.append(neighbor)
            print(path_copy)
            q.enqueue(path_copy)
    print(graph.get_neighbors(1))
    return earliest_ancestor
