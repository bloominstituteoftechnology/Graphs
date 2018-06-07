/**
 * Edge
 */
export class Edge {
  // TODO: Could be a way to save a loop in the draw by adding origin
  constructor(origin, destination) {
    this.origin = origin.pos;
    this.destination = destination.pos;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'default', pos = {x: -1, y: -1}) {
    this.edges = [];
    this.value = value;
    this.pos = pos; 
    this.distance = null;
    this.predecessor = null;
    this.visited = false;
    this.color = 'rgb(0, 206, 209)';
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.components = 0;
  }

  debugCreateTestData() {
    console.log('called test function');
    let debugVertex1 = new Vertex('t1', {x: 40, y: 40});
    let debugVertex2 = new Vertex('t2', {x: 80, y: 80});
    let debugVertex3 = new Vertex('t3', {x: 40, y: 80});
    
    let debugEdge1 = new Edge(debugVertex1, debugVertex2);
    debugVertex1.edges.push(debugEdge1);

    let debugEdge2 = new Edge(debugVertex1, debugVertex3);
    debugVertex1.edges.push(debugEdge2);

    this.vertexes.push(debugVertex1, debugVertex2, debugVertex3);
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability=0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v0, v1));
      v1.edges.push(new Edge(v1, v0));
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


    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.8;
    const boxInner = pxBox * boxBuffer;
    const boxInnerOffset = (pxBox - boxInner) / 2 + 5;

    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        grid[y][x].pos = {
          'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
        };
      }
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
    let queue = [];
    let visited = [];
    let level = 1;
    let currentNode = null;

    // initialize source/start
    start.distance = 0;
    start.visited = true;
    queue.push(start);
    visited.push(start);
    

    // begin search
    while (queue.length > 0) {
      currentNode = queue.pop();

      // if node is isolated, we're done
      if (currentNode.edges.length === 0) {
        break;
      }

      for (let i = 0; i < currentNode.edges.length; i++) {
        let connectedNode = null;
        let edge = currentNode.edges[i];

        for (let k = 0; k < this.vertexes.length; k++) {
          if (this.vertexes[k].visited === false) {
            if (this.vertexes[k].pos.x === edge.destination.x && this.vertexes[k].pos.y === edge.destination.y) {
              connectedNode = this.vertexes[k];
              console.log("BFS connectedNode: ", connectedNode);
            }
          }
        }
        
        // if node is null, we've been here before 
        if (!connectedNode) {
          continue;
        }
        
        connectedNode.distance = level;
        connectedNode.predecessor = currentNode;
        connectedNode.visited = true;
        visited.push(connectedNode);
        
        if (connectedNode.edges.length > 0) {
          queue.push(connectedNode);
        }
      }
      level++;
      console.log("BFS Visited: ", visited);  
      }
      
      return visited;
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    
    let connectedComponents = [];
    let unvisited = this.vertexes;
    let visited = [];
    let colors = [];

    // color generator
    let randomBlueColorString = () => {
      let blue = Math.floor((Math.random() * 240) + 130);
      let green = blue - 30;
      let red = green - 40;

      return "rgb(" + red.toString() + ", " + green.toString() + ", " + blue.toString() + ")";
    };
    
    while (visited.length < this.vertexes.length) {
      connectedComponents.push(this.bfs(unvisited[0]));
      unvisited = this.vertexes.filter(vertex => vertex.visited === false);
      console.log("Unvisited: ", unvisited);
      visited = connectedComponents.reduce((acc, val) => acc.concat(val), []);
    }

    console.log("Connected Components: ", connectedComponents);
    console.log("Component Count: ", connectedComponents.length);
    
    this.components = connectedComponents.length;

    // colorize components
    for (let i = 0; i < connectedComponents.length; i++) {
      
      let newBlue = randomBlueColorString();
      
      while (colors.includes(newBlue)) {
        newBlue = randomBlueColorString();
      }

      colors.push(randomBlueColorString());
      
      for (let k = 0; k < connectedComponents[i].length; k++) {
        connectedComponents[i][k].color = colors[i];
      }
    }
  }
}
