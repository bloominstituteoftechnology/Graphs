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
    #add verteces/nodes to Graph
    #add edges to connect nodes -- child to parent
    #implement Queue
    #add starting_node to Queue
    #create 'visited' set
    #create empty 'results' list

    #BEGIN REPL/loop
    #while Queue is greater than 0
        #create variable and assign to dequeue
        #create variable, assign for last vertex in path
        #check if last vertex has been visited or not
            #add that vertex to visted list
        #for loop in get_neighbors passing in last vertex
            #create variable for a new path -- copy path
            #add neighbor to our new path
            #enqueue the new path to Queue
            #append last item of that new path to 'results'
        #if 'results' list is empty
            #there are no parents, return -1
    #return last item of 'results' list
    graph = Graph()
    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
    for node in ancestors:
        graph.add_edge(node[1], node[0])
    que = Queue()
    que.enqueue([starting_node])
    visited = set()
    results = []

    while que.size() > 0:
        path = que.dequeue()
        last_vert = path[-1]
        if last_vert not in visited:
            visited.add(last_vert)
        for neighbor in graph.get_neighbors(last_vert):
            new_path = list(path)
            new_path.append(neighbor)
            que.enqueue(new_path)
            print(f'new path: {new_path}')
            results.append(new_path[-1])
        if len(results) == 0:
            return -1
    return results[-1]