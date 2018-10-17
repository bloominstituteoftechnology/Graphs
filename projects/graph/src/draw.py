"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import viridis


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graphStorage):
        self.graphStorage = graphStorage

    def show(self, graphstyle='square', graphcolor="connectedOnly"):

        node_indices = list(map(int,  self.graphStorage.keys()))

        plot = figure(title="Graph Layout Demonstration", x_range=(-1.1, 1.1),
                      y_range=(-1.1, 1.1), tools="", toolbar_location=None)
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        if graphcolor is "viridis":
            graph.node_renderer.data_source.add(viridis(len(node_indices)), 'color')
        elif graphcolor is "connectedOnly":
            outputArr = []
            for node in self.graphStorage:
                if len(self.graphStorage[node]) > 0:
                    outputArr.append('green')
                else:
                    outputArr.append('black')
            graph.node_renderer.data_source.add(outputArr, 'color')

        else:
            graph.node_renderer.data_source.add([graphcolor] *len(node_indices), 'color')
        
        graph.node_renderer.glyph = Circle(radius=.05, fill_color='color')
        x = []
        y = []
        for key in self.graphStorage:
            for num in self.graphStorage[key]:
                x.append(key)
                y.append(num)
        graph.edge_renderer.data_source.data = dict(start=x, end=y)
        if graphstyle == "circle":
            circ = [i*2*math.pi/len(node_indices) for i in node_indices]
            xpos = [math.cos(i) for i in circ]
            ypos = [math.sin(i) for i in circ]
        elif graphstyle == "square":
            pointDistribation = 4/len(node_indices)
            totalTrack = 0
            counter = 0 
            xpos=[]
            ypos=[]
            while(counter  < len(node_indices) ):
                if totalTrack <= 1:
                    xPosition = (totalTrack )-.5
                    xpos.append(xPosition)
                    ypos.append(-.5)
                elif totalTrack >1 and totalTrack <=2:
                    yPosition = (totalTrack )-1.5
                    xpos.append(.5)
                    ypos.append(yPosition)
                elif totalTrack >2 and totalTrack <=3:
                    xPosition = (totalTrack )-2.5
                    xpos.append(-xPosition)
                    ypos.append(.5)
                elif totalTrack >3 and totalTrack <=4:
                    yPosition = (totalTrack )-3.5
                    xpos.append(-.5)
                    ypos.append(-yPosition)    
                totalTrack+=pointDistribation
                counter +=1
                               
            
        graph_layout = dict(zip(node_indices, zip(xpos, ypos)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        source = ColumnDataSource(
            dict(xvals=xpos, yvals=ypos, name=node_indices))

        labels = LabelSet(x='xvals', y='yvals', text='name', text_align='center',
                       level='glyph',text_baseline='middle', source=source, text_color='white')

        plot.renderers.append(graph)
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)
