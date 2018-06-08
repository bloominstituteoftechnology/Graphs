/**
 * Edge
 */
export class Edge {
  constructor(destination) {
    this.destination = destination;
    // implement weight
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'default', pos = { x: -1, y: -1 }) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.color = 'white';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  debugCreateTestData() {
    // console.log('called debugCreateTestData()');
    let debugVertex1 = new Vertex('t1', { x: 40, y: 40 });
    let debugVertex2 = new Vertex('t2', { x: 80, y: 80 });
    let debugVertex3 = new Vertex('t3', { x: 40, y: 80 });
    // debugVertex1.pos.x = 50;
    // debugVertex1.pos.y = 60;

    let debugEdge1 = new Edge(debugVertex2); // 1 to 2
    let debugEdge2 = new Edge(debugVertex3); // 2 to 3

    this.vertexes.push(debugVertex1, debugVertex2, debugVertex3);

    debugVertex1.edges.push(debugEdge1);
    debugVertex2.edges.push(debugEdge2);
  }

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
        grid[y][x].pos = {
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

  randomRGBArr() {
    return [
      Math.floor(Math.random() * 256),
      Math.floor(Math.random() * 256),
      Math.floor(Math.random() * 256),
    ];
  }

  /**
   * BFS
   */
  bfs(start, rgbColor) {
    // !!! IMPLEMENT ME
    // 0. Pick a random color
    let randColor =
      'rgb(' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ')';

    // 1. a. Take start and add it to our found list
    let found = [];
    found.push(start);
    // Method One - Keep a list of what we've found
    //    Advantages - Easy to query, list per CC
    //    Disadvantages - Takes time and space, must be passed around,
    //    must be iterated through to find specific item, more complexity O(n)

    // Method Two - Use flag on vertex to mark as found
    //    Advantages - Easy to implement, no list management, easier access, time complexity O(1)
    //    Disadvantages - no list if list is needed, fragmented data, additional logic needed to add color/assign cc

    // Method Three - Use color as the flag
    // Shares most advantages and disadvantages with Method Two
    // Advantages - Avoid redundancy and need for tracking a second property
    // Disadvantages - Not explicit, data meaning becomes obscured

    // 1. b. And add to the queue
    let queue = [];
    queue.push(start);

    // 1. c. And add color
    start.color = rgbColor;

    // 4. If queue is not empty, go to step 2 (while loop)
    while (queue.length > 0) {
      // 2. For each edge in queue[0]'s edge array,
      const vertex = queue[0];
      for (let edge of vertex.edges) {
        // if destination is not in found
        if (!found.includes(edge.destination)) {
          //    a. add to found list
          found.push(edge.destination);
          //    b. add to the end of the queue
          queue.push(edge.destination);
          //    c. add color property
          edge.destination.color = rgbColor;
        }
      }
      // 3. Dequeue queue[0]
      queue.shift();
    }
    return found;
  } // end bfs

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // 0. Set color for connected components
    const rgbArr = this.randomRGBArr();
    // 1. Go to next unfound vertex in graph.vertexes and call bfs on it
    // 2. Go to step 1 until we get to the end of the array
    let connected = [];
    // let i = 0;
    // let j = 0;
    // let k = 0;
    let flag = true;
    for (let vertex of this.vertexes) {
      let color = 'rgb(' + rgbArr[0] + ',' + rgbArr[1] + ',' + rgbArr[2] + ')';
      if (!connected.includes(this.vertex)) {
        console.log('color: ', color);
        connected = connected.concat(this.bfs(vertex, color));
      }
      console.log('flag: ', flag);
      if (flag) {
        // if incrementing only
        if (rgbArr[0] - 20 >= 0) {
          rgbArr[0] -= 20;
        } else {
          rgbArr[0] += 17;
          flag = false;
        }
        if (rgbArr[1] - 20 >= 0) {
          rgbArr[1] -= 20;
        } else {
          rgbArr[1] += 17;
          flag = false;
        }
        if (rgbArr[2] - 20 >= 0) {
          rgbArr[2] -= 20;
        } else {
          rgbArr[2] += 17;
          flag = false;
        }
      }

      if (!flag) {
        if (rgbArr[0] + 17 <= 255) {
          rgbArr[0] += 17;
        } else {
          rgbArr[0] -= 20;
          flag = true;
        }
        if (rgbArr[1] + 17 <= 255) {
          rgbArr[1] += 17;
        } else {
          rgbArr[1] -= 20;
          flag = true;
        }
        if (rgbArr[2] + 17 <= 255) {
          rgbArr[2] += 17;
        } else {
          rgbArr[2] -= 20;
          flag = true;
        }
      }

      // if (rgbArr[1] - 15 >= 0) {
      //   rgbArr[1] -= 15;
      // } else {
      //   rgbArr[1] += 10;
      // }
      // if (rgbArr[2] - 15 >= 0) {
      //   rgbArr[2] -= 15;
      // } else {
      //   rgbArr[2] += 10;
      // }
    }
  } // end getConnectedComponents
} // end Graph class
