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
