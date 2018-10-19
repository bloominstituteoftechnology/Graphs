"""
Simple graph implementation compatible with BokehGraph class.
"""

import random
import queue as queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            raise ValueError(f'Duplicate vertex {value} found')
        self.vertices[vertex_id] = Vertex(vertex_id)        


    def add_undirected_edge(self, start_edge, end_edge):
        if start_edge not in self.vertices:
            raise ValueError(f'Provided vertex {start_edge} does not exist')
        if end_edge not in self.vertices:
              raise ValueError(f'Provided vertex {end_edge} does not exist')
        self.vertices[start_edge].edges.add(end_edge)
        self.vertices[start_edge].add_color()       #adding color to connected nodes
        self.vertices[end_edge].edges.add(start_edge)
        self.vertices[end_edge].add_color()         #adding color to connected nodes
        

    def add_directed_edge(self, start_edge, end_edge):
        if start_edge not in self.vertices:
            ValueError(f'Vertex {start_edge} does not exist!')
        if end_edge not in self.vertices:
            ValueError(f'Vertex {end_edge} does not exist!')
        self.vertices[start_edge].edges.add(end_edge)
        self.vertices[start_edge].add_color()           #adding color to connected nodes
        self.vertices[end_edge].add_color()


    def breadth_first_search(self, start_node):
         q = []   #empty queue
         q.append(start_node)  #add strt_node to the queue
         visited = []
         while len(q) > 0:
             current = q.pop(0)
             visited.append(current)
             for edge in self.vertices[current].edges:       
                 if edge not in visited and edge not in q:
                     q.append(edge)
         print(f'breadth first seacrh {visited}')


    def depth_first_search(self, start_node, visited=[]):
        visited=visited
         
        if self.vertices[start_node]!=None:               
            if start_node not in visited:
                visited.append(start_node)
                for edge in self.vertices[start_node].edges:        
                    self.depth_first_search(edge, visited) #using recurssion   
        

        print(f'depth first search{visited}')                
        
    def dfs_search_value(self, start_node, target_node, visited=[]):
        
        if visited is None:
            visited=[]

        visited.append(start_node)
        if start_node==target_node:
            print('True')
            return True

        for edge in self.vertices[start_node].edges:
            if edge not in visited: 
                if self.dfs_search_value(edge, target_node, visited):        #using recurssion
                    print('True')  
                    return True 
        print('False')


        #Alternate soultion for dfs search to find if the target_node is present in the connected tree
        '''if start_node==target_node:
            print('True')
            return True

        visited=visited

        if self.vertices[start_node]!=None:
            if start_node not in visited:
                visited.append(start_node)
                for edge in self.vertices[start_node].edges:
                    if edge==target_node:
                        print('True')
                        return True
                    else:
                        self.dfs_search_value(edge, target_node, visited) #using recurssion
                        #print('True')
                        #return True
        print('False')'''

class Vertex:
    def __init__ (self, vertex_id, x=None, y=None, value=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.color='Blue'   #default color 
        self.edges = set()
        if self.x is None:
            self.x = random.random() * 10 - 5
        if self.y is None:
            self.y = random.random() * 10 - 5
        
        
    def add_color(self):  #  method to add a different color when the nodes get connected
        self.color='Red'


'''graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
#graph.add_edge('0', '4')
print(graph.vertices)'''
