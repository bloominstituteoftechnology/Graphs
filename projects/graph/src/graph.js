/**
 * Edge
 */
export class Edge {
  // TODO: i think that by adding origin here
  // we can save a loop in the draw.
  constructor(destination, weight = 0, drawWeight = false) {
    this.destination = destination;
    this.weight = weight;
    this.drawWeight = drawWeight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'default', pos = { x: -1, y: -1 }, fillColor = 'white') {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.fillColor = fillColor;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    console.log('called Graph constructor');
    this.vertexes = [];
    this.found = [];
    this.queueToSearch = [];
  }

  debugCreateTestData() {
    console.log('called debugCreateTestData()');
    let debugVertex1 = new Vertex('t1', { x: 40, y: 40 });
    let debugVertex2 = new Vertex('t2', { x: 80, y: 80 });
    let debugVertex3 = new Vertex('t3', { x: 40, y: 80 });

    let debugEdge1 = new Edge(debugVertex2); // 1 to 2
    debugVertex1.edges.push(debugEdge1);

    let debugEdge2 = new Edge(debugVertex3); // 2 to 3
    debugVertex2.edges.push(debugEdge2);

    let debugEdge3 = new Edge(debugVertex1);
    debugVertex3.edges.push(debugEdge3); // 3 to 1

    this.vertexes.push(debugVertex1, debugVertex2, debugVertex3);
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      const randWeight = () => {
        return Math.floor(Math.random() * 10 + 1);
      };
      v0.edges.push(new Edge(v1, randWeight(), true));
      v1.edges.push(new Edge(v0, randWeight(), false));
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
   */
  bfs(start) {
    // !!! IMPLEMENT ME
    // 0. Pick a random color.
    let randColor =
      'rgb(' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ')';
    // 1. Take start and add it to our found list and to the queue and add color.
    // const found = [];
    // const queueToSearch = [];
    this.found.push(start);
    this.queueToSearch.push(start);
    start.fillColor = randColor;
    // 2. For each edge in queue[0]'s edge array, if destination is not in found list:
    //    a. add to found list.
    //      Method 1: Save a list of this stuff.
    //      Method 2: Add a flag to a vertex that says it's found.
    //      Method 3: add color property.
    //    b. add to the end of the queue.
    //    c. add color property.
    // 3. Dequeue queue[0].
    // 4. If queue is not empty, go to step 2 (while loop).
    while (this.queueToSearch.length > 0) {
      for (let edge of this.queueToSearch[0].edges) {
        if (!this.found.includes(edge.destination.value)) {
          this.found.push(edge.destination.value);
          this.queueToSearch.push(edge.destination);
          edge.destination.fillColor = randColor;
        }
      }
      this.queueToSearch.shift();
    }
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // 1. Go to next unfound vertex in graph.vertexes and call BFS on it.
    // 2. Go to Step 1, until we get to end of the array (Loop).
    for (let vertex of this.vertexes) {
      if (!this.found.includes(vertex.value)) {
        this.bfs(vertex);
      }
    }
  }
}
