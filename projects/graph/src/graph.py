"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO
    
    def add_vertex(self,value):
        self.vertices[value] = set()

    def add_edge(self, value, valuetwo):
        if value in self.vertices and valuetwo in self.vertices:
            self.vertices[value].add(valuetwo)
            self.vertices[valuetwo].add(value)
        else:
            raise IndexError("That vertex does not exist!")
            
    def bft(self, adjList, node_id):
        collection = []
        collection.append(node_id)
        visited = []
        while len(collection) > 0:
            n = collection.pop(0)
            if n not in visited:
                visited.append(n)
                for next_node in adjList[n]:
                    collection.append(next_node)
