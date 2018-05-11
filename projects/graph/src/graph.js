/**
 * Edge
 */
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
  constructor(value='fred', pos = {x: 0, y: 0}) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.visited = false;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  // debugCreateTestData() {
  //   // console.log('called debugCreateTestData()');
  //   let debugVertex1 = new Vertex('debug1', {x: 100, y: 100});
  //   let debugVertex2 = new Vertex('debug2', {x: 200, y: 200});

  //   let debugEdge1 = new Edge(debugVertex2);

  //   debugVertex1.edges.push(debugEdge1);

  //   this.vertexes.push(debugVertex1, debugVertex2);
  // }

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
   * BFS - finds only all vertexes of a connected component (a set of connected vertexes)
   * BFS(graph, startVert):
      for v of graph.vertexes:
        v.color = white

      startVert.color = gray
      queue.enqueue(startVert)

      while !queue.isEmpty():
        u = queue[0]  // Peek at head of queue, but do not dequeue!

        for v of u.neighbors:
          if v.color == white:
            v.color = gray
            queue.enqueue(v)
        
        queue.dequeue()
        u.color = black
   */
  bfs(start) {
    // !!! IMPLEMENT ME

  }
  // bfs(start, flag=true) {
    // Beej's solution
    // const component = [];
    // const queue = [];
    // if (flag) {
    //   for (let vert of this.vertexes) {
    //     vert.color = 'white';
    //   }
    // }
    // start.color = 'gray';
    // queue.push(start);
    // while (queue.length > 0) {
    //   const u = queue[0];
    //   for (let e of u.edges) {
    //     const v = e.destination;
    //     if (v.color === 'white') {
    //       v.color = 'gray';
    //       queue.push(v);
    //     }
    //   }
    //   queue.shift();
    //   u.color = 'black';
    //   component.push(u);
    // }
    // return component;
  // }

    /**
   * DFS - finds only all vertexes of a connected component (a set of connected vertexes)
   *   DFS(graph):
      for v of graph.verts:
          v.color = white
          v.parent = null
            for v of graph.verts:
                if v.color == white:
                    DFS_visit(v)
      DFS_visit(v):
          v.color = gray
          for neighbor of v.adjacent_nodes:
              if neighbor.color == white:
                  neighbor.parent = v
                  DFS_visit(neighbor)
          v.color = black
   */

  dfs(start) {
    // !!! IMPLEMENT ME
    const component = [];
    const listToExplore = [start];
    start.visited = true;

    while (listToExplore.length) {
      const visitingVert = listToExplore.pop();

      visitingVert.edges.forEach(edge => {
        const visitedVert = edge.destination;
        if (!visitedVert.visited) {
          listToExplore.push(visitedVert);
        }
        component.push(visitedVert);
        visitedVert.visited = true;
      });
    }
    return component;
  }

  /**
   * Get the connected components - returns a list of sets of connected vertexes
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // Beej's Solution with his implementation of BFS
    // const connected_components = [];
    // let flag = true;
    // for (let vert of this.vertexes) {
    //   if (flag || vert.color === 'white') {
    //     const component = this.bfs(vert, flag);
    //     flag = false;
    //     connected_components.push(component);
    //   }
    // }
    // return connected_components;

    const connected_components = [];
    for (let vert of this.vertexes) {
      if (vert.visited === false) {
        const component = this.dfs(vert);
        connected_components.push(component);
      }
    }
    return connected_components;


  }

}
