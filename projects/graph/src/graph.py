"""
Simple graph implementation compatible with BokehGraph class.
"""

import random
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex_id):
        self.vertices[vertex_id]=Vertex(vertex_id)
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError('That vertex does not exist.')
    def bfs(self,starting_node):
        queue=[]
        queue.append(starting_node)
        visited=[]
        while len(queue)>0:
            current_item=queue.pop(0)
            if current_item not in visited:
                visited.append(current_item)
                queue.extend(list(current_item.edges))

class Vertex:
    def __init__(self,vertex_id,x=None,y=None):
        self.id=vertex_id
        self.edges=set()
        if x is None:
            self.x=random.random()*10-5
        else:
            self.x=x
        if y is None:
            self.y=random.random()*10-5
        else:
            self.y=y
    def __repr__(self):
        return f'{self.edges}'
