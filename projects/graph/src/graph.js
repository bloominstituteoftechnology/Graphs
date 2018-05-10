/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1){
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = "default", pos = {x: -1, y: -1}){
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.fillColor = "white";
    this.visited =  false;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  createTestData(){
    let vert1 = new Vertex("v1", {x: 100, y: 100});
    let vert2 = new Vertex("v2", {x: 200, y: 200});

    let edge1 = new Edge(vert2);
    vert1.edges.push(edge1);

    this.vertexes.push(vert1, vert2);
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
    //# my implementation
    //* creates a queue to handle the vertexes in a FIFO order
    const queue = []
    //* sets the starting node to visited and changes the color accordingly
    start.visited = true;
    start.fillColor = "lightblue";
    //* pushes the starting vertex to the queue as the first value
    queue.push(start);
    
    //* while the queue has a value, you store/shift it then change its destination status and color.
    while (queue.length){
      const vert = queue.shift();
      
      //* if the edge has a destionation value that hasn't been vistied, push it to the back of the queue
      for (let edge in vert){
        if (!edge.destination.visited){
          edge.destination.fillColor = "lightblue";
          edge.destination.visited = true;
          queue.push(edge.destination);
        }
      }
    }
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    for (let vert of this.vertexes){
      if (!vert.visited){
        this.bfs(vert)
      }
    }
  }
}