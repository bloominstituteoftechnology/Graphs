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
  constructor(value='default', pos={x: -1, y: -1}, color='white') {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.color = color;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  // createDummyGraph() {
  //   const dummyVertex1 = new Vertex('v1', {x: 20, y: 25});
  //   const dummyVertex2 = new Vertex('v2', {x: 100, y: 25});
  //   const dummyVertex3 = new Vertex('v3', {x: 500, y: 605});
  //   this.vertexes.push(dummyVertex1);
  //   this.vertexes.push(dummyVertex2);
  //   this.vertexes.push(dummyVertex3);
  // }

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
  bfs(start, rgbColor) {
    // !!! IMPLEMENT ME
    // Step 1. pick a random color
    let randomColor = 'rgb(' + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ')';
    // bfs logic here
    // Step 2. Take start and add it to our component list
    const component = [];
    component.push(start);
    // Step 3. Add to the queue
    let queue = [];
    queue.push(start);
    // Step 4. Add a color
    start.color = rgbColor;
    // Step 5. Check to see if queue is empty
    // if not empty continue down the loop
    while (!queue.isEmpty()) {
      // for edge
      const vertex = queue[0];
      for (let edge of vertex.edges) {
        // if destination is not in component
        if (!component.includes(edge.destination)) {
          // add to component array
          component.push(edge.destination);
          // add to the end of the queue
          queue.push(edge.destination);
          // add color
          edge.destination.color = rgbColor;
        }
      }
    }
    // Step 6. Dequeue queue
    queue.dequeue();
    return component;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
   //const component = this.bfs(vertex);
    // choose a random color
    // apply that color to every vertex in component array
  }
}
