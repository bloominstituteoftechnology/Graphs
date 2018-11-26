#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph import Graph
from draw import BokehGraph

def createDefaultGraph():
    graph=Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_undirected_edge('0', '1')
    graph.add_undirected_edge('0', '3')
    graph.add_directed_edge('1', '2')
    graph.add_directed_edge('1', '4')
    graph.add_directed_edge('2', '5')
    graph.add_directed_edge('2', '6')
    graph.breadth_first_search('0')
    graph.depth_first_search('0')
    graph.dfs_search_value('0','1')
    #graph.dfs_search_value('0','11')
    #graph.add_directed_edge('7','4')
    #graph.add_directed_edge('7','4')
    g1 = BokehGraph(graph)
    g1.show()


def createRandomGraph(numNodes, numEdges):
    graph=Graph()
    
    all_edges=[]

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i,  j) )
    
    
    random.shuffle(all_edges)
    
    edges=all_edges[:numEdges]

    for i in range(numNodes):
        graph.add_vertex(i)
   
    
    for edge in edges:
        #print(edge)
        graph.add_directed_edge(edge[0], edge[1])


    g1 = BokehGraph(graph)
    g1.show()
    



def main(style, numNodes, numEdges):
    if style=='default':
        createDefaultGraph()
    elif style=='random':
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = "default"
    numNodes = 4
    numEdges = 4

    for arg in argv[1:]:
        argv_split=arg.split("=")
  
        if len(argv_split)==2:
            if (argv_split[0]).lower()=='style':
                style=(argv_split[1]).lower()
            elif (argv_split[0]).lower()=='nodes':
                numNodes=int(argv_split[1])
            elif (argv_split[0]).lower()=='edges':
                numEdges=int(argv_split[1])    
            else:
                print('In correct command.')
    
    main(style, numNodes, numEdges)    

