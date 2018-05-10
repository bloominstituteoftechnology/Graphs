/**
 * Edge
 */

function returnNumber(min, max) {
  let number = Math.max( min, Math.floor(Math.random() * (max + 1)) );
  // console.log(number);
  return number;
}

function returnNotSelf(min, max, self) {
  let number = Math.max( min, Math.floor(Math.random() * (max + 1)) );
  // console.log(number);
  if (number !== self) return number;
  return returnNotSelf(min, max, self);
}

export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor() {
    this.edges = [];
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v1, returnNumber(0, 99)));
      v1.edges.push(new Edge(v0, returnNumber(0,99)));
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
            connectVerts(grid[y][x], grid[returnNotSelf(0, height-1, y)][returnNotSelf(0, width-1, x)]);
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[returnNotSelf(0, height-1, y)][returnNotSelf(0, width-1, x)]);
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
          // 'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          'x': returnNumber(30, 770) | 0,
          // 'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          'y': returnNumber(30, 770) | 0,
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
    const queue = [start];
    const result = [];
    // let counter = 0;

    // console.log("here is the queue member that is about to break everything:", queue[0].edges);

    while (queue.length > 0) { //while the queue still has something in it
      if (queue[0].edges.length === 0) { // if there are no edges
        result.push(queue[0]); // add it to the results array, so we know it's part of this iteration's group        
      }

      for (let i = 0; i < queue[0].edges.length; i++) { // loop through the queue's first vertex's edges
        if (queue[0].edges[i].destination.found === undefined) { //if the edge is not yet found
          queue[0].edges[i].destination.found = true; // mark it as found
          queue.push(queue[0].edges[i].destination); // add it to the queue, so we can cycle through its edges
          result.push(queue[0].edges[i].destination); // add it to the results array, so we know it's part of this iteration's group
        }
      }
      queue.shift(); // remove the item from the queue;
      // counter++;
    }

    return result; //return the array containing all vertices in the group;
  }

  dfs(start) {

    const stack = [start];
    const result = [];
    // let currentEdge = stack[0];

    whileLabel: while (stack.length > 0) {
      if (stack[0].edges.length === 0) {
        result.push(stack[0]);
      }

      for (let i = 0; i < stack[0].edges.length; i++) {
        if (stack[0].edges[i].destination.found === undefined) {
          stack[0].edges[i].destination.found = true;
          result.push(stack[0].edges[i].destination);
          stack.unshift(stack[0].edges[i].destination);
          continue whileLabel;
        }
      }
      stack.shift();
    }

    return result;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents(list) {
    // !!! IMPLEMENT ME
    const groups = [];

    // console.log("we were given this list", list);
    list.forEach((vertex) => {
      if (vertex.found === undefined) {
        // groups.push(this.bfs(vertex));
        groups.push(this.dfs(vertex));
      }
    });

    // console.log(groups);
    return groups;
  }
}
