import math

"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure, output_file, show
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Oval)
from bokeh.palettes import Spectral8
# from bokeh.charts import Scatter, output_file, show

N = 8
node_indices = list(range(N))

# dataframe=pandas.DataFrame(columns=["X", "Y"])
# dataframe["X"]=[1,2,3,4,5]
# dataframe["Y"]=[5,6,4,5,3]

# p=Scatter(dataframe, x="X", y="Y", title="Temperature Observations", xlabel="Day of observations", ylabel="Temperature")

# output_file("Scatter_charts.html")

# show(p)

# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self):
#         graph = GraphRenderer()

# p=figure(plot_width=500,plot_height=400,title="This is the title, now")
p=figure(
    plot_width=500,
    plot_height=400,
    title="Learning to Graph using Bokeh",
    tools='',
    toolbar_location=None
)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(['red'] * N, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices
)

# layout
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot = figure(title="graph layout demo", x_range=(-1.1,1.1), y_range=(-1.1,1.1), tools='', toolbar_location=None)

plot.renderers.append(graph)

# p.circle([1,2,3,4,5],[5,6,5,5,3],size=5,color="red")
# p.triangle([1,2,3,4,5],[5,6,5,5,3],size=12,color="red")
p.circle([1,2,3,4,5],[5,6,5,5,3],size=[25,50,12,6,100],color="red")

output_file("Scatter_plotting.html")
show(p)
show(plot)