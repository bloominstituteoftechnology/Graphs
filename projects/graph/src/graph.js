/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {
    this.weight = weight;
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = '', pos = { x: -1, y: -1 }) {
    this.value = value;
    this.pos = pos;
    this.edges = [];
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
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let weights = Math.floor((Math.random() * 10)) + 1; // Randomly pick a weight from 1 - 10
      v0.edges.push(new Edge(v1, weights)); 
      v1.edges.push(new Edge(v0, weights));
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
            connectVerts(grid[y][x], grid[y + 1][x]);
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x + 1]);
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
  bfs(start) {
    // !!! IMPLEMENT ME
    const returnArray = [start];
    let inclusion = { [`${start.value}`]: 1 };

    let loop_extract = (vertex) => {
      let { edges } = vertex;

      edges.forEach(edge => {
        // Ensuring that we do not have loops
        if (inclusion[`${edge.destination.value}`] === undefined) {
          returnArray.push(edge.destination); // Vertex is Pushed in the Array
          inclusion[`${edge.destination.value}`] = 1;
          loop_extract(edge.destination);
        }
      });
    };
    loop_extract(start);
    return returnArray;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    let returnArray = [];
    // Loop over all vertices in the graph
    // If the vertex.edges array contains anything
    // Push it inside the returnArray
    this.vertexes.forEach(vertex => {
      if (vertex.edges.length >= 1) {
        returnArray.push(vertex);
      }
    });
    // Return an array of vertices that contain connections.
    return returnArray;
  }
}

// let mg = new Graph();

// mg.randomize(3, 3, 20);

// mg.dump();

// let mgArr = mg.bfs(mg.vertexes[0]);
// mgArr.forEach(item => {
//   console.log('Item: ', item.value);
// });

// let myConnected = mg.getConnectedComponents();
// myConnected.forEach(item => {
//   console.log('Connected: ', item);
// });