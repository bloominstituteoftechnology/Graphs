#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex
from flask import Flask, render_template
from bokeh.client import pull_session
from bokeh.embed import server_session

app = Flask(__name__)

app.route('/', methods=['GET'])

def main(num_vertices=8, num_edges=8, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()

def bkapp_page():
  with pull_session(url="http://localhost:8000/") as session:
    script = server_session(session_id=session.id, url="http://localhost:8000/")
    return render_template("embed.html", script=script, template="Flask")

if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
        app.run(port=8000)
    else:
        print('Expected arguments: num_vertices num_edges draw_components')
        print('Both numbers should be integers, draw_components should be 0/1')
