
#Graphs Problem Solving 
#Translate the problem
#Nodes are people
# Edges: when a child has a parent
# build the graph, define get_neighbors

##Choose algo
# I guess either bfs or dfs works here
## my version uses dfs
# how would we know if dfs happened to be faster, check visited 
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set() 
            
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        
class Stack():
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

def earliest_ancestor(ancestors, starting_node):
    # create a graph
    # add vertices
    graph = Graph()

    for v in ancestors:
        graph.add_vertex(v[0])
        graph.add_vertex(v[1])
        graph.add_edge(v[1],v[0])
    
    # queue and enqueue
    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1

    # earlierst ancestor
    oldest_ancestor = -1

    #While queue is not empty:
    while q.size() > 0:
        #pop the first thing in queue
        path = q.dequeue()
        # get last node form the path
        last_node = path[-1]
         # add the path to its neighbors to back of queue
        for neighbor in graph.get_neighbors(last_node):
            #clone the path
            new_path = path.copy()
             # add neighbor to the back of the queue 
            new_path.append(neighbor)
            q.enqueue(new_path)
        # ??
        if (len(path) == longest_path and  last_node < oldest_ancestor) or (len(path) > longest_path):
            oldest_ancestor = last_node
            longest_path = len(path)
            print(oldest_ancestor)

        
    
    return oldest_ancestor

    """
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    """
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))

