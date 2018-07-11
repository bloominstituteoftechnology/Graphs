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
  constructor(value, position) {
    this.value = value;
    this.edges = [];
    this.pos = {};
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

  bfs(start) {
    const queue = [];
    const component = [];

    start.color = "gray";
    queue.push(start);

    while (queue.length > 0) {
      let current = queue[0];

      for (let v of current.edges) {
        if (v.destination.color === "white") {
          v.destination.color = "gray";
          queue.push(v.destination); // add current's neighbors to the queue
        }
      }
      current.color = "black"; // current has been visited
      component.push(queue[0]);
      queue.shift(); // remove current from the queue
    }
    // component should have the start vertex, start's neighbors, and the neighbors' neighbors
    return component;
  }

  /**
   * Get the connected components
   */

  getConnectedComponents() {
    const connected_components = []; // an array of components/group of connected vertices
    for (let v of this.vertexes) {
      // mark all vertices as unvisited
      v.color = "white";
    }

    for (let v of this.vertexes) {
      if (v.color === "white") {
        let component = this.bfs(v); // find all the neighbors of unvisited vertices
        connected_components.push(component);
      }
    }

    for (let component of connected_components) {
      let redOffset = Math.random() * 256;
      let greenOffset = Math.random() * 256;
      let blueOffset = Math.random() * 256;
      // assign a random color for each component
      let color = `rgb(${redOffset}, ${greenOffset}, ${blueOffset})`;

      for (let v of component) {
        v.color = color;
      }
    }
    return connected_components;
  }
}
