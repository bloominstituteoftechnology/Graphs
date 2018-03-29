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
  constructor(value = 'vertex', pos = { x: -1, y: -1 }) {
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

  debugCreateTestData() {
    // console.log("Debug: Ran debugCreateTestData()");

    // new verts
    let debugVert1 = new Vertex('dv1', { x: 50, y: 20 });
    let debugVert2 = new Vertex('dv2', { x: 100, y: 100 });
    let debugVert3 = new Vertex('dv3', { x: 50, y: 200 });
    let debugVert4 = new Vertex('dv4', { x: 230, y: 80 });
    let debugVert5 = new Vertex('dv5', { x: 500, y: 40 });
    let debugVert6 = new Vertex('dv6', { x: 200, y: 300 });
    let debugVert7 = new Vertex('dv7', { x: 450, y: 230 });

    // new edge
    let edge1 = new Edge(debugVert3);
    let edge3 = new Edge(debugVert4);
    let edge4 = new Edge(debugVert5);
    let edge5 = new Edge(debugVert6);
    let edge6 = new Edge(debugVert7);
    let edge7 = new Edge(debugVert6);

    // add edges to array
    debugVert1.edges.push(edge1);
    debugVert3.edges.push(edge3);
    debugVert4.edges.push(edge4);
    debugVert5.edges.push(edge5);
    debugVert6.edges.push(edge6);
    debugVert4.edges.push(edge7);

    // add verts to array
    this.vertexes.push(debugVert1, debugVert2, debugVert3, debugVert4, debugVert5, debugVert6, debugVert7);

  }

  /**
   * Create a random graph
   */
  // randomize(width, height, pxBox, probability = 0.6) {
  //   // Helper function to set up two-way edges
  //   function connectVerts(v0, v1) {
  //     v0.edges.push(new Edge(v1));
  //     v1.edges.push(new Edge(v0));
  //   }

  //   let count = 0;

  //   // Build a grid of verts
  //   let grid = [];
  //   for (let y = 0; y < height; y++) {
  //     let row = [];
  //     for (let x = 0; x < width; x++) {
  //       let v = new Vertex();
  //       //v.value = 'v' + x + ',' + y;
  //       v.value = 'v' + count++;
  //       row.push(v);
  //     }
  //     grid.push(row);
  //   }

  //   // Go through the grid randomly hooking up edges
  //   for (let y = 0; y < height; y++) {
  //     for (let x = 0; x < width; x++) {
  //       // Connect down
  //       if (y < height - 1) {
  //         if (Math.random() < probability) {
  //           connectVerts(grid[y][x], grid[y + 1][x]);
  //         }
  //       }

  //       // Connect right
  //       if (x < width - 1) {
  //         if (Math.random() < probability) {
  //           connectVerts(grid[y][x], grid[y][x + 1]);
  //         }
  //       }
  //     }
  //   }

  //   // Last pass, set the x and y coordinates for drawing
  //   const boxBuffer = 0.8;
  //   const boxInner = pxBox * boxBuffer;
  //   const boxInnerOffset = (pxBox - boxInner) / 2;

  //   for (let y = 0; y < height; y++) {
  //     for (let x = 0; x < width; x++) {
  //       grid[y][x].pos = {
  //         'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
  //         'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
  //       };
  //     }
  //   }

  //   // Finally, add everything in our grid to the vertexes in this Graph
  //   for (let y = 0; y < height; y++) {
  //     for (let x = 0; x < width; x++) {
  //       this.vertexes.push(grid[y][x]);
  //     }
  //   }
  // }

  // /**
  //  * Dump graph data to the console
  //  */
  // dump() {
  //   let s;

  //   for (let v of this.vertexes) {
  //     if (v.pos) {
  //       s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):';
  //     } else {
  //       s = v.value + ':';
  //     }

  //     for (let e of v.edges) {
  //       s += ` ${e.destination.value}`;
  //     }
  //     console.log("s", s);
  //   }
  // }

  /**
   * BFS
   */
  bfs(start) { // start at index 0 of this.vertexes array
    // !!! IMPLEMENT ME
    console.log("start", start);
    console.log("this.vertexes", this.vertexes);

    let nodes = this.vertexes;
    let visitedNodes = [];
    let queue = [];

    for (let i = 0; i < nodes.length; i++) { // go through entire node
      queue.push(i); // add node to nodes to visit list
      visitedNodes.push(i); // add node to visited list
      for (let i = 0; i < queue.length; i++) { // go through each node
        if (!visitedNodes[i] === queue[i]) { // check to see if node isn't in list of nodes to visit
          visitedNodes.push(i); // add child node to list of nodes to visit;
        }
      }
      queue.shift(i); // remove current node from queue
    }
    console.log("visitedNodes", visitedNodes);
    return visitedNodes; // return visited nodes

  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}