/**
 * Edge
 */
export class Edge {
  constructor(destination) {
    this.destination = destination;
    this.weight = Math.floor(Math.random() * Math.floor(10));
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'init', pos = {x: 0, y: 0}, found = false) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.found = found;
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
  bfs(start) {
    const queue = [start];
    const found = [];

    start.found = true;

    while (queue.length > 0) {
      const head = queue[0];

      for (let edge of head.edges) {
        const vert = edge.destination;
        if (vert.found === false) {
          vert.found = true;
          queue.push(vert);
        }
      }
      queue.shift();
      found.push(head);
    }
    return found;
  }

  dfs(start) {
    const stack = [start];
    const found = [];

    dfsLoop: while (stack.length > 0) {
      if (stack[0].edges.length === 0) {
        found.push(stack[0]);
      }

      for (let edge of stack[0].edges) {
        if (edge.destination.found === false) {
          edge.destination.found = true;
          found.push(edge.destination);
          stack.unshift(edge.destination);
          continue dfsLoop;
          }
        }
      stack.shift();
    }
    return found;
  }

  /**
   * Get the connected components
   */
  getConnectedComponentsBFS() {
    const ccList = [];

    for (let vertex of this.vertexes) {
      if (vertex.found === false) {
        ccList.push(this.bfs(vertex));
      }
    }
    return ccList;
  }

  getConnectedComponentsDFS() {
    const ccList = [];

    for (let vertex of this.vertexes) {
      if (vertex.found === false) {
        ccList.push(this.dfs(vertex));
      }
    }
    return ccList;
  }
}
