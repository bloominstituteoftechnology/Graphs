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


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = "white"
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def add_bidirectional_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
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
                [to_visit.enqueue(child) for child in self.vertices[deq_node].edges]

    def depth_first_traversal(self, starting_node):
        to_visit = Stack()
        visited = set()
        to_visit.push(starting_node)
        while to_visit.size() > 0:
            deq_node = to_visit.pop()
            if deq_node not in visited:
                print(deq_node)
                visited.add(deq_node)
                [to_visit.push(child) for child in self.vertices[deq_node].edges]

    def depth_first_traversal_rec(self, starting_node, visited=set()):
        visited.add(starting_node)
        print(starting_node)
        for child_node in self.vertices[starting_node]:
            if child_node not in visited:
                self.depth_first_traversal_rec(child_node, visited)

    def breadth_first_search(self, start_node, dest_node):
        to_visit = Queue()
        visited = set()
        start_path = [start_node]

        to_visit.enqueue(start_path)

        while to_visit.size() > 0:
            deq_path = to_visit.dequeue()
            deq_node = deq_path[-1]
            print(f"Visited: {visited}")
            print(f"Path: {deq_path}")

            if deq_node not in visited:
                if deq_node == dest_node:
                    return deq_path

                visited.add(deq_node)

                for child in self.vertices[deq_node].edges:
                    copied_path = list(deq_path)
                    copied_path.append(child)
                    to_visit.enqueue(copied_path)

        return None


    def depth_first_search(self, start_node, dest_node):
        to_visit = Stack()
        visited = set()
        start_path = [start_node]

        to_visit.push(start_path)

        while to_visit.size() > 0:
            deq_path = to_visit.pop()
            deq_node = deq_path[-1]
            print(f"Visited: {visited}")
            print(f"Path: {deq_path}")

            if deq_node not in visited:
                if deq_node == dest_node:
                    return deq_path

                visited.add(deq_node)

                for child in self.vertices[deq_node].edges:
                    copied_path = list(deq_path)
                    copied_path.append(child)
                    to_visit.push(copied_path)

        return None