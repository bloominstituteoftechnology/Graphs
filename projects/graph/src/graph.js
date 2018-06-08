/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight) {
    this.destination = destination;
    this.weight = weight;
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
    this.isFound = false;
    this.distance = 0;
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
    const randomWeight = () => {
      return Math.ceil(Math.random()*10);
    }
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      const weight = randomWeight();
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
  pickRandomColor() {
    let colorDigits = '#';
    [...Array(6).keys()].forEach(() => {
      colorDigits += (Math.floor(Math.random()*8)+7).toString(16);
    })
    return colorDigits;
  }

  /**
   * BFS
   */
  bfs(start, destination) {
    // !!! IMPLEMENT ME
    //pick a random color
    let queue = [start];
    let current = {};
    let color = this.pickRandomColor();
    let distance;
    let path = [];
    //bfs and add color to all connected nodes
    while (queue.length) {
      current = queue.pop();
      const edges = current.edges.sort((a, b) => {
        return a.weight - b.weight;
      });
      //iterate over edges
      edges.forEach(edge => {
        distance = current.distance + edge.weight;
        if (!edge.destination.isFound) {
          //change destination properties to show foundness and add destination to queue
          queue.push(edge.destination);
          edge.destination.distance = distance;
          edge.destination.parent = current;
          edge.destination.color = color;
          edge.destination.isFound = true;
        }
        if (edge.destination.distance > distance) {
          //relax edges for optimal path selection
          edge.destination.parent = current;
          edge.destination.distance = distance;
          queue.push(edge.destination);
        }
      });
      if (destination && current === destination) {
        //retrace path from destination back to origin
        //should be overwritten as algorithm above optimizes
        path = [];
        const traceDestination = (node) => {
          path.unshift(node);
          if (node === start) return path;
          return traceDestination(node.parent);
        }; traceDestination(current);
      }
    } return path;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
   
    this.vertexes.forEach(vertex => {
      if (!vertex.isFound) {
        vertex.color = this.pickRandomColor();
        this.bfs(vertex);
      }
    })
  }
}