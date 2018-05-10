/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  //, weight = Math.floor(Math.random() * 10 + 1))
  constructor(destination) {
    this.destination = destination;
    // this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value, position = { x: 0, y: 0 }) {
    this.edges = [];
    this.value = value;
    this.position = position;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.memo = [];
  }

  // debugCreateTestData() {
  //   let debugVertex1 = new Vertex('A', { x: 100, y: 100 });
  //   let debugVertex2 = new Vertex('B', { x: 200, y: 200 });
  //   let debugEdge1 = new Edge(debugVertex2, 10);

  //   debugVertex1.edges.push(debugEdge1);

  //   this.vertexes.push(debugVertex1);
  //   this.vertexes.push(debugVertex2);
  // }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
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
        grid[y][x].position = {
          x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
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
      if (v.position) {
        s = v.value + ' (' + v.position.x + ',' + v.position.y + '):';
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
    for(let i = 0; i < this.memo.length; i++) {
      if (this.memo[i].value === start.value) {
        return;
      }
    }
    const queue = [];
    const found = []; //singular connection

    found.push(start); //add start to found
    queue.push(start); // add start to queue
    
    let flag = false;
    // check if array is empty
    while (queue.length) {

      let current = queue[0];
      //loop through edges of queue item
      for (let i = 0; i < current.edges.length; i++) {
        //check queue if destination vertex to add already exists
        for (let j = 0; j < queue.length; j++) {
          if (queue[j].value === current.edges[i].destination.value) {
            flag = true;
          }
        }
        //check found if destination vertex to add already exists
        for (let k = 0; k < found.length; k++) {
          if (found[k].value === current.edges[i].destination.value) {
            flag = true;
          }
        }     
        // otherwise add to queue/found
        if (flag === false) {
          queue.push(current.edges[i].destination);
          found.push(current.edges[i].destination);
        }
        flag = false;   
      }
      queue.shift();
    }

    for(let i = 0; i<found.length; i++) {
      this.memo.push(found[i]);
    }

    return found;
  }
}
