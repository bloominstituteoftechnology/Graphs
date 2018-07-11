/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination, weight) {
    this.destination = destination;
    this.weight = weight;
  }

}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value = 'default', pos = { x: -1, y: -1 }, color = 'white') {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.color = color;
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
    // function getRandomColor() {
    //   var letters = '0123456789ABCDEF';
    //   var color = '#';
    //   for (var i = 0; i < 6; i++) {
    //     color += letters[Math.floor(Math.random() * 16)];
    //   }
    //   return color;
    // }
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
    // create a visited array
    // var visited = [];
    // for (var i = 0; i < this.vertexes.length; i++)
    //   visited[i] = 'white';

    // // Create an object for queue
    // var q = new Graph();

    // // add the starting node to the queue
    // visited[start] = true;
    // q.enqueue(start);

    // // loop until queue is element
    // while (!q.isEmpty()) {
    //   // get the element from the queue
    //   var getQueueElement = q.dequeue();

    //   // passing the current vertex to callback funtion
    //   console.log('getQueueElement called',getQueueElement);

    //   // get the adjacent list for current vertex
    //   var get_List = this.AdjList.get(getQueueElement);

    //   // loop through the list and add the elemnet to the
    //   // queue if it is not processed yet
    //   for (var i in get_List) {
    //     var neigh = get_List[i];

    //     if (!visited[neigh]) {
    //       visited[neigh] = true;
    //       q.enqueue(neigh);
    //     }
    //   }
    // }


    const component = [];
    const queue = [];

    start.color = 'gray';
    queue.push(start);

    while (queue.length > 0) {
      const u = queue[0];

      for (let e of u.edges) {
        const v = e.destination;
        if (v.color === 'white') {
          v.color = 'gray';
          queue.push(v);
        }
      }

      queue.shift(); // de-queue
      u.color = 'black';
      component.push(u);
    }

    return component;
    //<<<<< >>>>>>> <<<<<<  >>>>>>>>
    // for (let v of this.graph.vertexes) {

    //   v.color = white
    // }

    // start.color = 'gray'
    // queue.enqueue(start)

    // while (!queue.isEmpty()) {
    //   u = queue[0]  // Peek at head of queue, but do not dequeue!

    //   for (let v of u.neighbors) {

    //     if (v.color == 'white') {

    //       v.color = gray
    //       queue.enqueue(v)
    //     } else {

    //       queue.dequeue()
    //       u.color = 'black'
    //     }

    //   }
    // }

  }
  // dfs(start) {
  //   function visit(v) {
  //     v.color = gray;

  //     for (e of v.edges) {
  //       const neighbor = e.destination;
  //       if (neighbor.color === 'white') {
  //         neighbor.parent = v;
  //         visit(neighbor);
  //       }
  //     }

  //     v.color = 'black';
  //   }

  //   for (v of this.vertexes) {
  //     v.color = 'white';
  //     v.parent = null;
  //   }

  //   for (v of this.vertexes) {
  //     if (v.color === 'white') {
  //       visit(v);
  //     }
  //   }
  // }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // const component = this.bfs(this.vertex);
    // !!! IMPLEMENT ME
    const componentsList = [];
    for (let v of this.vertexes) {
      v.color = 'white'; 
    }
    for (let v of this.vertexes) {
      if (v.color === 'white') {
        const component = this.bfs(v);
        componentsList.push(component);
      }
    }
    return componentsList;
  }
}
