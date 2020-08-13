from util import Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    #implement Graph class
    graph = Graph()
    #add verteces/nodes to Graph
    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
    #add edges to connect nodes -- child to parent
    for node in ancestors:
        graph.add_edge(node[1], node[0])
    #implement Queue
    que = Queue()
    #add starting_node to Queue
    que.enqueue([starting_node])
    #create 'visited' set
    visited = set()
    #create empty 'results' list
    results = []

    #BEGIN REPL/loop
    #while Queue is greater than 0
    while que.size() > 0:
        #create variable and assign to dequeue
        path = que.dequeue()
        #create variable, assign for last vertex in path
        last_vert = path[-1]
        #check if last vertex has been visited or not
        if last_vert not in visited:
            #add that vertex to visted list
            visited.add(last_vert)
        #for loop in get_neighbors passing in last vertex
        for neighbor in graph.get_neighbors(last_vert):
            #create variable for a new path -- copy path
            new_path = list(path)
            #add neighbor to our new path
            new_path.append(neighbor)
            #enqueue the new path to Queue
            que.enqueue(new_path)
            print(f'new path: {new_path}')
            #append last item of that new path to 'results'
            results.append(new_path[-1])
        #if 'results' list is empty
        if len(results) == 0:
            #there are no parents, return -1
            return -1
    #return last item of 'results' list
    return results[-1]




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 7))