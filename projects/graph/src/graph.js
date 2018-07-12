const randomColor = () => {
  const dec = Math.floor(Math.random() * 256);
  return dec.toString(16);
}

/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {  //need a default weight since weight isnt specified on Edge creation on line 37/38
    this.destination = destination;
    this.weight = weight;  //will take default weight of 1 but can be changed
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'default', pos = {x: -1, y: -1}) {  //Vertex is made without a value so setting a 'default' value which can be changed
    this.edges = [];  //list of edges
    this.value = value;
    this.pos = pos;
    this.color = '#' + randomColor() + randomColor() + randomColor();
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];  //list of vertexes
  }

  createDummyGraph() {
    const dummyVertex1 = new Vertex('v1', {x:20, y:25});
    const dummyVertex2 = new Vertex('v2', {x:200, y:250});
    const dummyVertex3 = new Vertex('v3', {x:400, y:500});

    this.vertexes.push(dummyVertex1);
    this.vertexes.push(dummyVertex2);
    this.vertexes.push(dummyVertex3);
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v1));
      v1.edges.push(new Edge(v0));
      v1.color = v0.color;
      // if(v0.edges.length >= v1.edges.length) v1.color = v0.color;
      // else v1.color = v0.color; 
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
            // grid[y+1][x].color = grid[y][x].color;
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x+1]);
            // grid[y][x+1].color = grid[y][x].color;
          }
        }
      }
    }

    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.6;
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
        s += ` ${e.destination.value} is ${e.destination.color}`;
      }
      console.log(s);
    }
  }

  /**
   * BFS
   */
  bfs(start) {
    // !!! IMPLEMENT ME    
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}
