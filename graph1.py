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

class Graph:
    def __init__(self):
        self.verticies = {}

    # add verts
    def add_vertex(self, vertex_id):
         self.verticies[vertex_id] = set() #set of edges from this vert
    # add edges
    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2) # add v2 as a neighbour to v1
        else:
            raise IndexError('Vertex does not exist')
    # get neighbors for vert
    def get_neighbors(self, vertex_id):
        return self.verticies[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empty queue and enqueue the starting vertex ID
	    q = Queue()
        # To initialize we have to put starting_vertex_id
	    q.enqueue(starting_vertex_id)

	    # Create a Set to store visited vertices
	    visited = set()

	    # While the queue is not empty...
	    while q.size() > 0:
            # Dequeue the first vertex
		    v = q.dequeue()

		    # If that vertex has not been visited...
		    if v not in visited:
                # Visit it
			    print(v)

			    # Mark it as visited...
			    visited.add(v)

			    # Then add all of its neighbors to the back of the queue
			    for next_vert in self.get_neighbors(v):
				    q.enqueue(next_vert)


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("B", "C")
g.add_edge("B", "A")

g.add_edge('C', 'B')

# print(g.get_neighbors('B'))
# print(g.get_neighbors('C'))

# print('-----------')
# print(g.verticies)
g.bft('B')