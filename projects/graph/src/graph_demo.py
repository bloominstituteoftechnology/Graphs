#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
# from graph import Graph
# from draw import BokehGraph
from random import randrange



def main(**kwargs):
	print(kwargs)

# 	#get input for my number of vertices
# 	irand = int(input('how man nodes would you like?'))

# 	while irand > 7:
# 		print('max number of vertices is 7')
# 		irand = int(input('how man nodes would you like?'))

# 	random_graph = Graph()

# 	#user input to generate my vertices
# 	for i in range(0, irand):
# 	  random_graph.add_vertex(str(i))

# 	#now that I have my number of nodes I give each node a random number of edges

# 	#I will represent the random number of edges to add per node as a set of randomly generated numbers in a list

# 	#I picked random number between 0-4 to keep things simple
# 	edges_to_add_per_node = []
# 	for i in range(0, irand):
# 	  edges_to_add_per_node.append(randrange(0, 4))

# 	# print(edges_to_add_per_node)

# 	#I will loop through the edges_to_add_per_node list. I will take each number at its said idx as the ending point of another loop that will add the number of edges added to that particular node.

# 	#also the added edge will be random as well
# 	for idx, val in enumerate(edges_to_add_per_node):
# 	  for i in range(0, val):

# 	    #here I randomly assign weither or not the node is edge going to be added as bi_directional or not
# 	    is_bi = randrange(0,2)

# 	    if is_bi == 0:
# 	      is_bi = False
	    
# 	    if is_bi == 1:
# 	      is_bi = True
	    
# 	    random = randrange(0, irand)
# 	    random_graph.add_edge(str(idx), str(random), is_bi)

# 	drawn_tree = BokehGraph(random_graph)
# 	drawn_tree.draw_graph()



if __name__ == '__main__':
    # TODO - parse argv
    # print(argv)
    # main()

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













