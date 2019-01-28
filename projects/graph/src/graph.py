# Simple graph implementation
from queue import Queue


class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        # TODO
        # Create an empty graph
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            print(f"No {vertex} vertex")

    def bf_traversal(self, starting_vertex):
        # Create a queue
        queue = Queue()
        # Enqueue starting vertex
        queue.enqueue(starting_vertex)
        visited = []

        # while queue is not empty
        while queue.len() > 0:
            # Dequeue vertex from queue
            current_node = queue.dequeue()
            # print("current node", current_node)
            if current_node not in visited:
                # Mark vertex as visited
                visited.append(current_node)
                # Enqueue current_vertex's child vertices
                for edge in self.vertices[current_node]:
                    queue.enqueue(edge)

        print(visited)

