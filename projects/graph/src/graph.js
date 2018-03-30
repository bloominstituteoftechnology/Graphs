import { getRandomColor } from './utils';
/**
 * Edge
 */
export class Edge {
  /**
   * @param {Vertex} destination
   * @param {number} weight
   */
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  /**
   * @param {string} value
   * @param {Object} pos
   * @param {number} pos.x
   * @param {number} pos.y
   * @param {string} color inside color of the vertex
   */
  constructor(value = '', pos = { x: -1, y: -1 }, color) {
    this.value = value;
    this.pos = pos;
    this.color = color;

    /** @type {Array<Edge>} */
    this.edges = [];
  }
}
/**
 * Graph
 */
export class Graph {
  constructor() {
    /**@type {Array<Vertex>}*/
    this.vertexes = [];
  }

  debugCreateTestData() {
    const debugVert1 = new Vertex('dv1', { x: 10, y: 10 });
    const debugVert2 = new Vertex('dv2', { x: 100, y: 100 });
    const debugVert3 = new Vertex('dv3', { x: 50, y: 200 });
    const debugVert4 = new Vertex('dv4', { x: 40, y: 500 });
    const debugVert5 = new Vertex('dv5', { x: 500, y: 40 });
    const debugVert6 = new Vertex('dv6', { x: 20, y: 600 });
    const debugVert7 = new Vertex('dv7', { x: 250, y: 450 });
    const edge1 = new Edge(debugVert2);
    const edge2 = new Edge(debugVert4);
    const edge3 = new Edge(debugVert7);
    debugVert1.edges.push(edge1);
    debugVert2.edges.push(edge2);
    debugVert3.edges.push(edge3);
    this.vertexes.push(debugVert1, debugVert2, debugVert3, debugVert4, debugVert5, debugVert6, debugVert7);
  }

  /**
   * Create a random graph
   * @param {Number} width xCount rendering multiplier
   * @param {Number} height yCount rendering multiplier
   * @param {Number} pxBox size of the canvas rendering box
   * @param {number} probability
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
          x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
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
   * @param {Vertex} start
   * @returns {Array<Vertex>}
   */
  bfs(start) {
    const connected = [];
    const queue = [start];
    const color = getRandomColor();

    while (queue.length) {
      const current = queue.shift();

      for (const { destination } of current.edges) {
        if (!destination.color) {
          // no color == not touched yet
          queue.push(destination);
        }
      }

      current.color = color;
      connected.push(current);
    }

    return connected;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}
