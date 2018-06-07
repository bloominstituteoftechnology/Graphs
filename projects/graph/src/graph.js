/**
 * Edge
 */
export class Edge {
  //by adding origin, try to save a loop in the draw
  // !!! IMPLEMENT ME
  constructor(destination) {
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'default', pos = {x: -1, y: -1}) { // (x,y -1) stands out more to test if rendered correctly
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.color = 'white';
  }
  //TODO: Figure out how to add edges
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    // console.log('called graph constructor');
    this.vertexes = [];
  }

  debugCreateTestData() {
    console.log('called debugCreateTestData()');
    let debugVertex1 = new Vertex('T1', {x: 40, y: 40});
    let debugVertex2 = new Vertex('T2', {x: 80, y: 80});
    let debugVertex3 = new Vertex('T3', {x: 40, y: 80});
//  debugVertex1.pos.x = 50; another way to write it
//  debugVertex1.pos.y = 60;
    let debugEdge1 = new Edge(debugVertex2); // 1 to 2
    debugVertex1.edges.push(debugEdge1);

    let debugEdge2 = new Edge(debugVertex3);
    debugVertex2.edges.push(debugEdge2);
    
    this.vertexes.push(debugVertex1, debugVertex2, debugVertex3);
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
    // Breadth First Search(start)
    // Pick random color

    const randomColor =
    'rgb(' +
    Math.floor(Math.random() * 256) +
    ',' +
    Math.floor(Math.random() * 256) +
    ',' +
    Math.floor(Math.random() * 256) +
    ')';

    // Take start and add it to our found list
    let queue = [];
    let found = [];
    found.push(start);

    // add to the queue
    queue.push(start);

    //add color
    start.color = randomColor;

    // if queue is NOT empty, go to step 2 (while loop)
    while(queue.length > 0) {
    // for each edge in the queue[0]'s edge array, if destination is not in the found list
    const v = queue[0];
    for (let edge of v.edges) {
      if (!found.includes(edge.destination)) {
        // add to found list
      found.push(edge.destination)
      // add to the end of queue
      queue.push(edge.destination)
      // add the color property
      edge.destination.color = randomColor;
      }
      
    }
    // dequeue queue[0]
    queue.shift();
    }
    return found;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    let searched = [];
    for (let vertex of this.vertexes) {
      if (!searched.includes(vertex)) {
        searched = searched.concat(this.bfs(vertex));
      }
    }
    
  }
}
