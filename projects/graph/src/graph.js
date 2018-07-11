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
  constructor(value = "default", pos = { x: -1, y: -1 }) {
    this.edges = [];
    this.value = value;
    this.pos = pos; // pos set to x: 1, y: -1
    this.color = "white";
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  /* static dummy graph */
  createDummyGraph() {
    const dummyVertex1 = new Vertex("v1", { x: 20, y: 25 });
    const dummyVertex2 = new Vertex("v2", { x: 100, y: 75 });
    const dummyVertex3 = new Vertex("v3", { x: 500, y: 605 });

    dummyVertex1.edges.push(new Edge(dummyVertex2));
    dummyVertex2.edges.push(new Edge(dummyVertex1));
    dummyVertex2.edges.push(new Edge(dummyVertex3));
    dummyVertex3.edges.push(new Edge(dummyVertex2));

    this.vertexes.push(dummyVertex1);
    this.vertexes.push(dummyVertex2);
    this.vertexes.push(dummyVertex3);
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    console.log("vertexes:", this.vertexes);
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
        v.value = "v" + count++;
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
          // converts the coordinates from decimals to intergers using bitwise OR
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
        s = v.value + " (" + v.pos.x + "," + v.pos.y + "):";
      } else {
        s = v.value + ":";
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
  bfs() {
    // !!! IMPLEMENT ME
    const component = [];
    const queue = [];

    // start vert
    // white: Unsearched, Yellow: queued for search, Black: Searched
    for (let i = 0; i < this.vertexes.length; i++) {
      if (this.vertexes[i].color === "white") {
        this.vertexes[i].color = "yellow"; // turn yellow when selected
        queue.push(this.vertexes[i]); // enqueue

        while (queue.length !== 0) {
          let u = queue[0];
          console.log("u before selected:", u);
          for (let j = 0; j < u.edges.length; j++) {
            if (u.edges[j]) {
              if (u.edges[j].destination.color === "white") {
                u.edges[j].destination.color = "yellow";
                queue.push(u.edges[j].destination);
              }
            }
          }
          queue.shift();
          u.color = "black";
        }
      }

      console.log("u after:", u);

      console.log("queue:", queue);
      console.log("vertexes:", this.vertexes);
    }

    return component;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents(vertex) {
    // !!! IMPLEMENT ME
    const component = this.bfs(vertex);
    // select random color
    // apply color to all connected vertecies
  }
}
