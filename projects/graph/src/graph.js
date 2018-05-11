/**
 * Edge
 */
export class Edge {
  constructor(destination, weight = 0) {
    this.destination = destination;
    this.weight = weight;
  }
}

/*
 * Vertex
 */
export class Vertex {
  constructor(value = '', pos = { x:0, y:0 }) {
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
    this.queue = [];
    this.found = [];
    this.foundValues = [];
  }

  debugCreateDummyData() {
    let dumbVertex1 = new Vertex ('d1', { x:100, y:100 });
    let dumbVertex2 = new Vertex ('d2', { x:200, y:200 });

    this.vertexes.push(dumbVertex1, dumbVertex2);

    let dumbEdge1 = new Edge (dumbVertex2);

    dumbVertex1.edges.push(dumbEdge1);
    
    console.log({ 'dumbVertex1.edges': dumbVertex1.edges })
    
    // });
  }
  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      const randomWeight = (max,min) => {
        return Math.trunc(Math.random() * (max - min) + min);
      }
      v0.edges.push(new Edge(v1, randomWeight(10, 1)));
      v1.edges.push(new Edge(v0, randomWeight(10, 1)));
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

  getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
  
    for (let i = 0; i <6; i++) {
      color += letters[Math.floor(Math.random()*16)];
    }
    return color;
  }

  /**
   * BFS
   */
  bfs(start) {
    // !!! IMPLEMENT ME
    let { found, queue, foundValues } = this;
    let current = [];
    current.color = this.getRandomColor();
    found.unshift(current); 
    queue.push(start);
    current.push(start);
    foundValues.push(start.value);
    while (queue.length > 0) {
      queue[0].edges.forEach((edge) => {
        if (!foundValues.includes(edge.destination.value)) {
          foundValues.push(edge.destination.value);
          current.push(edge.destination);
          queue.push(edge.destination);
        }
      });
      queue.shift();
    }
    // console.log('found', found);
    return found;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    let { foundValues } = this;
    for (let vertex of this.vertexes) {
      if (!foundValues.includes(vertex.value)) {
        this.bfs(vertex);
      }
    }
  }
}
