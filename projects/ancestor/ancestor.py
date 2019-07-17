from util import Stack, Queue  # These may come in handy

class Graph:
    def __int__(self):
        self.vertices = {}

    #Add a vertex to the graph 
    def add_vertices(self, vertex):
        self.vertices[vertex] = set()
    # Add  a directed edge to the
    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertices(v1);
        if v2 not in self.vertices:
            self.add_vertices(v2);
        self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    
    # Build graph
    graph = Graph()

    1= list(group)
    graph.add_edge(1[1], 1[0])
    # BFT
    #make a queue
        queue = Queue()
        #make a visited set
        visited = set()
        # make path
        dft_path = []
        #store highest node
        highest_node = []
        # put starting vertex in he queue
        queue.enqueue(starting_vertex)
        #while q isn\t empty
        while queue.size():
        # dequeue the item, it is our current item
            node = queue.dequeue()
            print(node)
        # mark current as visited
            visited.add(node)
        # for each of the dequeued item's edge
            for edge in self.vertices[node]:
        # put them in the queue
                queue.enqueue(edge)

    # Create Count

