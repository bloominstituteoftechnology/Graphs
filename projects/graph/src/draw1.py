# In draw.py, implement the BokehGraph class. The constructor should accept a 
# Graph object (as you implemented in part 1), and optionally other parameters
# configuring e.g. graphical settings. The show method should use Bokeh to 
# generate and display HTML that draws the graph - the included Pipfile will 
# install Bokeh and necessarily dependencies.This is purposefully open-ended, 
# so feel free to get creative. But also, ask questions to avoid being blocked, 
# and generally discuss and work from lecture examples.


"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph1 import Graph
from bokeh.palettes import Spectral8


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    
    def drawGraph(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(graph.vertices)
        
        # figure class (imported above) creates a new Figure for plotting. class Figure(*ark, **kw) is a subclass of Plot that simplifies plot creation with default axes, grids, tools, etc.
        plot = figure(title = 'Adrian\'s Graph Demo', x_range = (-10,10), y_range = (-10,10))
        
        # GraphRenderer class: maintains separate sub-GlyphRenderers for the graph nodes and the graph edges. This allows for customizing the nodes by modifying the GraphRenderer’s node_renderer property. 
        #   -edge_renderer attribute: Instance of GlyphRenderer class containing an MultiLine Glyph that will be rendered as the graph edges.
        #   -node_renderer attribute: Instance of GlyphRenderer class containing an XYGlyph (point-like Glyph) that will be rendered as the graph nodes.
        graphRenderer = GraphRenderer()

        # data_source attribute of Glyphrenderer: Local data source to use when rendering glyphs on the plot. Instance of the DataSource class. The DataSource class is a an abstract base class used to help organize the hierarchy of Bokeh model types. It is not useful to instantiate on its own.
        # Two requirements for data sources belonging to node_renderer and edge_renderer
        #   -The ColumnDataSource (i.e. a JSON dict that maps names to arrays of values) associated with the node sub-renderer must have a column named "index" that contains the unique indices of the nodes.
        #   -The ColumnDataSource associated with the edge sub-renderer has two required columns: "start" and "end". These columns contain the node indices of for the start and end of the edges.
        # ColumnDataSource is a bokeh class that maps names of columns to sequences or arrays. It's a fundamental data structure of Bokeh. Most plots, data tables, etc. will be driven by a ColumnDataSource.
        graphRenderer.node_renderer.data_source.add(node_indices, 'index')

        # spectral8 (a color palette) specifies the range of colors used for the plot markers
        graphRenderer.node_renderer.data_source.add(Spectral8, 'color')

        # specifies the shape and style of the plot markers (i.e. graph nodes in our case)
        # GlyphRenderer class attr glyph: Instance of Glyph class. Specifies glyph to render, in conjunction with the supplied data source and ranges.
        graphRenderer.node_renderer.glyph = Circle(radius=0.2, fill_color='color')

        # The ColumnDataSource associated with the edge sub-renderer has two required columns: "start" and "end". These columns contain the node indices of for the start and end of the edges.
        # data attribute of ColumnDataSource class : Mapping of column names to sequences of data. The data can be, e.g, Python lists or tuples, NumPy arrays, etc.
        start_indices = []
        end_indices = []

        for vertex in graph.vertices:
            for edge_end in graph.vertices[vertex].adjVertices:
                start_indices.append(vertex)
                end_indices.append(edge_end)
            print(start_indices)
            print(end_indices)
        
        graphRenderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)



### start of layout code
# circ here is a list populated with the different angles of a circle (i.e. 0 to 2*pi)
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

# the zip() method: The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
graph_layout = dict(zip(node_indices, zip(x, y)))

# StaticLayoutProvider base class: bokeh.models.graphs.LayoutProvider (abstract data type. not useful on its own.)
# graph_layout attribute of StaticLayoutProvider: The coordinates of the graph nodes in cartesian space. The dictionary keys correspond to a node index and the values are a two element sequence containing the x and y coordinates of the node. (property type: Dict ( Either ( String , Int ), Seq ( Any ) ))
# By default the StaticLayoutProvider will draw straight-line paths between the supplied node positions. In order to supply explicit edge paths you may also supply lists of paths to the edge_renderer bokeh.models.sources.ColumnDataSource. The StaticLayoutProvider will look for these paths on the "xs" and "ys" columns of the data source. Note that these paths should be in the same order as the "start" and "end" points.
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot here is an instantiation of the Figure class (A subclass of Plot that simplifies plot creation with default axes, grids, tools, etc.)
# renderers is an attribute of Plot. Description:A list of all renderers for this plot, including guides and annotations in addition to glyphs and markers. property type: List ( Instance ( Renderer ) ). Recall that Renderer is an abstract base class used to help organize the hierarchy of Bokeh model types. It is not useful to instantiate on its own.
plot.renderers.append(graph)

# output_file(): Configures the default output state to generate output saved to a file when show() is called. (https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.output_file)
output_file('graphEx1.html')
# show(): Immediately displays a Bokeh object or application. (https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.show)
show(plot)






















###### Bookeh example for Visualizing Network Graphs (https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html) ##########
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
# "Bokeh uses a separate LayoutProvider model in order to supply the coordinates of a graph in Cartesian space. Currently the only built-in provider is the StaticLayoutProvider model, which contains a dictionary of (x,y) coordinates for the nodes.""
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

N = 8
node_indices = list(range(N))

# figure class (imported above) creates a new Figure for plotting. class Figure(*ark, **kw) is a subclass of Plot that simplifies plot creation with default axes, grids, tools, etc.
plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

# GraphRenderer class: maintains separate sub-GlyphRenderers for the graph nodes and the graph edges. This allows for customizing the nodes by modifying the GraphRenderer’s node_renderer property. 
#   -edge_renderer attribute: Instance of GlyphRenderer class containing an MultiLine Glyph that will be rendered as the graph edges.
#   -node_renderer attribute: Instance of GlyphRenderer class containing an XYGlyph (point-like Glyph) that will be rendered as the graph nodes.
graph = GraphRenderer()

# data_source attribute of Glyphrenderer: Local data source to use when rendering glyphs on the plot. Instance of the DataSource class. The DataSource class is a an abstract base class used to help organize the hierarchy of Bokeh model types. It is not useful to instantiate on its own.
# Two requirements for data sources belonging to node_renderer and edge_renderer
#   -The ColumnDataSource (i.e. a JSON dict that maps names to arrays of values) associated with the node sub-renderer must have a column named "index" that contains the unique indices of the nodes.
#   -The ColumnDataSource associated with the edge sub-renderer has two required columns: "start" and "end". These columns contain the node indices of for the start and end of the edges.
# ColumnDataSource is a bokeh class that maps names of columns to sequences or arrays. It's a fundamental data structure of Bokeh. Most plots, data tables, etc. will be driven by a ColumnDataSource.
graph.node_renderer.data_source.add(node_indices, 'index')

# spectral8 (a color palette) specifies the range of colors used for the plot markers
graph.node_renderer.data_source.add(Spectral8, 'color')

# specifies the shape and style of the plot markers (i.e. graph nodes in our case)
# GlyphRenderer class attr glyph: Instance of Glyph class. Specifies glyph to render, in conjunction with the supplied data source and ranges.
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

# The ColumnDataSource associated with the edge sub-renderer has two required columns: "start" and "end". These columns contain the node indices of for the start and end of the edges.
# data attribute of ColumnDataSource class : Mapping of column names to sequences of data. The data can be, e.g, Python lists or tuples, NumPy arrays, etc.
graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
# circ here is a list populated with the different angles of a circle (i.e. 0 to 2*pi)
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

# the zip() method: The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
graph_layout = dict(zip(node_indices, zip(x, y)))

# StaticLayoutProvider base class: bokeh.models.graphs.LayoutProvider (abstract data type. not useful on its own.)
# graph_layout attribute of StaticLayoutProvider: The coordinates of the graph nodes in cartesian space. The dictionary keys correspond to a node index and the values are a two element sequence containing the x and y coordinates of the node. (property type: Dict ( Either ( String , Int ), Seq ( Any ) ))
# By default the StaticLayoutProvider will draw straight-line paths between the supplied node positions. In order to supply explicit edge paths you may also supply lists of paths to the edge_renderer bokeh.models.sources.ColumnDataSource. The StaticLayoutProvider will look for these paths on the "xs" and "ys" columns of the data source. Note that these paths should be in the same order as the "start" and "end" points.
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot here is an instantiation of the Figure class (A subclass of Plot that simplifies plot creation with default axes, grids, tools, etc.)
# renderers is an attribute of Plot. Description:A list of all renderers for this plot, including guides and annotations in addition to glyphs and markers. property type: List ( Instance ( Renderer ) ). Recall that Renderer is an abstract base class used to help organize the hierarchy of Bokeh model types. It is not useful to instantiate on its own.
plot.renderers.append(graph)

# output_file(): Configures the default output state to generate output saved to a file when show() is called. (https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.output_file)
output_file('graphEx1.html')
# show(): Immediately displays a Bokeh object or application. (https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.show)
show(plot)

