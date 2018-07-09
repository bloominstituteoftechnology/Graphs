/* 
 *  Constants
 */

// const color = [
//   'yellow',
//   'green',
//   'pink',
//   'blue',
//   'gray',
//   'purple',
//   'orange',
//   'red',
// ];

const maxWeight = 200;

/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination) {
    // TODO: origin -- save a loop in the draw?
    this.destination = destination;
    this.weight = -1;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'default', pos = { x: -1, y: -1 }) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.color = 'white';
  }
  addEdge = edge => {
    this.edges.push(new Edge(edge));
  };
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    // console.log('called graph constructor');
    this.vertexes = [];
  }

  // debugCreateTestData = () => {
  //   console.log('called debugCreateTestData');
  //   let debugVertex1 = new Vertex('t1', { x: 540, y: 40 });
  //   let debugVertex2 = new Vertex('t2', { x: 100, y: 400 });
  //   let debugVertex3 = new Vertex('t3', { x: 80, y: 500 });

  //   // let debugEdge1 = new Edge(debugVertex2);
  //   debugVertex1.addEdge(debugVertex2);
  //   debugVertex2.addEdge(debugVertex3);
  //   // debugVertex3.addEdge(new Edge(debugVertex1));
  //   this.vertexes.push(debugVertex1);
  //   this.vertexes.push(debugVertex2);
  //   this.vertexes.push(debugVertex3);
  //   console.log(debugVertex1);
  // };

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

  /**
   * BFS
   */
  bfs(start) {
    // !!! IMPLEMENT ME
    // const q = [];
    // const rv = [];

    // q.push(start);
    // rv.push(start.value);

    // // console.log(start, 'start');

    // while (q.length > 0) {
    //   q[0].edges.forEach(edge => {
    //     if (!rv.includes(edge.destination.value)) {
    //       q.push(edge.destination);
    //       rv.push(edge.destination.value);
    //     }
    //   });
    //   q.shift();
    // }

    // // console.log(rv, 'rv');

    // return rv;

    let randColor =
      'rgb(' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ',' +
      Math.floor(Math.random() * 256) +
      ')';
    const queue = [];
    const found = [];

    found.push(start);
    queue.push(start);

    console.log(start, 'start');
    start.color = randColor;

    while (queue.length > 0) {
      const v = queue[0];
      for (let edge of v.edges) {
        edge.weight = Math.ceil(Math.random() * maxWeight);
        if (!found.includes(edge.destination)) {
          found.push(edge.destination);
          queue.push(edge.destination);
          edge.destination.color = randColor;
        }
      }
      queue.shift();
    }
    return found;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // const this = this;
    // console.log(typeof this, 'this');
    // const connectedComponents = [];
    // let found = [];

    // this.vertexes.forEach(vert => {
    //   let component;

    //   if (!found.includes(vert.value)) {
    //     component = this.bfs(vert);
    //     this.vertexes.forEach(v => {
    //       if (component.includes(v.value)) {
    //         v.color = color[connectedComponents.length];
    //         // console.log(v, 'v');
    //       }
    //     });
    //     connectedComponents.push(component);
    //     found = [...found, ...component];
    //   }
    // });
    // console.log(this, 'this.graph');
    // console.log(connectedComponents, 'connectedComponents');
    // return this;

    let searched = [];
    console.log(this.vertexes);
    for (let vertex of this.vertexes) {
      if (!searched.includes(vertex)) {
        console.log(vertex, 'vertex');
        searched.concat(this.bfs(vertex));
      }
    }
  }
}
