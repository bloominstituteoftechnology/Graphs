const Queue = require('./storage/queue');
const maxColor = 0x90;
const colors = { black: ["black", "white"], white: ["white", "black"], grey: ["gray", "green"] }
const timeout = 500;
/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(vertex, isVisible) {
    this.destination = vertex;
    this.weight = Math.floor(Math.random() * 10) + 1;
    this.color = isVisible ? this.randomColor() : "illlegal color";
    this.isVisible = isVisible;
  }
  // randomColorx = () => {
  //   let color, hex;
  //   do {
  //     color = Math.round(Math.random() * 0xFFFFFF);
  //     for (let i = 0; i < 3; i++) {
  //       hex = (color & (0xff << (4 - i * 2))) >> (4 - i * 2);
  //       if (hex <= maxColor) break;
  //     }
  //   } while (hex > maxColor);
  //   return color;
  // }
  randomColor = () => {
    const smallColor = Math.floor(Math.random() * 3);
    const colors = [];
    for (let i = 0;i< 3;i++) 
      colors[i] = Math.round(Math.random() * ((i === smallColor) ? maxColor : 0xff));
    return `rgb(${colors[0]}, ${colors[1]}, ${colors[2]})`
  }

}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor() {
    this.edges = [];
    this.value = null;
    this.pos = null; // {x: 0, y: 0}
    this.color = colors.white;
  }
  get isBlack() {
    return this.color === colors.black;
  }  
}

const max_edges = 1000;
// const max_nodes = 20
export let edges = 0;
// let nodes = 0;


/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.q = new Queue();
    this.cv  = null;
    this.update = null;
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    // console.log("running randomize");

    function connectVerts(v0, v1) {
      if (edges > max_edges) return;
      edges += 2;
      v0.edges.push(new Edge(v1, true));
      v1.edges.push(new Edge(v0, false));
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
    // console.log(`randomize edges: ${edges}`);
  }
  dumpVertex(v) {
    let s;
    if (v.pos) {
      s = v.value + ' (' + v.pos.x + ',' + v.pos.y + ',  back ' + v.color[0] + ',  for ' + v.color[1] + '):';
    } else {
      s = v.value + ':';
    }

    for (let e of v.edges) {
      s += ` ${e.destination.value}`;
    }
    console.log(s);
  }
  /**
   * Dump graph data to the console
   */
  dump() {
    for (let v of this.vertexes) {
      this.dumpVertex(v);
    }
  }
  // bfsIterate(q, cv) {
  //   const childQ = new Queue();
  //   while (!q.isEmpty) {
  //     while (!q.isEmpty) {
  //       const parent = q.dequeue();
  //       parent.edges.forEach(edge => {
  //         childQ.enqueue(edge.destination);
  //         cv(edge.destination);
  //       });
  //     }
  //     console.log(`childQ.length: ${childQ.size} childQ[0]: ${childQ.size ? childQ.top.value : -1}  `)
  //     q = new Queue(childQ.copy);
  //     childQ.clear();
  //   }
  //   return null;
  // }
  bfsIterate(q, cv) {
    while (!q.isEmpty) {
      const parent = q.dequeue();
      parent.color = colors.black;
      parent.edges.forEach(edge => {
        if (edge.destination.color === colors.white) {
          edge.destination.color = colors.grey;
          q.enqueue(edge.destination);
          cv(edge.destination);
        }
      });
    }
  }
  bfsStep() {
    if (!this.q.isEmpty) {
      const parent = this.q.dequeue();
      parent.color = colors.black;
      parent.edges.forEach(edge => {
        if (edge.destination.color === colors.white) {
          edge.destination.color = colors.grey;
          this.q.enqueue(edge.destination);
          this.cv(edge.destination);
        }
      });
      this.update();
      return true;
    } else return false;
  }
  /**
   * BFS
   */
  bfs(start, update) {
    this.update = update;
    const q = this.q.clear();
    this.cv = (v) => {}; //this.dumpVertex;
    this.vertexes.forEach(v => v.color = colors.white);
    start.color = colors.grey;
    q.enqueue(start);
    this.cv(start);
    // console.log(`number of edges ${start.edges.length}`);
    // nodes = 1;
    //this.bfsIterate(q, this.dumpVertex);
    // while(this.bfsStep());h
    let handle = setInterval(() => {

      if (!this.bfsStep()) {
        this.update();
        // console.log('done');
        this.dump();
        clearInterval(handle);
      }
    },timeout);
    // console.log('exitig bfs');
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
  }
}
// const g = new Graph();
// g.randomize(5, 4, 150, 0.6);
// for (let i = 0;i<g.v)
// g.bfs(g.vertexes[0]);
