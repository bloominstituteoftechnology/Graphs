from queue import Queue
from stack import Stack
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
        else:
            raise Exception(f'Vertex {vertex1} does not exist.')

    def breadth_first_traversal(self, start_node):
        # Create a new queue using the imported queue file
        queue = Queue()
        # Storage for the nodes that were visted
        visited = []
        # Enqueues the starting node
        queue.enqueue(start_node)
        # Checks if the queue size is greater than 0
        while queue.len() > 0:
            node = str(queue.dequeue())
            visited.append(node)
            for c_node in self.vertices[node]:
                if c_node not in visited:
                    queue.enqueue(c_node)
        return visited

    def depth_first_traversal(self, start_node):
        # Create a new stack instance
        stack = Stack()
        # Create new set with intention to store visited nodes
        visited = set()
        # Add start_node to the stack
        stack.push(start_node)
        # While the stack is not empty
        while stack.size() > 0:
            # Assign node to stack.pop()
            node = stack.pop()
            # If current node is not in visited set
            if node not in visited:
                # Print node for clarity
                print(node)
                # Add current node to visited set
                visited.add(node)
                # For each child node in current node
                for next_node in self.vertices[node]:
                    # Add each child to the stack
                    stack.push(next_node)
        return visited

    def breadth_first_search(self, start_node, target_node):
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)
        while queue.len() > 0:
            node = queue.dequeue()
            if node not in visited:
                if node == target_node:
                    return True
                print(node)
                visited.add(node)
                for next_node in self.vertices[node]:
                    queue.enqueue(next_node)
        return False

    def depth_first_search(self, start_node, target_node):
        s = Stack()
        visited = set()
        s.push(start_node)
        while s.size() > 0:
            node = s.pop()
            if node not in visited:
                if node == target_node:
                    return True
                print(node)
                visited.add(node)
                for next_node in self.vertices[node]:
                    s.push(next_node)
        return False

    def breadth_first_path(self, start_node, target_node):
        queue = Queue()
        visited = set()
        queue.enqueue([start_node])
        while queue.len() > 0:
            path = queue.dequeue()
            node = path[-1]
            for neighbor in self.vertices[node]:
                visited.add(neighbor)
                upath = path + [neighbor]
                if neighbor is target_node:
                    return upath
                else:
                    queue.enqueue(upath)
        return print('no path found')
