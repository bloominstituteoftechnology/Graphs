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
  constructor(value) {
    this.edges = [];
    this.value = value;
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
    function connectVerts(v0, v1) {
      const weight = Math.floor(Math.random() * 10) + 1
      v0.edges.push(new Edge(v1, weight));
      v1.edges.push(new Edge(v0, weight));
    }
    let count = 0;
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
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        if (y < height - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y+1][x]);
          }
        }
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x+1]);
          }
        }
      }
    }

    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.5;
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
    const searched = [];

    queue.push(start);
    
    while (queue.length > 0) {
      const head = queue[0];
      for (let i = 0; i < head.edges.length; i++) {
        if (!(queue.includes(head.edges[i].destination) || searched.includes(head.edges[i].destination))) {
          queue.push(head.edges[i].destination);
        }
      }
      queue.shift();
      searched.push(head);
    }
    return searched;
  }
  /**
   * Get the connected components
   */
  getConnectedComponents() {
    const connectedComp = [];
    const searched = [];
    for (let v of this.vertexes) {
      if (!searched.includes(v)) {
        const subgraph = this.bfs(v);
        for (let subv of subgraph) {
          searched.push(subv);
        }
        connectedComp.push(subgraph);
      }
    }
    return connectedComp;
  }
}
