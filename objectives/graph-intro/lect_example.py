class Queue:
    def __init__(self, ls=[]):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        if self.size <= 0:
            return 0
        else:
            return self.size

    def enqueue(self, value):
        self.size +=1
        return self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size += -1
            return self.storage.pop(0)


class Graph:
    def __init__(self):
        self.vertices = {

        }

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # holds the edges

    def add_edge(self, vert1, vert2):
        if vert1 and vert2:
            self.vertices[vert1].add(vert2) # set.add()
        else:
            raise IndexError("nonexistant vert")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def breadth_first_traversal(self, start_id):
        # This uses a queue, tracks what is visited until completely explored.
        # while the queue is not empty, dequeue and keep going.
        #  Visit, add all neighbors into the queue, order doesn't matter.

        # Create a q, create a set to store visited
        q = Queue()
        visited = set()
        #  init: enqueue starting node
        q.enqueue(start_id)
        # while queue isn't empty
        while q.size > 0:
        #   dequeue first item
            v = q.dequeue()
        #   if not visited:
            if v not in visited:
        #       mark as fvisited
                visited.add(v)
                print("Visited: ", v)
        #       add neighbors to queue    
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")

g.add_edge("B", "A")
g.add_edge("B", "C")
g.add_edge("B","B")

g.add_edge("C","D")
g.add_edge("D","C")

g.breadth_first_traversal("B")