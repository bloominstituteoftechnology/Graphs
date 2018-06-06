import { colors } from './colors';
/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination) {
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'default', pos = { x: -1, y: -1 }) {
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

  debugCreateVertexes() {
    const vertexes = [
      new Vertex('t1', { x: 10, y: 30 }),
      new Vertex('t2', { x: 60, y: 90 }),
      new Vertex('t3', { x: 700, y: 200 }),
      new Vertex('t4', { x: 690, y: 500 }),
      new Vertex('t5', { x: 130, y: 160 }),
      new Vertex('t6', { x: 200, y: 300 }),
      new Vertex('t7', { x: 400, y: 400 }),
      new Vertex('t8', { x: 130, y: 660 }),
      new Vertex('t9', { x: 200, y: 100 }),
      new Vertex('t10', { x: 600, y: 130 }),
      new Vertex('t11', { x: 230, y: 360 }),
      new Vertex('t12', { x: 400, y: 300 }),
    ];

    let e1 = new Edge(vertexes[0]); // 0 to 1 === t1 to t2
    vertexes[1].edges.push(e1);

    let e2 = new Edge(vertexes[1]); // 1 to 2 === t2 to t3
    vertexes[2].edges.push(e2);

    vertexes.forEach(v => this.vertexes.push(v));
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
    // Breadth First Search(start)
    // 0. Pick a random color
    // 1. Take start and add it to our found list and add to the queue and add color
    // 2. For each edge in queue[0]'s edge array, if destination is not in found list:
    //    a. add to found list
    //    //Methods
    //    //Method 1: have a list of this stuff
    //    //Method 2: add a found flag to a vertex
    //    //Method 3: use color to mark found
    //    b. add to end of the queue
    //    c. add color property
    // 3. Dequeue queue[0]
    // 4. if queue is not empty, Go to step 2 (while loop/recursion)

    // pick a random color
    const color = colors[Math.floor(Math.random() * colors.length)];

    // init a found list and queue
    const foundVertexList = [start];
    const queue = [start];

    // init a vertex variable just to make things readable
    let vertex;
    while (queue.length) {
      // get the vertex at the start of the queue and assign it to the vertex variable
      vertex = queue[0];

      // assign the vertext the color
      vertex.color = color;

      // loop through the vertex edges
      vertex.edges.forEach(edge => {
        // check if the destinations are not in the found vertex list
        if (!foundVertexList.includes(edge.destination)) {
          // add to the found vertex list and queue
          foundVertexList.push(edge.destination);
          queue.push(edge.destination);
        }
      });

      // dequeue
      queue.shift();
    }

    return foundVertexList;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // Connected Components
    // 1. Go to the next unfound vertex in graph vertexes and call BFS on it
    // 2. Go to step 1 until we get to the end of the array(loop)

    let searched = [];

    this.vertexes.forEach(vertex => {
      if (!searched.includes(vertex)) {
        searched = searched.concat(this.bfs(vertex));
      }
    });
    console.log(searched);
  }
}
