#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,4)
    graph.add_edge(2,5)
    graph.add_edge(3,6)
    graph.add_edge(4,6)
    graph.add_edge(4,7)
    graph.add_edge(6,8)
    graph.add_edge(7,8)
    graph.add_edge(5,7)

    print(graph.vertices)
    print("\nBREADTH-FIRST-TRAVERSAL...")
    graph.breadth_first_traversal(0)
    print("\nDEPTH-FIRST-TRAVERSAL...")
    graph.depth_first_traversal(0)
    print("\nDEPTH-FIRST-TRAVERSAL-RECURSIVE")
    print("\n",graph.DFT_recursive(0))
    print("\nBREADTH-FIRST-SERACH...")
    print("\n",graph.breadth_first_search(0, 3)) # TRUE as 3 is in vertices
    print("\nDEPTH-FIRST-SEARCH...")
    print("\n",graph.depth_first_search(0, 9))  # False as 9 is not present in vertices
    print("BFS_PATH    " ,graph.BFS_path(0, 3))
    
    
if __name__ == '__main__':
    # TODO - parse argv
    main()
