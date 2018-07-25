#!/usr/bin/python
import numpy as np
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, "label"):
            raise Exception("This is not a vertex!")
        self.vertices.add(vertex)

    def _get_labels(self):
        label_data = {"x": [], "y": [], "name": []}
        for vertex, edges in self.pos.items():
            label_data["x"].append(edges[0])
            label_data["y"].append(edges[1])
            label_data["name"].append(vertex)
        print("label", label_data)
        label_source = ColumnDataSource(label_data)
        print("label source:", label_source)

        labels = LabelSet(
            x="x",
            y="y",
            text="name",
            text_color="white",
            level="glyph",
            text_align="center",
            text_baseline="middle",
            text_line_height=1,
            source=label_source,
            render_mode="canvas",
        )
        self.plot.add_layout(labels)


class Vertex:
    """Vertices have a label and a set of edges."""

    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class ListGraph:
    """Adjacency list graph."""

    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, "label"):
            raise Exception("This is not a vertex!")
        self.vertices.add(vertex)
   
    def dfs(start, reset=true) {
        const component = [];
        const stack = [];

    if (reset) {
      for (let v of this.vertexes) {
        v.color = 'white';}
    }

    stack.push(start);

    while (stack.length > 0) {
      const u = stack.pop();
      if (u.color === 'white') {
        u.color = 'gray';
        for (let e of u.edges) {
          stack.push(e.destination);}
      }

      stack.unshift(); // de-stack
      u.color = 'black';

      component.push(u);}

    return component;}

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    const componentsList = [];

    let needReset = true;

    for (let v of this.vertexes) {
      if (needReset || v.color === 'white') {
        const component = this.dfs(v, needReset);
        needReset = false;

        componentsList.push(component);
      }
    }

    return componentsList;
  }
"""
General drawing methods for graphs using Bokeh.
"""


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, title='Graph', width=10, height=10,
                 show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        self.plot = figure(title=title, x_range=(
            0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))


def main():
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")
    graph.add_vertex("7")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    graph.add_edge("7", "5", False)



# Random Graph
adj = np.random.randint(0,2,(n,n))
n = np.random.randint(1, N+1)