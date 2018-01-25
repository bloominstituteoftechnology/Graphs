/**
 * Edge
 */
export class Edge {
  constructor(dest, weight = null) {
    this.destination = dest;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(val) {
    this.edges = [];
    this.value = val;
    this.color = null;
    this.pos = {
      x: null,
      y: null
    };
    this.minDistance = null;
  }
}

class PriorityQueue {
  constructor() {
    this.data = [];
  }

  enqueue(item, priority) {
    this.data.push([item, priority]);
    this.sort();
  }

  dequeue() {
    return this.data.shift()[0];
  }

  isEmpty() {
    return !this.data.length;
  }

  sort() {
    this.data.sort((a, b) => a[1] - b[1]);
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
      const weight = ~~(Math.random() * 10 + 1);
      v0.edges.push(new Edge(v1, weight));
      v1.edges.push(new Edge(v0, weight));
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
    const visited = [];

    const q = [];
    start.color = "gray";
    q.push(start);

    while (q.length) {
      let u = q.shift();

      u.edges.forEach(e => {
        const vert = e.destination;
        if (vert.color === "white") {
          vert.color = "gray";
          q.push(vert);
        }
      });
      u.color = "black";
      visited.push(u);
    }

    return visited;
  }

  dijkstraShortestPath(start, end) {
    const q = new PriorityQueue();
    const distances = {};
    const prev = {};
    let path = [];

    distances[start.value] = 0;

    for (let v of this.vertexes) {
      if (v !== start) {
        distances[v.value] = Number.POSITIVE_INFINITY;
      }
      prev[v.value] = null;
      q.enqueue(v, distances[v.value]);
    }

    while (!q.isEmpty()) {
      let smallest = q.dequeue();
      if (smallest === end) {
        path = [];

        while (prev[smallest.value]) {
          path.push(smallest);
          smallest = prev[smallest.value];
        }

        break;
      }

      if (!smallest || distances[smallest.value] === Number.POSITIVE_INFINITY) {
        continue;
      }

      for (let adj of smallest.edges) {
        let alt = distances[smallest.value] + adj.weight;
        if (alt < distances[adj.destination.value]) {
          distances[adj.destination.value] = alt;
          prev[adj.destination.value] = smallest;

          q.enqueue(adj.destination, alt);
        }
      }
    }

    return path;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    const connectedComponents = [];
    this.vertexes.forEach(v => (v.color = "white"));
    this.vertexes.forEach(v => {
      if (v.color === "white") {
        const component = this.bfs(v);
        connectedComponents.push(component);
      }
    });

    return connectedComponents;
  }
}
