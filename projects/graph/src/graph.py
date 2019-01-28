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
            current_vertex = queue.dequeue()

            # check if current vertex is already visited
            if current_vertex not in visited:
                # Mark vertex as visited
                visited.append(current_vertex)
                # Enqueue current_vertex's child vertices
                for edge in self.vertices[current_vertex]:
                    queue.enqueue(edge)

        print(visited)

    def df_traversal(self, starting_vertex):
        # Create a stack and
        # Push starting_vertex to stack
        stack = [starting_vertex]
        visited = []

        while len(stack) > 0:
            # Pop off last node in the stack
            current_vertex = stack.pop()

            # check if current_vertex is not yet visited
            if current_vertex not in visited:
                # Mark vertex as visited
                visited.append(current_vertex)
                # Push current_vertex's child vertices
                for edge in self.vertices[current_vertex]:
                    stack.append(edge)

        print(visited)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
# graph.add_vertex("E")
# graph.add_edge("B", "A")
# graph.add_edge("C", "B")
# graph.add_edge("D", "B")
# graph.add_edge("E", "C")
# graph.add_edge("A", "D")
# graph.add_edge("D", "E")
# graph.df_traversal("A")
# print(graph.vertices)

