class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
     def vertex(self, label):
        if label in self.vertices:
            print('Already accounted for')
        else:
            self.vertices[label] = set()

    def edges(self, label, destination):
        if label in self.vertices:
            if destination in self.vertices:
                self.vertices[label].add(destination)
            else:
                print('No destination')
        else:
            print('No vertex')
 graph = Graph()  # Instantiate your graph
graph.vertex('0')
graph.vertex('1')
graph.vertex('2')
graph.vertex('3')
graph.edges('0', '1')
graph.edges('0', '3')
print(graph.vertices)

def bfsearch(self, root):
    if self.vertices == None:
        return
     if root not in self.vertices:
        raise IndexError('No vertex with that value in the graph.')
     # initialize our visited list
    visited = []
    # initialize a queue
    storage = queue.Queue()
    # put root value in the queue
    storage.put(self.vertices[root])
     while not storage.empty():
        # start at the root node
        current = storage.get()
         if current not in visited:
            visited.append(current)
         for edge in current.edges:
            if self.vertices[edge] not in visited:
                storage.put(self.vertices[edge])
     print(f'visited: {visited}')
    return visited
