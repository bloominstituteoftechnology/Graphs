"""
Simple graph implementation compatible with BokehGraph class.
"""
import random


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else: 
            return None
    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if(self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")    

class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()

        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x  
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return f"{self.edges}"



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # graph.add_edge('0', '4')
    # graph.add_edge('3', '0')
    print(graph.vertices)



# Old code, above is the refactored code
# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
    
#     def add_vertex(self, vertex):
#         self.vertices[vertex] = set()
    
#     def add_edge(self, vert, edge2):
#         # specify which vertex
#         # receive inputs for edge cases regard that vertex
#         # update vertex set values
#         # print the dictionary
#         #code is below this line
#         # vert = f"Please specify vertex: {input()}"
        
#         # self.vertices[vert].update(edge) 
#         # print(self.vertices)
#         if vert not in self.vertices:
#             raise Exception(f"No{vert} vertex")
#             self.vertices[vert].add(edge2)
#             if vert not in self.vertices:
#                 raise Exception(f"No {edge2} vertex")
#             self.vertices[vert].add(edge2)


#         self.vertices[vert].add(edge2)
#         self.vertices[edge2].add(vert)

# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     graph.add_vertex('0')
#     graph.add_vertex('1')
#     graph.add_vertex('2')
#     graph.add_vertex('3')
#     graph.add_edge('0', '1')
#     graph.add_edge('0', '3')
#     # graph.add_edge('0', '4')
#     # graph.add_edge('3', '0')




    