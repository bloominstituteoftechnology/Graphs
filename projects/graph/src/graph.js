/**
 * Edge
 */
export class Edge {
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'vertex', pos = {x: 50, y: 50}) {
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
    let queue = [start];          // initialize queue with start vertex value
    let knownVertexes = [start];  // initialize knownVertexes vertex list with start vertex value
    let current;                  // tracker for current vertex

    while (queue.length > 0) {    // while there are still vertexes to check in the queue
      current = queue.shift();
      if (this.vertexes[current].edges) {   // if the current vertex has edges
        for (let i = 0; i < this.vertexes[current].edges.length; i++) {
          // get the edge's destination value
          const destination = parseInt(this.vertexes[current].edges[i].destination.value.slice(1), 10);
          if (!knownVertexes.includes(destination)) {  // if the destination hasn't been seen yet
            queue.push(destination);          // add destination to the queue
            knownVertexes.push(destination);  // add destination to the knownVertexes list
          }
        }
      }
    }
    return knownVertexes;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    let vertex = 0;                   // vertex tracker, starting search from zero
    let componentCount = 0;           // number of components
    let masterVisitedVertexes = [];   // vertexes in all explored components
    let newVisitedVertexes = [];      // vertexes in last explored component
    let connectedComponentsList = []; // array to store components found
    let allVertexesVisited = false;   // boolean used to control loop, exits when all are visited

    // main loop to traverse all vertexes
    do {
      // do a bfs of component starting from current vertex value
      newVisitedVertexes = this.bfs(vertex);

      // copy the newly explored component into the components found array
      connectedComponentsList[componentCount++] = newVisitedVertexes;

      // update master list of visited vertexes with vertexes in most recent component
      for (let i = 0; i < newVisitedVertexes.length; i++) {
        masterVisitedVertexes[newVisitedVertexes[i]] = true;
      }
      // set control status then check for unvisited vertexes
      allVertexesVisited = true;
      for (let i = 0; i < this.vertexes.length; i++) {
        if (masterVisitedVertexes[i] !== true) {
          allVertexesVisited = false;
          vertex = i;
          break;
        }
      }
    } while (!allVertexesVisited);

    return connectedComponentsList;
  }
}
