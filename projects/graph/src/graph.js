/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME

  constructor(destination){
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor(value='default', pos = {x: -1, y: -1}, size = Number, fillColor='white') {
    this.edges = [];
    this.value = value;
    this.pos = pos;
    this.size = size;
    this.fillColor = fillColor;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
    this.foundList = [];
    this.searchList = [];
  }

  debugCreateTestData(){
  console.log('called debugCreateTestData()');
  let debugVertex1 = new Vertex('t1', {x: 195, y: 290}, 40);
  let debugVertex2 = new Vertex('t2', {x: 360, y: 380}, 40)
  let debugVertex3 = new Vertex('t3', {x: 540, y: 430}, 40)
  // debugVertex1.pos.x = 50;
  // debugVertex1.pos.y = 60;
  // console.log(debugVertex1);

  let debugEdge1 = new Edge(debugVertex2);
  debugVertex1.edges.push(debugEdge1);

  let debugEdge2 = new Edge(debugVertex3);
  debugVertex2.edges.push(debugEdge2);
  

  this.vertexes.push(debugVertex1, debugVertex2, debugVertex3)
  
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

        //0. Pick a color
        //1. Take start and add it to our found list and add to the queue and
        //2. For each edge in queue[0]'s edge array, if destination is not 
        //in found list:

          // a. add to found list
            // Method 3: Use color to mark found vertexes
          // b. add to the end of the queue
          // c. add color

        //3. Dequeue' queue[0]
        //4. If queue is not empty, Go to step 2 (while loop)

        // let verts = this.vertexes;
        // start = this.vertexes[0];
        // let foundList = [];
        // console.log(verts.length);
        this.foundList.push(start);
        this.searchList.push(start);
        start.fillColor = '#111111'
        // let fCol = 'rgb(0, 0, 0)';
        // console.log(foundList);
        // let edgeLoc = verts[0].edges;
        // console.log('loc', edgeLoc);
        // let count = 0;

        while(this.searchList.length > 0){

          

          // for(let i = 0; i < verts.length; i++ ){


          //   if (edgeLoc.length === 0){
          //     return verts[i];
          //    }
             
          //   for(let j = 0; j < edgeLoc.length; j++){
          //       foundList.push(edgeLoc[j])
              
          //   }
          // }

          // ++count


          for (let edge of this.searchList[0].edges) {
            if (!this.foundList.includes(edge.destination.value)) {
              this.foundList.push(edge.destination.value);
              this.searchList.push(edge.destination);
              edge.destination.fillColor = '#000000';
            }
          }
          this.searchList.shift();
          // console.log('fuu', this.foundList);
        }
        
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // Go to the next unfound vertex in graph.vertexes and call BFS
    // Go to step 1 until we get to the end of hte array
    let found = [];
    for (let vertex of this.vertexes) {
      if (!found.includes(vertex)) {
        found = found.concat(this.bfs(vertex));
      }
      // console.log('Fuund', found);
    }

  }
}
