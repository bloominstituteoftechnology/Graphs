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
  constructor(value= 'default', pos={x: -1, y: -1}) {
    this.edges = []; 
    this.value; 
    this.pos = pos; 
    this.searched = false; 
    this.color = 'black'; 
  }
}
//function for random color generation
function randomColor() {
  let letters = '0123456789ABCDEF'; 
  let color = '#'; 

  for(let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)]; 
  }
  return color; 
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }
createDummyGraph() {
  const dummyVertex1 = new Vertex('v1', {x: 20, y: 25}); 
  const dummyVertex2 = new Vertex('v2', {x:100, y:75}); 
  const dummyVertex3 = new Vertex('v3', {x: 500, y: 605}); 

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
    let queue = []; 
    let random = randomColor(); 

    queue.push(start); 
    start.searched = true; 

    while (queue.length > 0) {
      const vertex = queue[0]; 
      vertex.color = random; 

      for (let edge of vertex.edges) {
        if(!edge.destination.searched) {
          queue.push(edge.destination);
          edge.destination.searched = true; 
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
    const componentList = []; 

    let needReset = true; 

    for (let v of this.vertexes) {
      if (needReset || v.color === 'white') {
        const component = this.bfs(v, needReset); 
        needReset = false; 

        componentList.push(component); 
      }
    }

    return componentList; 
  }
}
