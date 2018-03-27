/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1,) {
    this.weight = weight;
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'vertex', pos = { x: -1, y: -1}) {
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
    let debugVert1 = new Vertex('dV1', {x: 50, y: 50});
    let debugVert2 = new Vertex('dV2', {x: 100, y: 100});
    let debugVert3 = new Vertex('dV3', {x: 200, y: 150});
    let debugVert4 = new Vertex('dV4', {x: 40, y: 400});
    let debugVert5 = new Vertex('dV5', {x: 400, y: 50});
    let debugVert6 = new Vertex('dV6', {x: 500, y: 500});
    let debugVert7 = new Vertex('dV7', {x: 250, y: 450});

    // to test our edge let's make a debug edge arbitrarily
    // that connects node one and node two
    // to do that we need to create an edge that belonds to debugVert1
    // and has a destination of debugVert2, which by our definition of our
    // edge class, is all we need to say that you go from one to two
    let edge1 = new Edge(debugVert2);
    let edge2 = new Edge(debugVert4);
    let edge3 = new Edge(debugVert7);
    debugVert1.edges.push(edge1);
    debugVert2.edges.push(edge2);
    debugVert3.edges.push(edge3);
    //console.log check here>>>


    this.vertexes.push(debugVert1);
    this.vertexes.push(debugVert2);
    this.vertexes.push(debugVert3);
    this.vertexes.push(debugVert4);
    this.vertexes.push(debugVert5);
    this.vertexes.push(debugVert6);
    this.vertexes.push(debugVert7);


  }
  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let random = Math.floor(Math.random() * 5);
      v0.edges.push(new Edge(v1, random));
      v1.edges.push(new Edge(v0, random));
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
    // !!! IMPLEMENT ME
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}
