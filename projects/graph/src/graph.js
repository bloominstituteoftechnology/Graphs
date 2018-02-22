/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value) {
    this.value = value;
    this.edges = [];
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
      const w = Math.floor(Math.random() * 10 + 1);
      v0.edges.push(new Edge(v1, w));
      v1.edges.push(new Edge(v0, w));
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
    let queue = [];
    let complete = [];

    // for (let i = 0; i < this.vertexes.length; i++) {
    //   this.vertexes[i].color = 'white';
    // }

    start.color = 'gray';
    queue.push(start);
    
    while (queue.length > 0) {
      let u = queue[0];
      if (u.edges.length === 0) {
        u.color = 'black';
        complete.push(queue.shift());
        return(complete);
      }

      for (let j = 0; j < u.edges.length; j++) {
        if (u.edges[j].destination.color === 'white') {
          u.edges[j].destination.color = 'gray';
          // console.log(u.edges[j].destination.value);        
          queue.push(u.edges[j].destination);
        }
      }

      complete.push(queue.shift());
      // console.log(u.value);
      u.color = 'black';
    }
    // for (let i = 0; i < complete.length; i++){
    //   console.log(complete[i].value);
    // }
    return(complete);
  }
  
  dfsVisit(v) {
    v.color = 'gray';
    for (let j = 0; j < v.edges.length; j++) {
      if (v.edges[j].color === 'white') {
        v.edges[j].parent = v;
        this.dfsVisit(v.edges[j]);
      }
    }
    v.color = 'black';
  }

  dfs(graph) {
    for (let i = 0; i < this.vertexes.length; i++) {
      this.vertexes[i].color = 'white';
      this.vertexes[i].parent = null;
    }
    for (let i = 0; i < this.vertexes.length; i++) {
      if (this.vertexes[i].color === 'white') {
        this.dfsVisit(this.vertexes[i]);
      }
    }
  }


  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    let connectedComponents = []

    for (let i = 0; i < this.vertexes.length; i++) {
      this.vertexes[i].color = 'white';
    }

    for (let i = 0; i < this.vertexes.length; i++) {
      if (this.vertexes[i].color === 'white') {
        let component = this.bfs(this.vertexes[i]);
        connectedComponents.push(component);
      }
    }

    console.log(connectedComponents);
    return connectedComponents;
  }
}
