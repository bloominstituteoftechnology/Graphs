from random import sample
from sys import argv
from draw import BokehGraph 
from graph import Graph

def main(num_vertices=2,num_edges=2):
  graph = Graph()
  for num in range(num_vertices):
    graph.add_vertex(str(num))
  for _ in range(num_edges):
    vertices = sample(graph.vertices.keys(),2)
    graph.add_edge(vertices[0],vertices[1])
  # graph.get_connected_components()
  bg = BokehGraph(graph)
  bg.show()
if __name__ == '__main__':
  if len(argv) == 3:
    NUM_VERTICES = int(argv[1])
    NUM_EDGES = int(argv[2])
    main(NUM_VERTICES, NUM_EDGES)
  else:
    main()
