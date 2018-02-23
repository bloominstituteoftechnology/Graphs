/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight) {
    // this.weight = weight; do later
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor() {
    this.visited = false;
    this.edges = [];
    this.parent = null;
    this.color = 'white';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.currentIndex = 0;
    this.stack = [];
    this.visited = [];
    this.vertexes = [];

  }


  startBFS() {
    let refresh = setInterval(() => {
      action();
    }, 1000);
    let action = () => {
      this.bfs(this.currentIndex);
      if (this.stack.length === 0) {
        clearInterval(refresh);
      }
    }
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

    if (start === undefined) {
      start = this.vertexes[0];
    } else {
      start = this.vertexes[start];
    }
    //console.log(this)
    // this.state.updateCanvas();
    console.log('start', this.vertexes[start])
    let stack = this.stack;
    if (this.stack.length === 0) stack.push(start);
    let u = stack[0];
    console.log(u.edges[0])
    //if (u.edges) {
    u.edges.forEach(e => {
      let vert = e.destination;
      if (vert.color === 'white') {
        vert.color = 'grey';
        stack.push(vert);
      }
    })
    //} else {
    u.visited = true;
    u.color = 'black';
    this.visited.push(stack[0]);
    stack.shift();
    if (this.stack.length === 0) this.getConnectedComponents() //color edges
    //}
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    console.log('getting connected components');
    for (var i = 0; i < this.vertexes.length; i++) {
      if (this.vertexes[i].visited === false) {
        this.currentIndex = i;
        console.log(this);
        this.startBFS();
        return;
      }
    }
  }
}
