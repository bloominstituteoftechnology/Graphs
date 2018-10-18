"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
     #   self.id
        self.vertices = {}
        vertices = self.vertices
        # self.label = label
        self.edges = ()
    # self.vertices[key] = Vertex[key]
    #  key is vertex_id

    def add_vertex(self,key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self, srcKey, destKey):
        if srcKey in self.vertices and destKey in self.vertices:
            self.vertices[srcKey].edges.add(destKey)
            self.vertices[destKey].edges.add(srcKey)
        else:
            raise IndexError("That vertex does not exist!")
    # def add_edge(self, srcKey, destKey):
    #     self.vertices[srcKey].addNextEdge(self.vertices[destKey])
    #
    # def Edge_doesNot_exist(self, srcKey, destKey):
    #     return self.vertices[srcKey].whoDoes_itPointTo(self.vertices[destKey])
    #
    # def __iter__(self):
    #     return iter(self.vertices.values())

    def bfs(self, starting_node):
        queue = [starting_node]
        visited = [starting_node]
        while len(queue) > 0:
            
            cur_node =  queue.pop()
            for edge in self.vertices[cur_node].edges:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)
        return visited


    def dfs(self, starting_node, target_node, visited=None):
        """
        Depth first traversal using recursion
        """
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        #print(starting_node)
        if starting_node == target_node:
            return True
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                if self.dfs(node, target_node, visited):
                    return True
        return False

    def dfs_path(self, start_vert, target_value, visited=None, path=None):
        # Initialize starting visited/path lists
        if visited is None:
            visited = []
        if path is None:
            path = []
        # Mark the first node as visited
        visited.append(start_vert)
        print(start_vert)
        # Add the node to the path
        extended_path = list(path)
        extended_path.append(start_vert)  # ...as a path.
        # Return the path if we find our target node
        if start_vert == target_value:
            return extended_path
        # Otherwise, for each child
        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:  # If it hasn't been visited yet
                # Call dfs_path on the children
                new_path = self.dfs_path(child_vert, target_value, visited, extended_path)
                # Return the path if it's valid
                if new_path:
                    return new_path
        return None

class Vertex:
    def __init__(self, key, x=None, y=None):
        self.key = key
        self.edges = set()
        self.points_to = {}
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    # def addNextedge(self, dest):
    #     self.points_to = dest
    #
    # def getNextEdge(self):
    #     return self.points_to.keys
    #
    # def whoDoes_itPointTo(self,dest):
    #     return dest in self.points_to





    def __repr__(self):
        return f"{self.edges}"

# graph = Graph() # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_vertex('6')
# graph.add_vertex('7')
# # graph.add_edge('0', '1')
# # graph.add_edge('0', '3')
# print(graph.vertices)
