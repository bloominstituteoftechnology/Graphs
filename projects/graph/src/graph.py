"""
Simple graph implementation compatible with BokehGraph class.
"""
# let's use python's built in queue library
import queue as queue

class Vertex:
    def __init__(self, vertex_value):
        self.value = vertex_value
        self.edges = set()

    # define the printable representation of the Vertex's edges object to be human-readable in the console
    # this prevents the '__main__.Object at 0x1234f' gobbledygook from logging in the console
    def __repr__(self):
        return f'{self.value}'

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # initialize an empty object for the vertices
        self.vertices = {}
        # each vertices[index] Vertex() will have an associated object of edges found in vertices[index].edges

        # method to add a vertex to the vertices object
    def add_vertex(self, vertex_value):
        self.vertices[vertex_value] = Vertex(vertex_value)
        # constructs a new Vertex with the class constructor below

        # method to add edges to an existing vertex
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
            # connect the two vertices by giving each their respective edge
        else:
            raise IndexError('Vertex not found.')
            # return an error if either vertex does not exist

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

        print(f'visited bft: {visited}')
        return visited

    def dfsearch(self, root):

        # STACK SOLUTION
        stack = [self.vertices[root]]
        visited = []

        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)

            for edge in current.edges:
                if self.vertices[edge] not in visited:
                    stack.append(self.vertices[edge])

        print(f'visited dft: {visited}')
        return visited

    def dfrecursion(self, root, visited=[]):
        
        visited.append(root)
        
        for edge in self.vertices[root].edges:
            if edge not in visited:
                self.dfrecursion(edge, visited)

        return visited


        # put the start node in the queue
        # while queue is not empty...
        # remove node from queue
        # check if it's visited
            # if not, mark node as visited
            # then put all children in queue




# test the Graph class
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('5')
graph.add_vertex('4')
graph.add_edge('5', '4')
graph.add_edge('4', '2')
graph.add_edge('2', '4')
graph.add_edge('5', '3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# print(graph.vertices)
graph.bfsearch('0')
graph.dfsearch('0')
print('dfrecursion: ', graph.dfrecursion('1'))