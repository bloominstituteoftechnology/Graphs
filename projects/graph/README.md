# Drawing Connected Components

This is a multi-stage project to draw a graph and show the connected
components of that graph in different colors.

A designer on your team has provided a mockup for what the final product should look like:  https://github.com/LambdaSchool/Graphs/blob/master/projects/graph/UI:UX%20Mockup.png

Note that it should not always appear exactly like this.  The vertexes, edges, and colors should vary randomly each time the program is run.  

## Phase 1: Graph, Vertex, Edge Classes

In the file `graph.js`, add code that implements `Graph`, `Vertex`, and
`Edge` classes.

For this project, you should have the `Graph` contain a list of
`Vertex`es, and have each `Vertex` contain a list of `Edge`s. Each
`Edge` would have a `destination` and a `weight`.

**NOTE**: A later phase of this project will make use of code in
`graph.js` that generates random graphs, called `randomize()`. Examine
this code for clues as to how to implement `Graph`, `Vertex` and `Edge`
so that it interfaces with the `randomize()` code.

You can make the functions in `graph.js` available to code in other
files with the `export` keyword:

```javascript
export class Graph { 
  // ...
```

## Phase 2: HTML Canvas and React

A _canvas_ in HTML is a bitmap that you can draw to using various
drawing primitives. We'll use this to draw our graph on the screen.

Here is some example boilerplate for implementing a canvas component in
React and drawing to it:

```javascript
class GraphView extends Component {
  componentDidMount() {
    this.update();
  }

  componentDidUpdate() {
    this.update();
  }

  update() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear the canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw some stuff
    // ...
  }

  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}
```

Use Google-fu to figure out how to draw lines (for edges) and circles (for vertexes).


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
