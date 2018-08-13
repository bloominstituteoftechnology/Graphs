const ColorScheme = require('color-scheme');

/**
 * Edge
 */
export class Edge {
  constructor(destination, weight) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value='not assigned', pos={x: 0, y: 0}) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.visited = false;
    this.color = 'black';
    this.group = null;
  }

  setColor(color) {
    this.color = color;
  }

  setGroup(id) {
    this.group = id;
  }

  visit() {
    this.visited = true;
  }

}

function randomColor() {
  const scm = new ColorScheme();
  scm.from_hue(20).scheme('tetrade').variation('pastel');
  const colors = scm.colors();
  return '#'+ colors[Math.floor(Math.random() * colors.length)];
}


/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.queue = [];
    this.found = [];
  }

  refresh = () => {
    this.vertexes = [];
  }

  /**
   * Create a random graph
  */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let randomWeight = (Math.floor(Math.random()*10) + 1);
      v0.edges.push(new Edge(v1, randomWeight));
      v1.edges.push(new Edge(v0, randomWeight));
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
        s = `${v.value} (${v.pos.x},${v.pos.y}):`;
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
    this.queue.push(start);
    start.visit();

    const color = randomColor();
    const id = Math.floor(Math.random() * Math.random() * 1000);

    while(this.queue.length > 0) {
      const currentVertex = this.queue[0];
      currentVertex.setColor(color);
      currentVertex.setGroup(id);

      for(let edge of currentVertex.edges) {
        if(!edge.destination.visited) {
          this.queue.push(edge.destination);
          edge.destination.visit();
        }
      }

      this.queue.shift();
    }

  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    for(let vertex of this.vertexes) {
      if(!vertex.visited) {
        this.bfs(vertex);
      }
    }
  }

  lowestCost = (costs, processed) => {
    return Object.keys(costs).reduce((lowest, node) => {
      if (lowest === null || costs[node] < costs[lowest]) {
        if (!processed.includes(node)) {
          lowest = node;
        }
      }
      return lowest;
    }, null);
  }

  dijkstra(start, end) {
    if(start.group !== end.group) {
      throw new Error('Unreachable, this shouldnt have happened');
    }
    const unprocessed = this.vertexes.filter(elem => elem.group === start.group);

    let queue = [];
    const distanceMatrix = {};
    const prev= {};
    distanceMatrix[start.value] = 0;

    for(let vert of unprocessed) {
      if(vert !== start) {
        distanceMatrix[vert.value] = Infinity;
        prev[vert.value] = undefined;
      }
      queue.push(vert);
    }

    let ranOnce = false;
    while (queue.length > 0) {
      let currentVertex;

      if(!ranOnce) {
        currentVertex = start;
      } else {
        const temp = [...queue];
        temp.sort((a, b) => {
          return distanceMatrix[a.value] - distanceMatrix[b.value];
        });
        currentVertex = temp[0];
      }
      queue = queue.filter(vert => vert !== currentVertex);

      for(let neighbor of currentVertex.edges) {
        if(queue.includes(neighbor.destination)) {
          let alt;
          if(distanceMatrix[currentVertex.value] === Infinity) {
            alt = neighbor.weight;
          } else {
            alt = distanceMatrix[currentVertex.value] + neighbor.weight;
          }

          if (alt < distanceMatrix[neighbor.destination.value]) {
            distanceMatrix[neighbor.destination.value] = alt;
            prev[neighbor.destination.value] = currentVertex.value;
          }
        }
      }

      ranOnce = true;
    }

    const path = {};
    let u = end.value;
    while(prev[u]) {
      path[u] = prev[u];
      u = prev[u];
    }
    console.log('PATH: ', path);
    return path;
  }
}
