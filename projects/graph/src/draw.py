"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Label,
                            ColumnDataSource, Title, Instance)
from graph import Graph, Vertex
import random 

vertex = Vertex(label="", component=-1)

class BokehGraph(Graph):
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title="Coordinates", width=600, height=600,
                show_axis=True, show_grid=True, circle_size=15):
        if not graph.vertices:
            raise Exception('Graph should contain vertices')
        self.graph = graph
        # setup plot
        TOOLTIPS = [
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("name", "vertex.label")
        ]
        self.width = width
        self.height = height
        self.pos = {} #dict to map vertices (x.y coordinates)
        self.plot = figure(title=title, toolbar_location="above", tooltips=TOOLTIPS, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)
        self._get_labels()

    def _setup_graph_renderer(self, circle_size):
        #graph_renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()
        # add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(list(self.graph.vertices.keys()), "index")
        graph_renderer.node_renderer.data_source.add(self._get_random_colors(), "color")
        graph_renderer.node_renderer.glyph = Circle(size=circle_size, line_color="black", fill_color="color")
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indices()
        self.randomize()
        self.plot.add_layout(Title(text="Whys", align="left"), "left")
        self.plot.add_layout(Title(text="Exes", align="center"), "below")
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout = self.pos)
        self.plot.renderers.append(graph_renderer)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)
        
    def _get_edge_indices(self):
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


    def randomize(self):
        """Randomize vertex positions"""

        for vertex in self.graph.vertices:
            self.pos[vertex] = (random.randint(10, 500), random.randint(10, 500))
    
    def _get_labels(self):
        label_data = {"x": [], "y": [], "name": []}
        for vertex, edges in self.pos.items():
            label_data["x"].append(edges[0])
            label_data["y"].append(edges[1])
            label_data["name"].append(vertex)
        print("label", label_data)
        print("label name", label_data["name"])
        label_source = ColumnDataSource(label_data)

        labels = LabelSet(
            x="x",
            y="y",
            text="name",
            text_color="black",
            level="glyph",
            text_align="center",
            text_baseline="middle",
            text_font_size= '6pt',
            source=label_source,
            render_mode="canvas",
        )
        self.plot.add_layout(labels)
    
    

    
    def _get_random_colors(self, num_colors=None):
        colors = []
        num_colors = num_colors or len(self.graph.vertices) #not a good idea to put a function call in a default param
        for _ in range(num_colors):
            color = "#" + ''.join([random.choice("0123456789ABCDEF") for j in range(6)])
            colors.append(color)
        return colors