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

    1 = list(group)
    graph.add_edge(1[1], 1[0])
    # BFT
    #make a queue
    queue = []
    #make a visited set
    visited = set()
    # make path
    dft_path = []
    #store highest node
    highest_nodes = []
    # put starting vertex in he queue
    queue.apend(starting_node)
    highest_node.append(starting_node)
    visited.add(starting_node)

    index = len(highest_nodes)
    count = len(highest_nodes)
    #while q isn\t empty
    while TRUE:
    # dequeue the item, it is our current item
        node = queue.pop()
        print(node)
        # mark current as visited
        bft_path.append(node)
        # for each of the dequeued item's edge
        highest_nodes += list(graph.vertices[node])
        # put them in the queue
        if not len(queue) and not graph.vertices[node]:
            break
        count -= 1
        if not count:
            highest_nodes = highest_nodes[index:]
            count = len(highest_nodes)
            index = len(highest_nodes)
        for parent in graph.verices[node]:
            if parent not in visited:
                queue.append(parent)
                visited.add(parent)
    print('Breath First Path', bft_path)
    print('Highest Nodes List', highest_nodes)

    if highest_nodes[0] == starting_node:
        return -1
    else: 
        return min(highest_nodes)


    # Create Count

