/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  };
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'vertex', pos = { x: 0, y: 0 }) {
    this.edges = [];
    this.value = value;
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

  debugCreateTestData() {
    let debugVertex1 = new Vertex('debug1', { x: 100, y: 100 });
    let debugVertex2 = new Vertex('debug2', { x: 200, y: 200});

    let debugEdge1 = new Edge(debugVertex2);

    debugVertex1.edges.push(debugEdge1);

    this.vertexes.push(debugVertex1, debugVertex2);
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

    if (this.vertexes.length > 0) this.vertexes = [];
    // Finally, add everything in our grid to the vertexes in this Graph
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        this.vertexes.push(grid[y][x]);
      }
    }
    console.log('vertexes is', this.vertexes);
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

  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}


/*
BFS Pseudocode
1. Add the first unfound vertex in the list of all vertexes to the queue
2. Add the first unfound vertex to the current found array
3. Go to the first item in the queue
  a. If queue is empty, add new found subarray and make that the current one
  b. Go to Step 1
4. Check the first vertex for neighbors
  a. For each new neighbor found, add it to current found array and queue
5. Dequeue the first item in the queue
6. Go to Step 3

Drawing Pseudocode
1. For each subarray, 
  a. Generate a random color
  b. Loop through and draw the edges
  c. Loop through and draw the vertexes

BFS Pseudocode actual implementation
1. Add the start vertex to the queue
2. Add the start vertex to the current found array
3. Go to the first item in the queue
  a. If queue is empty, stop
4. Check the first vertex for neighbors
  a. For each new neighbor found, add it to current found array and queue
5. Dequeue the first item in the queue
6. Go to Step 3

getConnectedComponents()
1. Loop through the list of vertexes, for each unfound vertex, do BFS for that item (start)
2. Go to Step 1
*/