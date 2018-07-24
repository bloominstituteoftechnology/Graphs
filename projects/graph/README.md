# Drawing Connected Components

This is a multi-stage project to draw a graph and show the connected
components of that graph in different colors.

A designer on your team has provided a mockup for what the final product should look like:  https://github.com/LambdaSchool/Graphs/blob/master/projects/graph/UI:UX%20Mockup.png

Note that it should not always appear exactly like this.  The vertexes, edges, and colors should vary randomly each time the program is run.  

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

This represents a graph with three vertices and two total (bidirectional) edges.
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


## Phase 2: Drawing with Bokeh

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


# Below are JS goals - they will be translated to Python shortly

## Phase 3: Draw a Random Graph

Modify the `GraphView` code to draw the graph itself.

For this, we'll use the `randomize()` code provided in `graph.js`. This
function sets up a grid of randomly jittered verts with random edges
between them. It also computes X and Y pixel values you can use to
determine where to draw things on the canvas.

```javascript
const g = new Graph();

// Create a graph with 20 nodes in a grid (5*4), with a 150x150px jitter
// box for each of them. The canvas size should be 750x600 to hold this
// graph (5*150=750, 4*150=600). The probability of any edge of the grid
// existing is 0.6.

g.randomize(5, 4, 150, 0.6);
```

The _x_ and _y_ pixel coordinates of the verts will be in the `.pos.x`
and `.pos.y` properties of the vert after `randomize()` has been called.

Once you have the graph, drawing it is a matter of iterating all the
verts and their edge destinations to draw the lines. 

After the lines are drawn, draw circles for each vert.

Finally, there is a `value` property on each vert that you can draw as
text on top of the vert circle.


## Phase 4: Implement Breadth-First Search (or Depth-First Search)

This is a necessary step in figuring out the connected components.

## Phase 5: Color the Connected Components Differently

It's likely the random graphs have multiple connected components. Choose
a random color for the edges of connected component.

## Phase 6: Add a UI Button to Generate a new Graph

Instead of hitting reload, it would be nice to have a button that you
could press to generate a new random graph and show the connected
components.

## Stretch 1:

Add random edge weights, integers from 1-10. Draw the weight near the center of the edge.

> Hint: the center of a line is at point _x_,_y_, where _x_ is the average of
> the x coordinates of the endpoints of the line, and _y_ is the average of the
> y coordinates of the endpoints of the line.

Even though there are two edges between each connected vertex on the graph,
there should only be one label (since the edges are effectively a single,
non-directed edge.)


## Stretch 2:

Figure out which vertex a user is clicking on when they click with a mouse.
`console.log` the vertex value when they do to test.

Allow the user to select two verts: starting and ending.


## Stretch 3:

Implement [Dijkstra's
Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the
shortest route between starting and ending points from Stretch 2.

Highlight the route.
