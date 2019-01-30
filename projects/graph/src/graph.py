"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        vertex = Vertex(vertex)
        self.vertices[vertex.vertex] = vertex.edge

    def add_edge(self, vertex_one, vertex_two):
        self.vertices[vertex_one].add(vertex_two)
        self.vertices[vertex_two].add(vertex_one)

    def add_directed_edge(self, start_vertex, end_vertex):
        self.vertices[start_vertex].add(end_vertex)

    def breadth_first_traversal(self, starting_vertex):
        queue = Queue() # new queue
        traversal_path = [starting_vertex] # new list for reporting traversal history; only str, not Vertexes
        queue.add(self.vertices[starting_vertex]) # adds input as starting member

        while queue.size() > 0:
            for item in queue.pop():
                if item in traversal_path:
                    pass
                else:
                    traversal_path.append(item)
                    queue.add(self.vertices[item])
            # queue.pop()

        print(f"traversal_path: {traversal_path}")

    def depth_first_traversal(self, starting_vertex):
        stack = Stack()
        traversal_path = [starting_vertex]
        stack.add(self.vertices[starting_vertex])
        while stack.size() > 0:
            for item in stack.pop():
                if item in traversal_path:
                    pass
                else:
                    traversal_path.append(item)
                    stack.add(self.vertices[item])
            # stack.add(self.vertices[stack.pop()])
        print(f"traversal_path: {traversal_path}")

    def recursive_depth_first_traversal(self, current_vertex):
        print(current_vertex)
        for item in self.vertices[current_vertex]:
            self.recursive_depth_first_traversal(item)

    def breadth_first_search(self, starting_node, destination_node):
        queue = Queue()
        traversal_path = []
        queue.add([starting_node])

        while queue.size() > 0:
            current_node = queue.pop()
            if current_node[-1] == destination_node:
                return current_node
            traversal_path.append(current_node[-1])
            for item in self.vertices[current_node[-1]]:
                new_path = list(current_node)
                new_path.append(item)
                queue.add(new_path)
            # queue.pop()

        print(f"traversal_path: {traversal_path}")

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edge = set()

    def __repr__(self):
        return f"{self.vertex} : {self.edge} \n"

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __repr__(self):
        pretty_print = "" # actually conventionally a separator character
        return pretty_print.join(str(self.queue))

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def __repr__(self):
        pretty_print = ""
        return pretty_print.join(str(self.stack))


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')

graph.add_directed_edge('0', '1')
graph.add_directed_edge('0', '2')
graph.add_directed_edge('1', '3')
graph.add_directed_edge('1', '4')
graph.add_directed_edge('3', '6')
graph.add_directed_edge('3', '7')
graph.add_directed_edge('2', '5')
graph.add_directed_edge('5', '8')
graph.add_directed_edge('5', '9')
# print(graph.vertices)

# graph.breadth_first_traversal('2')
# graph.breadth_first_traversal('0')
# graph.breadth_first_traversal('1')
# graph.breadth_first_traversal('3')
#
# graph.depth_first_traversal('0')
# graph.depth_first_traversal('1')
# graph.depth_first_traversal('2')
# graph.depth_first_traversal('3')

# graph.recursive_depth_first_traversal('0')

print(graph.breadth_first_search('0', '4'))
