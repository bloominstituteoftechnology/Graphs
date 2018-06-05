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
  constructor(value = 'vertex', pos = { x: 0, y: 0 }) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  found = [];

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    this.vertexes = [];

    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let randomWeight = (Math.floor(Math.random()*10) + 1);
      v0.edges.push(new Edge(v1, randomWeight));
      v1.edges.push(new Edge(v0, randomWeight));
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
        s += ` ${e.destination.value}, weight: ${e.weight}`;
      }
      console.log(s);
    }
  }

  /**
   * BFS
   */
  bfs(vertex) {
    // !!! IMPLEMENT ME
    // 1. Add the start vertex to the queue
    // 2. Add the start vertex to the current found array
    // 3. Go to the first item in the queue
    //    a.  if queue if empty, stop
    // 4. Check the first vertex for neighbors
    //    a. for each new neighbor found, add it to current found array and the queue
    // 5. Dequeue first item in queue
    // 6.  Go to step 3.

    let vertexConnections = [];
    let queue = [];
    queue.push(vertex);
    this.found.push(vertex);

    while (queue.length) {
      for (let edge of queue[0].edges) {
        let isNew = true;
        for (let j = 0; j < this.found.length; j++) {
          if (this.found[j].value === edge.destination.value) isNew = false;
        }
        if (isNew) {
          queue.push(edge.destination);
          this.found.push(edge.destination);
        }
        isNew = true;
      }
      vertexConnections.push(queue.shift());
    }
    return vertexConnections;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    this.found = [];
    // !!! IMPLEMENT ME
    // 1. Loop through the list of vertexes, for each unfound vertex,
    //    Do BFS for that item(start)
    let allVertexConnections = [];
    for (let vertex of this.vertexes) {
      //globally scope found
      let flag = true;
      for (let i = 0; i < this.found.length; i++) {
        if (this.found[i].value === vertex.value) flag = false;
      }
      if (flag) {
        allVertexConnections.push(this.bfs(vertex));
      }
      flag = true;
    }

    return allVertexConnections;
  }
}
