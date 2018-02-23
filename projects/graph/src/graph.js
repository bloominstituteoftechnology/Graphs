/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(destination) {
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor() {
    this.edges = [];
    this.color = 'green';
    this.value = null;
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
  
  bfs(vertexes) {
    //holds the vertexes
    let queue = [];
    let startVert = vertexes[0];
    startVert.color = 'grey';
    queue.push(startVert);

    while(queue.length !== 0) {
      //grab the first item off queue
      for (let i = 0; i < queue[0].edges.length; i++) { 
        // if node color is green, change it to grey
        if (queue[0].edges[i].destination.color === 'green') {
          const x = queue[0].edges[i].destination.pos.x;
          const y = queue[0].edges[i].destination.pos.y;
          queue[0].edges[i].destination.color = 'grey'; 
          // add the vertexes that are neighbors to the queue and not already explored
          for (let j = 0; j < vertexes.length; j++) {
            if (vertexes[j].value === queue[0].edges[i].destination.value && 
              queue[0].edges[i].destination.color !== 'black') {
              queue.push(vertexes[j]);
            }
          } 
        }
      }
      // change node color to black and pop it off the queue when neighbors all have been reached 
      // and added to queue
      queue[0].color = 'black';
      queue.shift();
    }
  }

  /**
   * Get the connected components
   */
  getConnectedComponents(vertexes, ctx) {
    // holds connected components in each index
    let connectedComponents = [];
    for (let i = 0; i < vertexes.length; i++) {
      let component = [];
      let queue = [];
      // only start a bfs if node hasn't been explored yet 
      if (!vertexes[i].visited) {
        // randome color values
        let red = Math.floor(Math.random()* 255);
        let green = Math.floor(Math.random()* 255);
        let blue = Math.floor(Math.random()* 255);
        // begin bfs
        queue[0] = vertexes[i];
        component.push(queue[0]);
        queue[0].color = 'brown';
        while(queue.length !== 0) {
          for (let i = 0; i < queue[0].edges.length; i++) { 
            let x = queue[0].pos.x;
            let y = queue[0].pos.y;
            let x2 = queue[0].edges[i].destination.pos.x;
            let y2 = queue[0].edges[i].destination.pos.y;
            ctx.strokeStyle = `rgb(${red}, ${blue}, ${green})`;
            ctx.beginPath();
            // initial point 
            ctx.moveTo(x, y);
            // second point 
            ctx.lineTo(x2, y2);
            // draw the line itself 
            ctx.stroke(); 
            //if node hasn't been visited and add vertex directly to the queue
            if (!queue[0].edges[i].destination.visited) {
              for (let j = 0; j < vertexes.length; j++) {
                if (vertexes[j].value === queue[0].edges[i].destination.value && !queue[0].edges[i]      .destination.visited) {
                  queue.push(vertexes[j]);
                  component.push(vertexes[j]);
                  // helps prevent revisting same nodes again 
                  queue[0].edges[i].destination.visited = true;
                  queue[0].edges[i].destination.color = 'brown';     
                }
              } 
            }
          }  
          // prevent node from being visited again
          queue[0].visited = true;
          queue.shift();
        }
        // completed component added as a index to the array
        connectedComponents.push(component);
      } 
    }
    console.log(connectedComponents);
    return connectedComponents;
  }
}
