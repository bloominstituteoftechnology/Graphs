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

  // BFS(graph, startVert):
  // for v of graph.vertexes:
  //   v.color = white

  // startVert.color = gray
  // queue.enqueue(startVert)

  // while !queue.isEmpty():
  //   u = queue[0]  // Peek at head of queue, but do not dequeue!

  //   for v of u.neighbors:
  //     if v.color == white:
  //       v.color = gray
  //       queue.enqueue(v)

  //   queue.dequeue()
  //   u.color = black

  bfs(start) {
    const queue = [];

    for (let v of this.vertexes) {
      v.color = "red"; // initialize every vertex as not visited
    }

    start.color = "green"; // mark the starting vertex as visited
    queue.push(start); // add the starting vertex to the queue

    while (queue.length > 0) {
      // keep checking vertexes for neighbors until queue is empty
      let current = queue[0];

      for (let neighbor of current.edges) {
        if (neighbor.color === "red") {
          // add all unvisited vertices to the queue
          neighbor.color = "green";
          queue.push(neighbor);
        }
      }
      queue.shift();
      current.color = "black"; // mark the start a unique color
    }
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {}
}
