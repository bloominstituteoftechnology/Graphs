/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'v') {
    this.value = value;
    this.edges = [];
    this.color = 'black';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.connectedComponents = [];
  }

  debugCreateVertex() {
    let d1 = new Vertex('d1');
    let d2 = new Vertex('d2');

    d1.pos = { x: 200, y: 200 };
    d2.pos = { x: 100, y: 100 };

    let e1 = new Edge(d2);

    d1.edges.push(e1);

    this.vertexes.push(d1, d2);
  }

  reset() {
    this.vertexes = [];
    this.connectedComponents = [];
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
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
            connectVerts(grid[ y ][ x ], grid[ y + 1 ][ x ]);
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[ y ][ x ], grid[ y ][ x + 1 ]);
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
        grid[ y ][ x ].pos = {
          x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
        };
      }
    }

    // Finally, add everything in our grid to the vertexes in this Graph
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        this.vertexes.push(grid[ y ][ x ]);
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
  bfs(start, reset = true) {
    let component = [];
    let queue = [];
    if (reset) {
      for (let v of this.vertexes) {
        v.color = 'white';
      }
    }

    start.color = 'grey';

    queue.push(start);

    while (queue.length > 0) {
      let current = queue[ 0 ];

      for (let edge of current.edges) {
        if (edge.destination.color === 'white') {
          edge.destination.color = 'grey';
          queue.push(edge.destination);
        }
      }

      queue.shift();
      current.color = 'black';
      component.push(current);
    }
    return component;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    let reset = true;

    for (let v of this.vertexes) {
      if (v.color === 'white' || reset) {
        let component = this.bfs(v, reset);
        reset = false;
        this.connectedComponents.push(component);
      }
    }
  }
}
