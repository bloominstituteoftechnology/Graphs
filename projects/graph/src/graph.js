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
  constructor(value='fred', pos={x: 0, y: 0}) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.visited = false;
    this.color = 'white';
  }

  setColor(color) {
    this.color = color;
  }

  visit() {
    this.visited = true;
  }

}

function randomColor() {
  const scm = new ColorScheme();
  scm.from_hue(35).scheme('contrast').variation('pastel');
  const colors = scm.colors();
  return '#'+ colors[Math.floor(Math.random() * colors.length)];
  // return '#'+(Math.random()*0xFFFFFF<<0).toString(16);
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
    this.queue.push(start);
    start.visit();

    let color = randomColor();

    console.log('color: ', color);

    while(this.queue.length > 0) {
      const vertex = this.queue[0];
      vertex.setColor(color);

      for(let edge of vertex.edges) {
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
    // !!! IMPLEMENT ME

    for(let vertex of this.vertexes) {
      if(!vertex.visited) {
        this.bfs(vertex);
      }
    }
  }

  dijkstra(start, end) {

  }
}
