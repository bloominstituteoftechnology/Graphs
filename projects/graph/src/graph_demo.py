#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
# from random import randrange
import random

def get_default_graph():
	default_graph = Graph()

	default_graph.add_vertex(0)
	default_graph.add_vertex(1)
	default_graph.add_vertex(2)
	default_graph.add_vertex(3)
	default_graph.add_vertex(4)
	default_graph.add_vertex(5)
	default_graph.add_vertex(6)
	default_graph.add_vertex(7)
	default_graph.add_vertex(8)
	default_graph.add_vertex(9)

	default_graph.add_edge(0, 1, False)
	default_graph.add_edge(0, 3, False)
	default_graph.add_edge(1, 2, False)
	default_graph.add_edge(2, 4, False)
	default_graph.add_edge(4, 9, False)
	default_graph.add_edge(2, 5, False)
	default_graph.add_edge(2, 4, False)
	default_graph.add_edge(3, 7, False)
	default_graph.add_edge(3, 6, False)

	drawn_tree = BokehGraph(default_graph)

	drawn_tree.draw_graph()

def get_random_graph(num_verts, num_edges):
	graph = Graph()

	for vert_id in range(0, num_verts):
		graph.add_vertex(vert_id)

	all_edges = []
	for i in range(0, num_verts):
		for j in range(0, num_verts):
			if i < j:
				all_edges.append((i, j))

	random.shuffle(all_edges)
	random_edges = all_edges[:num_edges]

	for edge in random_edges:
		graph.add_edge(edge[0], edge[1], False)

	drawn_tree = BokehGraph(graph)

	drawn_tree.draw_graph()


def main(**kwargs):
	print(kwargs)

	style = kwargs['style']
	num_verts = kwargs['num_verts']
	num_edges = kwargs['num_edges']

	if style == "default":
		graph = get_default_graph()
	elif style == "random":
		graph = get_random_graph(num_verts, num_edges)
	else:
		graph = get_default_graph()



if __name__ == '__main__':
    style="default"
    num_verts = 5
    num_edges = 6

    for arg in argv[1:]:
    	arg_split = arg.split("=")
    	if len(arg_split) == 2:
    		if arg_split[0] == "style":
    			style = arg_split[1].lower()
    		elif arg_split[0] == 'verts':
    			num_verts = int(arg_split[1])
    		elif arg_split[0] == 'edges':
    			num_edges = int(arg_split[1])

    main(style=style, num_verts=num_verts, num_edges=num_edges)













