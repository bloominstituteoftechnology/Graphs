/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value='vertex') {
    this.value = value;
    this.edges = [];
    this.color = 'white';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v1));
      v1.edges.push(new Edge(v0));
    }

    let count = 0;
    this.vertexes.length = 0;

    // Build a grid of verts
    let grid = [];
    for (let y = 0; y < height; y++) {
      let row = [];
      for (let x = 0; x < width; x++) {
        let v = new Vertex();
        //v.value = 'v' + x + ',' + y;
        v.value = 'v' + count++;
        row.push(v);
      }
      grid.push(row);
    }

    // Go through the grid randomly hooking up edges
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        // Connect down
        if (y < height - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y+1][x]);
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x+1]);
          }
        }
      }
    }

    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.8;
    const boxInner = pxBox * boxBuffer;
    const boxInnerOffset = (pxBox - boxInner) / 2;

    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        grid[y][x].pos = {
          'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
        };
      }
    }

    // Finally, add everything in our grid to the vertexes in this Graph
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        this.vertexes.push(grid[y][x]);
      }
    }
  }

  /**
   * Dump graph data to the console
   */
  dump() {
    let s;

    for (let v of this.vertexes) {
      if (v.pos) {
        s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):';
      } else {
        s = v.value + ':';
      }

      for (let e of v.edges) {
        s += ` ${e.destination.value}`;
      }
      console.log(s);
    }
  }

  /**
   * BFS
   */
  // We begin each BFS by 
  bfs(start, reset=true) {
    // !!! IMPLEMENT ME

    // Create a queue to store components (WHAT ARE THESE COMPONENTS?????????????????????????????????????????????)
    const component = [];

    // Create a queue to store the verts still in review
    const queue = [];

    // Every time we run the BFS, it resets for a new search
    // Since each new BFS run has reset = true, we are essentially saying "always do the following upon a new BFS"
    if (reset) {
      // Go through the vertexes array...
      for (let v of this.vertexes) {
        // ...and reset all vert colors to white
        v.color = 'white';
      }
    }

    // Each time we look to a node for review, we will set its color to gray
    start.color = 'gray';

    // This pushes the list of vertices from the queue into the vertex array "start" is pointing to
    queue.push(start);

    // As long as the queue isn't empty...
    while (queue.length > 0) {
      // We set the first item in queue to equal the variable "u"
      const u = queue[0];

      // ... we will search every item at the front of the queue for its edges...
      for (let e of u.edges) {
        // ...and for said edges' destinations
        const v = e.destination;
        
        // If the color of the queued vertex is white...
        if (v.color === 'white') {

          // ...we will set its color to gray while it is under review
          v.color = 'gray';

          // If we find edges,then we add those edges' connected verticies (v) to the queue
          queue.push(v);
        }
      }

      // Once the vertex is no longer under review, we will take it out of the queue...
      queue.shift(); // de-queue

      // ...and change its color to black
      u.color = 'black';

      // This pushes the first item in the queue into the component array
      component.push(u);
    }

    // Returns the component array
    return component;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    const componentsList = [];

    let needReset = true;

    for (let v of this.vertexes) {
      if (needReset || v.color === 'white') {
        const component = this.bfs(v, needReset);
        needReset = false;

        componentsList.push(component);
      }
    }

    return componentsList;
  }
}
