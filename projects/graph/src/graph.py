#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verts = {}

    def add_vert(self,label,connect = [], bidir = False):

        for x in connect:

            if x not in list(self.verts.keys()):
                print("Connection not made, node does not exist!")
                connect.remove(x)

            else:

                next

        self.verts[str(label)] = connect

        if bidir:

            for y in connect:

                self.verts[str(y)].append(label)

    def delete_vert(self, label):
       
        label = str(label)
        paths = []

        if label not in list(self.verts.keys()):
            raise Exception("Error - Node does not exist!")

        else:

            paths = self.verts[label]
            self.verts.pop(label,1)

            for i in paths:

                self.verts[i].remove(label)

    def delete_conn(self, node, conn, bidir = False):

        node = str(node)
        conn = str(conn)
        
        self.verts[node].remove(conn)

        if bidir:

            if node in self.verts[conn]:

                self.verts[conn].remove(node)  

    def add_conn(self, start, stop, bidir = True):
        
        start,stop = str(start),str(stop)

        if start not in list(self.verts.keys()):
            raise Exception("Error -Start Node does not exist!")

        
        elif stop not in list(self.verts.keys()):
            raise Exception("Error -Stop Node does not exist!")

        else:

            if bidir:

                self.verts[start].append(stop)
                self.verts[stop].append(start)

            else:
                self.verts[start].append(stop)