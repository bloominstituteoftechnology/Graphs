from random import sample
from sys import argv
from draw import BokehGraph 
from graph import Graph, Vertex

def main(num_vertices=2,num_edges=2, draw_components=True):
  graph = Graph()
  for num in range(num_vertices):
    graph.add_vertex(Vertex(label=str(num)))

  for _ in range(num_edges):
    vertices = sample(graph.vertices.keys(),2)
    graph.add_edge(vertices[0],vertices[1])
  # graph.get_connected_components()
  bg = BokehGraph(graph, draw_components = draw_components)
  bg.show()
if __name__ == '__main__':
  if len(argv) == 4:
    NUM_VERTICES = int(argv[1])
    NUM_EDGES = int(argv[2])
    DRAW_COMPONENTS= bool(int(argv[3]))
    main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
  else:
    print('Expected arguments: Num_vertices, num_edges draw components')
    print('Inputs are integers, draw components should be 1/0')
