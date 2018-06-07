/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination) {
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value='default', pos={x: -1, y: -1}, edges = [], color) {
    this.edges = edges;
    this.value = value;
    this.pos = pos;
    this.color = color;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    console.log('called graph constructor');
    this.vertexes = [];
  }

  debugCreateTestData() {
    console.log('called debugCreateTestData');
    let debugVertex1 = new Vertex('t1', {x: 100, y: 100});
    let debugVertex2 = new Vertex('t2', {x: 100, y: 400}, [new Edge(debugVertex1)]);
    let debugVertex3 = new Vertex('t3', {x: 400, y: 100}, [new Edge(debugVertex2), new Edge(debugVertex1)]);

    this.vertexes.push(debugVertex1);
    this.vertexes.push(debugVertex2);
    this.vertexes.push(debugVertex3);

    console.log(this.bfs(this.vertexes[0]));
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    this.vertexes = [];
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
    //1. pick a random color
    const pickRandomColor = () => {
      let colorDigits = '#';
      [...Array(6).keys()].forEach(() => {
        colorDigits += (Math.floor(Math.random()*8)+7).toString(16);
      })
      return colorDigits;
    }
    let found = [];
    let queue = [start];
    let current = {};
    let color = pickRandomColor();
    //2. choose first vertex and add to found list
    while (queue.length) {
      current = queue.pop();
      current.edges.forEach(edge => {
        if (!edge.destination.color) {
          queue.push(edge.destination);
          found.push(edge.destination);
          edge.destination.color = color;
        }
      });
    }
    //3. for each edge in queue[0].edges, if destination not in found list:
    //  a. add to found list
    //  b. add to the end of the queue
    //  c. add color property
    //4. Dequeue queue[0]
    //5. if queue is not empty go to step 2.
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    /*connected components
    1. go to next unfound vertex in graph and call BFS on it
    2. go to step 1 
    */
    const components = [this.vertexes];
    for (let v of this.vertexes) {
      if (this.vertexes) {
        const component = this.bfs(v);
        components.push(component);
      }
    }
    return components;
  }
}