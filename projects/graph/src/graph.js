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
  constructor( value = 'vertex', pos = { x: -1, y: -1} ) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.fillColor = "white";
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  debugCreateTestData(){
    let debugVert1 = new Vertex('dV1', {x: 250, y: 20});
    let debugVert2 = new Vertex('dV2', {x: 200, y: 100});
    let debugVert3 = new Vertex('dV3', {x: 300, y: 100});
    let debugVert4 = new Vertex('dV4', {x: 175, y: 200});
    let debugVert5 = new Vertex('dV5', {x: 225, y: 200});
    
    let debugEdge1 = new Edge(debugVert2);
    let debugEdge2 = new Edge(debugVert3);
    let debugEdge3 = new Edge(debugVert4);
    let debugEdge4 = new Edge(debugVert5);
    debugVert1.edges.push(debugEdge1, debugEdge2);
    debugVert2.edges.push(debugEdge3, debugEdge4);

    this.vertexes.push(debugVert1, debugVert2, debugVert3, debugVert4, debugVert5);

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
  bfs(start, queue = [], visited = []) {
    const queueToVisit = queue;
    const nodesVisited = visited;
    
    nodesVisited.push(start);
    start.fillColor = this.getRandomColor(); //get random color
    
    for (let edge of start.edges) {
      if (queueToVisit.indexOf(edge.destination) === -1 && visited.indexOf(edge.destination) === -1) {
        queueToVisit.push(edge.destination);
      }
    }

    if (queueToVisit.length > 0){
      return this.bfs(queueToVisit[0], queueToVisit.slice(1), nodesVisited);
    } else { //get the first unconnected next node
      return nodesVisited;
    }
  }

  dfs(start, stack = [], visited = []) {
    const stackToVisit = stack;
    const nodesVisited = visited;

    nodesVisited.push(start);
    start.fillColor = this.getRandomColor();

    for (let edge of start.edges) {
      if (stackToVisit.indexOf(edge.destination) === 1 && nodesVisited.indexOf(edge.destination) === -1) {
        stackToVisit.push(edge.destination);
      }
    }

    if (stackToVisit.length > 1) {
      return this.dfs(stackToVisit.pop(), stackToVisit, nodesVisited);
    } else {
      return nodesVisited;
    }
  }

  getRandomColor() {
    const r = Math.random() * 255 | 0;
    const g = Math.random() * 255 | 0;
    const b = Math.random() * 255 | 0;
    return 'rgb(' + r + ", " + g +", " + b + ')';
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}