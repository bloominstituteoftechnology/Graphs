"""
Simple graph implementation
"""

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        # O(n) because first item is popped off, and all other items have to be shifted
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def add_bidirectional_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("Vertex does not exist")

    def breadth_first_traversal(self, starting_node):
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_node)
        while to_visit.size() > 0:
            deq_node = to_visit.dequeue()
            if deq_node not in visited:
                print(deq_node)
                visited.add(deq_node)
                [to_visit.enqueue(child) for child in self.vertices.get(deq_node)]

    def depth_first_traversal(self, starting_node):
        to_visit = Stack()
        visited = set()
        to_visit.push(starting_node)
        while to_visit:
            deq_node = to_visit.pop()
            if deq_node not in visited:
                print(deq_node)
                visited.add(deq_node)
                [to_visit.push(child) for child in self.vertices.get(deq_node)]

    def depth_first_traversal_rec(self, starting_node, visited=set()):
        visited = visited
        if starting_node in self.vertices and starting_node not in visited:
            print(starting_node)
            visited.add(starting_node)
            for child in self.vertices.get(starting_node):
                self.depth_first_traversal_rec(child, visited)

    def depth_first_search(self, start_node, dest_node):
        start = start_node
        dest = dest_node
        dist = float("inf")
        shortest_path = []

        to_visit = []
        visited = []

        if start not in self.vertices or dest not in self.vertices:
            print("Start or destination node don't exist")
            return

        to_visit.append(start)

        while to_visit:
            curr_node = to_visit.pop()
            if curr_node not in visited:
                # Check visited distance to currently shortest distance
                if curr_node == dest and len(visited) < dist:
                    dist = len(visited)
                    shortest_path = visited
                    print(shortest_path)
                    print(to_visit)
                    #visited = visited[:1]
                else:
                    visited.append(curr_node)
                    [to_visit.append(child) for child in self.vertices[curr_node]]

        return shortest_path
