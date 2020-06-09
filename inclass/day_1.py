# set is like a list in python, except you can get O(1) lookup and there cannot be duplicates.

class Graph:

    def __init__(self):
        self.vertices = {}

    # add verts
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # set of edges from this vert

    # add edges
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # add v2 as a neighbor to v1
        else:
            raise IndexError("Vertex does not exist")

    # get neighbors for a vert
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
    def bft(self, starting_vertex_id):
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)

        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # If taht vertex has not been visited....
            if v not in visited:
                # visit it (Doing whatever we have to do here. In this case, we are just printing it)
                print(v)

                # MArk it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('B', 'C')
g.add_edge('B', 'A') # Now there's a bidirectional connection between B and C

g.add_edge('C', 'B')

print(g.get_neighbors('B'))
print(g.get_neighbors('C'))

print('------------------')
print(g.vertices)