"""
Simple graph implementation
"""
# test_graph =  { 
#     "A": {"B"},
#     "B": {"C", "D"},
#     "C": {"E"},
#     "D": {"F", "G"},
#     "E": {"C"},
#     "F": {"C"},
#     "G": {"A", "F"}
#                 }

  

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


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        print(self.vertices)
        
    def add_edge(self, from_vertex, to_vertex):
        self.vertices[from_vertex].add(to_vertex)
        self.vertices[to_vertex].add(from_vertex)
    
    def add_vertex(self, value):
        self.vertices[value] = set()
    
    def breadth_first_traversal(self, start_vert):
        new_queue = Queue()
        visited_node = []

        new_queue.enqueue(start_vert)

        while new_queue.size() > 0:
            n = new_queue.dequeue()

            if n not in visited_node:
                visited_node.append(n)
                print(f"Visited nodes: {visited_node}")
                print(self.vertices[n])

                for edge in self.vertices[n]:
                    new_queue.enqueue(edge)
                    # print(edge)
        # print(visited_node)

           
    def depth_first_traversal(self, start_vert):
        
        visited = []

        if start_vert not in visited:
            visited.append(start_vert)

            for node in self.vertices[start_vert]:
                self.depth_first_traversal(node, visited)
        
        return visited
        