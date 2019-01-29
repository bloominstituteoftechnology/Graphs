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

        # While queue is not empty
        while queue.len() > 0:
            # Dequeue vertex from queue
            current_vertex = queue.dequeue()

            # Check if current vertex is already visited
            if current_vertex not in visited:
                # Mark vertex as visited
                visited.append(current_vertex)
                # Enqueue current_vertex's child vertices
                for child_vertex in self.vertices[current_vertex]:
                    queue.enqueue(child_vertex)

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
                for child_vertex in self.vertices[current_vertex]:
                    stack.append(child_vertex)

        print(visited)

    def recursive_dft(self, vertex, visited=None):
        if visited is None:
            visited = []

        # # If the node has not been visited,
        if vertex not in visited:
            # Mark the node as visited
            visited.append(vertex)
            # Call recursive_dft on all children
            for child_vertex in self.vertices[vertex]:
                self.recursive_dft(child_vertex, visited)

        return visited

    def bf_search(self, starting_vertex, target_vertex):
        # Create a queue
        queue = Queue()
        # Enqueue starting vertex
        queue.enqueue([starting_vertex])
        visited = []

        # while queue is not empty
        while queue.len() > 0:
            # Dequeue path from queue
            path = queue.dequeue()  # returns a list
            # Set as current_vertex the last el of path
            current_vertex = path[-1]

            # check if current vertex is already visited
            if current_vertex not in visited:
                # Mark vertex as visited
                visited.append(current_vertex)
                if current_vertex == target_vertex:
                    return path
                # Enqueue current_vertex's child vertices
                for child_vertex in self.vertices[current_vertex]:
                    # duplicate path for each child_vertex
                    dup_path = list(path)
                    # append each child_vertex to path
                    dup_path.append(child_vertex)
                    # append dup_path to queue
                    queue.enqueue(dup_path)

        return None

    def df_search(self, starting_vertex, target_vertex):
        # Create a stack and
        # Push starting_vertex to stack
        stack = [starting_vertex]
        visited = []

        while len(stack) > 0:
            # Pop off last node in the stack
            current_vertex = stack.pop()

            # check if current_vertex is not yet visited
            if current_vertex not in visited:
                if current_vertex == target_vertex:
                    return True
                # Mark vertex as visited
                visited.append(current_vertex)
                # Push current_vertex's child vertices
                for child_vertex in self.vertices[current_vertex]:
                    stack.append(child_vertex)

        return False


# 0->3->5 and 0->1->4
graph = Graph()  # Instantiate your graph
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_vertex("4")
graph.add_vertex("5")
graph.add_vertex("6")
graph.add_vertex("7")
graph.add_edge("2", "1")
graph.add_edge("3", "2")
graph.add_edge("4", "2")
graph.add_edge("5", "3")
graph.add_edge("6", "4")
graph.add_edge("7", "4")
graph.add_edge("3", "5")
graph.add_edge("3", "6")
graph.add_edge("1", "7")
print(graph.bf_search("1", "6"))  # ['1', '2', '4', '6']
