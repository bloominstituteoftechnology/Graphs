# Drawing Connected Components

This is a multi-stage project to draw a graph and show the connected
components of that graph in different colors.


## Part 1: Graph, Vertex, Edge Classes

In the file `graph.py`, implement a `Graph` class that supports the API expected
by `draw.py`. In particular, this means there should be a field `vertices` that
contains a dictionary mapping vertex labels to edges. For example:

```python
{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}
```

This represents a graph with four vertices and two total (bidirectional) edges.
The vertex `'2'` has no edges, while `'0'` is connected to both `'1'` and `'3'`.

You should also create `add_vertex` and `add_edge` methods that add the
specified entities to the graph. To test your implementation, instantiate an
empty graph and then try to run the following:

```python
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
```

You should see something like the first example. As a stretch goal, add checks
to your graph to ensure that edges to nonexistent vertices are rejected.

```python
# Continuing from previous example
graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
```


## Part 2: Drawing with Bokeh

In `draw.py`, implement the `BokehGraph` class. The constructor should accept a
`Graph` object (as you implemented in part 1), and optionally other parameters
configuring e.g. graphical settings. The `show` method should use Bokeh to
generate and display HTML that draws the graph - the included `Pipfile` will
install Bokeh and necessarily dependencies.

This is purposefully open-ended, so feel free to get creative. But also, ask
questions to avoid being blocked, and generally discuss and work from lecture
examples.

Helpful resources:
- https://bokeh.pydata.org/en/latest/
- https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html

To test your implementation, try drawing your graph from part 1, and share your
result with the class!


## Part 3: Draw a Random Graph

In `graph_demo.py` write a function that demonstrates `Graph` and `BokehGraph`
by instantiating a random graph and drawing it. The main parameters should be
the number of vertices and the number of edges - for instance, you could have 4
vertices and 6 edges. Edges should by default by bidirectional, be added
randomly and should be unique. You should pick reasonable default parameters,
but also allow them to be passed in as arguments.

*Challenge question* - what's the largest number of edges you should allow?
Think about this, and if you think you know the answer add it as a check to
reject input when the number of edges is too large.

`graph_demo.py` is set to be executable from the command line, e.g.
`python graph_demo.py`. You can use `argv` (already imported) to parse command
line arguments, e.g. `python graph_demo.py arg1 arg2`, and pass them along to
the graph and drawing functionality to further configure.

Suggested functionality that could be set via arguments:
- Directional edges: allow edges to not be bidirectional (this will change how
many you would allow maximum)
- Layout: should it be random, or set to follow a pattern?
- Jitter/bounding boxes: how should layout be tuned to avoid overlap?
- Colors: again should they be random, specified, or somewhere in betwen?
- Output: configure where the file is output, or support other Bokeh outputs
- Edge probability: this would replace the number of edges, and instead be a
probability between 0 and 1 of the likelihood of an edge between any two
vertices (supporting this *and* edge number is a bit tricky, but good to try)

As with number of vertices and edges, pick reasonable defaults so the user
doesn't have to specify anything to get results (i.e. `python graph_demo.py`
alone should do something). You don't need to do all of these arguments, and you
can also come up with your own - any feature that you think would be cool to
expose for the user to configure is worth considering.

Modify the `GraphView` code to draw the graph itself.


## Part 4: Implement Breadth-First Search (or Depth-First Search)

This is a necessary step in figuring out the connected components. Add methods
to the `Graph` class to support search - you can add a `bfs` method, `dfs`,
both, or a general `search` method that takes an argument to specify type.

For implementing depth-first search, try to use a stack instead of recursion.
Hint: Python lists already have the methods needed to function as a stack (`pop`
and `append`).


## Part 5: Color the Connected Components Differently

It's likely the random graphs have multiple connected components. Add a function
to `graph_demo.py` that uses search to identify them, and sets each vertex in a
component to be the same color so when drawn they look something like this:

![Connected Components Mockup](https://raw.githubusercontent.com/LambdaSchool/Graphs/master/projects/graph/UI_UX%20Mockup.png)

It is also suggested to add another command line argument to `graph_demo.py` to
allow you to select whether or not connected components should run (i.e. to
choose between just drawing a random graph, and drawing a random graph with the
connected components indicated by common color).


## Part 6: Refactor

You've come a long way - time to hit the linter and clean up your code. You
should ensure your code conforms to
[pep8](https://www.python.org/dev/peps/pep-0008/), the standard Python style.

There are many tools to help, your editor may have built in support already
(look for squiggly lines below text and colored dots on the left). If you don't
already have something set up, check out
[Flake8](http://flake8.pycqa.org/en/latest/).

In addition to style, think if there's more substantial refactoring you should
do - do the methods you have in each class make sense, or would they be more
appropriate somewhere else? Do names of methods you intend for your use (and not
the use of people who would reuse your code) start with `_`? In general, are you
picking good variable names, writing informative comments, and all that other
good stuff?

Picture two audiences for your code - coworkers, and future you. Both will care
and benefit from your code being as readable as possible.


### Stretch 1: Interactivity

Add interactivity to the generated graph - a widget that enables drawing a new
random graph would be a great feature:
https://bokeh.pydata.org/en/latest/docs/user_guide/interaction/widgets.html#userguide-interaction-widgets

### Stretch 2: Random edge weights

Add random edge weights, integers from 1-10. Draw the weight near the center of the edge.

> Hint: the center of a line is at point _x_,_y_, where _x_ is the average of
> the x coordinates of the endpoints of the line, and _y_ is the average of the
> y coordinates of the endpoints of the line.

Even though there are two edges between each connected vertex on the graph,
there should only be one label (since the edges are effectively a single,
non-directed edge.)

### Stretch 3: Clicks

Figure out which vertex a user is clicking on when they click with a mouse.
Log the vertex value when they do to test (you can just use `print`, or see the
Python library for logging: https://docs.python.org/3.5/library/logging.html).

Use this input processing to allow the user to select two vertices. Again Bokeh
interactivity documentation will be key to implementing this functionality.

### Stretch 4: Dijkstra

Implement [Dijkstra's
Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the
shortest route between starting and ending points from Stretch 3.

Highlight the route.

### Stretch 5: Travelling saleperson

Read about the [travelling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
This is a *hard* problem, literally, so even as a stretch goal a real
implementation is not expected - but it's an interesting and famous problem
in the space, and worth learning about if you want to go deep in graphs.
