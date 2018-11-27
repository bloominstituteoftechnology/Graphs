"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print('This vertex is already part of the graph.')
            return

    def add_edge(self, vert1, vert2):
        # if both vert1 and vert2 are valid vertices found in self.vertices...
        if vert1 in self.vertices and vert2 in self.vertices:
            # if an edge has not already been created from vert1 to vert2, add edge to self.vertices
            if (not vert2 in self.vertices[vert1]) and (not vert1 in self.vertices[vert2]):
                self.vertices[vert1].add(vert2)
                self.vertices[vert2].add(vert1)
            # if the edge had already been created, print error message.
            else:
                print('This edge had already been created in the graph.')
                return
        # if one of vert1 and vert2 is an invalid vertex, print error message
        else:
            print('Please provide a valid set of vertices in the graph.')
            return
    
    def add_directed_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            if vert2 not in self.vertices[vert1]:
                self.vertices[vert1].add(vert2)
            else:
                print('This edge had already been created in the graph.')
                return
        # if one of vert1 and vert2 is an invalid vertex, print error message
        else:
            print('Please provide a valid set of vertices in the graph.')
            return
    # Breadth first traversal
    def bft(self, starting_vert):
        # create storage for vertices visited
        visited = []
        # create queue to maintain BFT order of vertices visited
        queue = [starting_vert]
        # While we have not finished checking all edges, as depicted by the number of elements left in the queue:
        while len(queue) > 0:
            # dequeue and check if element has been visited; if it hadn't, add it to the visited list, follow by adding its children vertices to the queue
            current_vert = queue.pop(0)
            if not current_vert in visited:
                visited.append(current_vert)
                for vert in self.vertices[current_vert]:
                    queue.append(vert)
        return visited
    
    # Depth first traversal
    def dft(self, starting_vert):
        # create storage for vertices visited
        visited = []
        # create stack to maintain BFT order of vertices visited
        stack = [starting_vert]
        # While we have not finished checking all edges, as depicted by the number of elements left in the queue:
        while len(stack) > 0:
             # dequeue and check if element has been visited; if it hadn't, add it to the visited list, follow by adding its children vertices to the stack
            current_vert = stack.pop(-1)
            if current_vert not in visited:
                visited.append(current_vert)
                for vert in self.vertices[current_vert]:
                    stack.append(vert)
        return visited

    # Depth first traversal - recursive
    def dft_recursive(self, starting_vert):
        visited = []
        

# test
graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('7', '1')
graph.add_edge('3', '5')

# print(graph.vertices)
# print(graph.bft('1'))
print(graph.dft('1'))