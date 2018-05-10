/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'vertex', pos = { x: 50, y: 50 }) {
    this.value = value;
    this.pos = pos;
    this.edges = [];
    this.color = 'black';
    this.visited = false;
  }
}

/** 
 * Generate random color
*/
function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

/**
 * Generate random weight
 */
function getRandomWeight() {
  return Math.floor(Math.random() * 10) + 1;
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  // debugCreateTestData() {
  //   let vertex1 = new Vertex('tv1', { x: 50, y: 100 });
  //   let vertex2 = new Vertex('tv2', { x: 100, y: 100 });
  //   let edge1 = new Edge(vertex2);

  //   vertex1.edges.push(edge1);
  //   this.vertexes.push(vertex1, vertex2);
  // }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {

    this.vertexes = [];
    
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      const weight = getRandomWeight();

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
    let randomColor = getRandomColor();

    queue.push(start);
    start.visited = true;

    while (queue.length > 0) {
      const vertex = queue[0];
      vertex.color = randomColor;


      for (let edge of vertex.edges) {
        if (!edge.destination.visited) {
          queue.push(edge.destination);
          edge.destination.visited = true;
        }
      }

      queue.shift();
    }
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    for (let vertex of this.vertexes) {
      if (!vertex.visited) {
        this.bfs(vertex);
      }
    }
  }
}
