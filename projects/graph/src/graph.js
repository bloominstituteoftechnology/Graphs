/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  //Passed in a destination and weight into the constructor and passed it to this.

  constructor(destination, weight) {
    this.weight = weight;
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  //Contains a list of edges like graph contains a list of vertexes
  //Pos has values within for the x and y value.
  //Also a value part of it within
  //Not certain if i need to pass in pos
  constructor(value = 'default', pos={x: -1, y:-1}) {
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

  // createDummyGraph() {
  //   const dummyV1 = new Vertex('1', {x: 10, y:10})
  //   this.vertexes.push(dummyV1);
  // }
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
    // !!! IMPLEMENT ME
    const queue = [];
    const searched = new Set();
    
    start.color = 'pink';
    queue.push(start);

    // start.visited = false;

    while(queue.length > 0) {
      let bfs = queue[0];
      for(let e of bfs.edges) {
        const dest = e.destination;
        if(dest.color === 'white') {
          dest.color = 'pink';
          // dest.visited = true;
          queue.push(dest);
        }
      }
      queue.shift();
      bfs.color = 'purple';
      searched.add(bfs);
    }
    return searched;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    const connected_components = new Set();

    for(let v of this.vertexes) {
      if(v.color === 'white'){
        const component = this.bfs(v);
        connected_components.add(component);
      }
    }
    return connected_components;
  }
}
