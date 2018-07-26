"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Jitter)

from random import choice, random, randrange, randint
from functools import reduce
from graph import Graph

class BokehGraph:
  """Class that takes a graph and exposes drawing methods."""
  def __init__(self, graph, title='Graph', width=10, height=10, show_axis=False, show_grid=False, circle_size=20):
    if not graph.vertices:
      raise Exception('Graph should contain vertices!')
    self.graph = graph
    
    # Setup plot
    self.width = width * circle_size
    self.height = height * circle_size
    self.circle_size = circle_size
    self.pos = {}  # dict to map vertices to x, y positions
    self.plot = figure(title=title, x_range=(0, width*circle_size), y_range=(0, height*circle_size))
    self.plot.axis.visible = show_axis
    self.plot.grid.visible = show_grid
    self._setup_graph_renderer(circle_size)

  def _setup_graph_renderer(self, circle_size):
    graph_renderer = GraphRenderer()

    node_indices = [*self.graph.vertices.keys()]
    colors = [self.graph.vertices[i].color for i in node_indices]
    print(colors)
    graph_renderer.node_renderer.data_source.data = dict(
      index=node_indices,
      fill_color = colors)

    graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='fill_color')
    
    graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
    self.randomize()

    graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
    self.plot.renderers.append(graph_renderer)

  def _get_edge_indexes(self):
    node_indices = [*self.graph.vertices.keys()]

    return dict(
      start=reduce(lambda x,y: x+y,[[i]*len(self.graph.vertices[i].edges) for i in node_indices]),
      end=reduce(lambda x,y: x+y,[list(self.graph.vertices[i].edges) for i in node_indices]))

  def _get_random_colors(self):
    colors = []
    for _ in range(len(self.graph.vertices)):
      color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
      colors.append(color)
    return colors

  def randomize(self):
    """Randomize vertex positions."""
    box_width = self.width / len(self.graph.vertices)
    half_height = self.height/2

    i = 0
    factor = 0
    for vertex in self.graph.vertices:
      i += 1
      factor = i % 2
      x = (i * box_width) - (box_width/2)
      y = randrange(self.circle_size + half_height*factor, half_height + half_height*factor - self.circle_size)

      self.pos[vertex] = (x,y)
      
    print(self.pos)
  def show(self, output_path='./graph.html'):
    output_file(output_path)
    show(self.plot)


def randomize_graph(size=10):
    graph = Graph()
    for i in range(size):
        graph.add_vertex(str(i))

    for vertex in graph.vertices.keys():
        vertices = list(graph.vertices.keys())
        vertices.remove(vertex)
        if random() > 0.7:
            num_connections = randint(0, 3)
            if num_connections > 0:
                for i in range(num_connections):
                    end = choice(vertices)
                    vertices.remove(end)
                    graph.add_edge(vertex, end)

    # graph.depth_first_search()
    graph.breadth_first_search()

    bokeh = BokehGraph(graph,'Graph',20,20)
    bokeh.show()

if __name__ == '__main__':
    randomize_graph(25)

# test = Graph()  # Instantiate your graph

# test.add_vertex('A')
# test.add_vertex('B')
# test.add_vertex('C')
# test.add_vertex('D')
# test.add_vertex('E')
# test.add_vertex('F')
# test.add_vertex('G')
# test.add_vertex('H')

# test.add_edge('A', 'B')
# test.add_edge('A', 'C')
# test.add_edge('D', 'E')
# test.add_edge('G', 'H')

# test.depth_first_search()

# graph = BokehGraph(test)
# graph.show()