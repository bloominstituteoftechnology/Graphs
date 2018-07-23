# Editing on Sublime, running on Google Colab
# Upgrade pip version 10.0.1 to version 18.0
!pip install --upgrade pip

# Install bokeh
!pip install bokeh

#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
    	self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
    	if start not in self.vertices or end not in self.vertices:
    		raise Exception('Given vertex does not exist.')
    	self.vertices[start].add(end)
    	if bidirectional:
    		self.vertices[end].add(start)