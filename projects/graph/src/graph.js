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
    this.color = 'white';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    console.log('called graph constructor');
    this.vertexes = [];
  }

  // debugCreateTestData() {
  //   console.log('called debugCreateTestData()');
  //   let debugVertex1 = new Vertex('t1', { x: 50, y: 40 });
  //   let debugVertex2 = new Vertex('t2', { x: 150, y: 55 });
  //   let debugVertex3 = new Vertex('t3', { x: 300, y: 75 });
  //   let debugVertex4 = new Vertex('t4', { x: 40, y: 95 });
  //   let debugVertex5 = new Vertex('t5', { x: 40, y: 95 });
  //   let debugVertex6 = new Vertex('t6', { x: 40, y: 95 });
  //   let debugVertex7 = new Vertex('t7', { x: 40, y: 95 });
  //   let debugVertex8 = new Vertex('t8', { x: 40, y: 95 });
  //   let debugVertex9 = new Vertex('t9', { x: 40, y: 95 });
  //   let debugVertex10 = new Vertex('t10', { x: 40, y: 95 });
  //   let debugVertex11 = new Vertex('t11', { x: 40, y: 95 });
  //   let debugVertex12 = new Vertex('t12', { x: 40, y: 95 });
  //   let debugVertex13 = new Vertex('t13', { x: 40, y: 95 });
  //   let debugVertex14 = new Vertex('t14', { x: 40, y: 95 });
  //   let debugVertex15 = new Vertex('t15', { x: 40, y: 95 });
  //   let debugVertex16 = new Vertex('t16', { x: 40, y: 95 });
  //   let debugVertex17 = new Vertex('t17', { x: 40, y: 95 });
  //   let debugVertex18 = new Vertex('t18', { x: 40, y: 95 });
  //   let debugVertex19 = new Vertex('t19', { x: 40, y: 95 });

  //   console.log(debugVertex1);
  //   let debugEdge1 = new Edge(debugVertex2);
  //   debugVertex1.edges.push(debugEdge1);

  //   let debugEdge2 = new Edge(debugVertex3);
  //   debugVertex2.edges.push(debugEdge2);

  //   this.vertexes.push(
  //     debugVertex1,
  //     debugVertex2,
  //     debugVertex3,
  //     debugVertex4,
  //     debugVertex5,
  //     debugVertex6,
  //     debugVertex7,
  //     debugVertex8,
  //     debugVertex9,
  //     debugVertex10,
  //     debugVertex11,
  //     debugVertex12,
  //     debugVertex13,
  //     debugVertex14,
  //     debugVertex15,
  //     debugVertex16,
  //     debugVertex17,
  //     debugVertex18,
  //     debugVertex19
  //   );
  // }

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
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
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

    //Breadth First Search(start)

    // 0. Pick a colour

    let randColor =
      'rgb(' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ')';

    // 1. Take start and add it to our found list and add to the queue and add colour

    // Method One - Keep a list of what we've found
    // -> Advantages - We can easily query the list. Reference number found.
    //                 When we're done, we have a list ready to go
    //                 If we make on list per CC, then we lists of them.

    let queue = [];
    let found = [];
    found.push(start);

    queue.push(start);

    start.color = randColor;

    while (queue.length > 0) {
      const v = queue[0];

      for (let edge of v.edges) {
        if (!found.includes(edge.destination)) {
          found.push(edge.destination);
          queue.push(edge.destination);
          edge.destination.color = randColor;
        }
      }

      queue.shift();
    }

    return found;

    // 2. For each edge in queue[0] edge array, if destination is not in found list
    //    a. Add to found list
    //       Method 1: Save a list of this stuff
    //       Method 2: Adda a flag to a vertex that says its found
    //       Method 3: Use color to mark found vertexes
    //    b. Add to the end of the queue
    //    c. Add colour property
    // 3. Dequeue queue[0]
    // 4. If queue is not empty, go to step 2
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    let searched = [];
    for (let vertex of this.vertexes) {
      if (!searched.includes(vertex)) {
        searched = searched.concat(this.bfs(vertex));
      }
    }
  }
}
