"""
Simple graph implementation compatible with BokehGraph class.
"""
import random


class Queue:  #FIFO
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


class Stack:  #LIFO
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

    # Traversal
    def dft(self, starting_node, visited=None):
        # depth first traversal using recursion
        if visited is None:
            visited = []
        visited.append(starting_node)
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited
    
    # Traversal
    def bft(self, starting_node):
        visited = []

        q = Queue()

        q.enqueue()
        while q.size() > 0:
            dequeue = q.dequeue()
            visited.append(dequeue)
            print(dequeue)
            for edge in self.vertices[dequeue].edges:
                if edge not in visited:
                    q.enqueue(edge)            

    
    # sorting using DFS
    def dft_s(self, starting_node):
        s = Stack()
        s.push(starting_node)
        visited = []
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    s.push(edge)
    
     # Saerching if the node exists using BFS
    def bfs(self, starting_node, target_node):
        visited = []

        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:
            dequeue = q.dequeue()
            visited.append(dequeue)
            print(dequeue)
            if dequeue == target_node:
                return True
            for edge in self.vertices[dequeue].edges:
                if edge not in visited:
                    q.enqueue(edge)
        return False

    # storing the nodes in an entire path
    def bfs_path(self, starting_node, target_value):
        q = Queue()
        q.enqueue([starting_node])
        visited = []
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                return path
            visited.append(v)
            for next_vert in self.vertices[v].edges:
                new_path = list(path)
                new_path = append(next_vert)
                q.enqueue(new_path)
        return None

    # D traversal
    def dfs(self, starting_node, target_node, visited=None):
        if visited is None:
            visited = []
        visited.append(starting_node)
        print(starting_node)
        if starting_node == target_node:
            return True
        
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                if self.dfs(node,target_node, visited):
                    return True
        return False


    # DFS Path
    def dfs_path(self, start_vert, target_value, visited=None, path=None):
        if visited is None:
            visited = []
        if path is None:
            path = []
        visited.append(start_vert)
        print(start_vert)

        extended_path = list(path)
        estended_path.append(start_vert)

        if start_vert == target_value:
            return extended_path
        
        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                new_path = self.dfs_path(child_vert, target_value, visited, extended_path)
                if new_path:
                    return new_path

        return None






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




    