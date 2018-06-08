/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination) {
    // To Do: By adding origin here can we save a loop in the draw???
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'default', pos = { x: -1, y: -1 }) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.color = 'white'; // For alternate bfs solution
  }
  //To Do: Figure out how to add edges
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    console.log('called graph constructor');
    this.vertexes = [];
  }

  // Test Data
  debugCreateTestData() {
    console.log('called debugCreateTestData()');
    let debugVertex1 = new Vertex('t1', { x: 40, y: 40 });
    let debugVertex2 = new Vertex('t2', { x: 180, y: 80 });
    let debugVertex3 = new Vertex('t3', { x: 75, y: 150 });

    let debugEdge1 = new Edge(debugVertex2); // 1 to 2
    debugVertex1.edges.push(debugEdge1);

    let debugEdge2 = new Edge(debugVertex3); // 2 to 3
    debugVertex2.edges.push(debugEdge2);

    this.vertexes.push(debugVertex1, debugVertex2, debugVertex3);
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
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
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
    // add <reset = true> as additional parameter for original solution
    // Alternate solution
    // 0. Pick random color
    const getRandomColor = () => {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    };

    // 1a. Take start and add it to our found list
    let queue = [];
    let found = [];
    found.push(start); // found = [v1]

    // 1b. add to the queue
    queue.push(start); // queue = [v1]

    // 1c. add color;
    start.color = getRandomColor();

    // 4. If queue is not empty, go to step 2 (while loop)
    while (queue.length > 0) {
      // 2. For each eadge in the queue[0]'s edge array,
      const v = queue[0]; // v1
      for (let edge of v.edges) {
        // v.edges = [v2, v7]
        // if destination is not in the found list
        if (!found.includes(edge.destination)) {
          // a. add to found list
          found.push(edge.destination); // found = [v1, v2, v7]
          // b. add to the end of the queue
          queue.push(edge.destination); // queue = [v1, v2, v7]
          // c. add color property
          edge.destination.color = v.color; // v2 color, v7 color
        }
      }
      // 3. Dequeue queue[0]
      queue.shift(); // queue = [v2, v7]
      console.log(Object.values(queue));
    }
    return found;

    // Original Solution

    // const queue = [];
    // const component = [];
    // let vertex;
    // let edge;

    // // !!! IMPLEMENT ME

    // if (reset) {
    //   for (vertex of this.vertexes) {
    //     vertex.color = 'white';
    //   }
    // }

    // start.color = 'gray';

    // queue.push(start);

    // while (queue > 0) {
    //   const unexplored = queue[0];

    //   for (edge of unexplored.edges) {
    //     if (edge.destination.color === 'white') {
    //       edge.destination.color === 'gray';
    //       queue.push(vertex);
    //     }
    //   }
    //   queue.shift();

    //   unexplored.color = 'black';

    //   component.push(unexplored);
    // }

    // return component;
  }

  dfs(start) {
    const getRandomColor = () => {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    };

    let stack = [];
    let found = [];

    found.push(start);
    stack.push(start);

    start.color = getRandomColor();

    while (stack.length > 0) {
      let v = stack.pop();
      if (!found.includes(v)) {
        found.push(v);
      }
      for (let edge of v.edges) {
        if (!found.includes(edge.destination)) {
          edge.destination.color = v.color;
          stack.push(edge.destination);
        }
      }
      console.log(Object.values(stack));
    }
    return found;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME

    // Alternate Solution
    let searched = [];

    for (let vertex of this.vertexes) {
      if (!searched.includes(vertex)) {
        searched = searched.concat(this.dfs(vertex));
      }
    }
    return searched;

    // Original Solution

    // const connectedComponents = [];
    // let vertex;

    // let reset = true;

    // for (vertex in this.vertexes) {
    //   if (reset || vertex.color === 'white') {
    //     const component = this.bfs(vertex, reset);
    //     reset = false;

    //     connectedComponents.push(component);
    //   }
    // }
    // return connectedComponents;
  }
}
