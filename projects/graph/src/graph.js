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
  constructor(value='default', pos={x: -1, y:-1}) {
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
    let queue = [];
    let checked = [];

    //adding the var start to the queue
    queue.push(start);

    //starting the queue
    while (queue.length > 0) {
      let base = queue[0];
      //loop threw all the edges
      for (let i = 0; i < base.edges.length; i++) {
        //checking if the edges are in the queue or have been added to checked and if not continuing
        if ( !(queue.includes(base.edges[i].destination) || checked.includes(base.edges[i].destination))) {
          queue.push(base.edges[i].destination);
        }
      }
      //exit condition making sure the queue will eventually end
      queue.shift();
      checked.push(base);
    }
    return checked;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents(vertexes) {
    // !!! IMPLEMENT ME
    let components = [];
    let checked = [];
    components.push(this.bfs(vertexes[0]));

    vertexes.forEach((v) => {
      let test = 0;
      for (let i = 0; i < components.length; i++) {
        if (components[i].includes(v)) checked.push(v);
        if (!(components[i].includes(v) || checked.includes(v))) components.push(this.bfs(v));
      }
    })
    // for (let i = 0; i < components.length; i++) {
    //   for (let x = 0; x < vertexes.length; i++) {
    //     if (!(components.includes(vertexes[x]))) {
    //       components.push(this.bfs(vertexes[x]));
    //     }
    //   }
    // }

    return components;

  }
}
