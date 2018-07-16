/**
 * Edge
 */
export class Edge {
  constructor(destination, weight, middle) {
    this.destination = destination;
    this.weight = weight;
    this.middle = middle;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = "default", pos = { x: -1, y: -1 }) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
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

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let weight = Math.sqrt(
        Math.pow(v0.pos.y - v1.pos.y, 2) + Math.pow(v0.pos.x - v1.pos.x, 2)
      );
      let middle = {
        x: (v1.pos.x + v0.pos.x) / 2,
        y: (v1.pos.y + v0.pos.y) / 2
      };

      if (weight < 39) weight = 0;
      else if (weight < 58) weight = 1;
      else if (weight < 77) weight = 2;
      else if (weight < 96) weight = 3;
      else if (weight < 110) weight = 4;
      else if (weight < 130) weight = 5;
      else if (weight < 150) weight = 6;
      else if (weight < 170) weight = 7;
      else if (weight < 190) weight = 8;
      else weight = 9;

      v0.edges.push(new Edge(v1, weight, middle));
      v1.edges.push(new Edge(v0, weight, middle));
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
  bfs(startVert) {
    let queue = [];
    let temp = new Set();

    startVert.color = "gray"; //set current vertex to gray
    queue.push(startVert);

    while (queue.length > 0) {
      let u = queue[0]; // Peek at head of queue, but do not dequeue!

      u.edges.forEach(v => {
        if (v.destination.color === "white") {
          v.destination.color = "gray";
          queue.push(v.destination);
        }
      });
      temp.add(...queue);
      queue.shift();
      u.color = "black";
    }
    return temp;
  } //bfs
}
