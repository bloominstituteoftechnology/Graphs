/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  // step 1: need to know start and end
  // step 2: start is already taken care of, because the edge will belong to a vertex
  // step 3: So all we need to know is destination
  // Edge has weight, and destination
  constructor(destination, weight = 1) {
    this.weight = weight;
    this.destination = destination;
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  // vertex's have value, pos, and edges
  constructor(value = '', pos = {x: -1, y: -1}) {
    this.value = value;
    this.edges = [];
    this.pos = pos;
    this.groupID = -1;
    this.parentVertex = null;
  }
}

/**
 * Graph
 */
export class Graph {
         constructor() {
           this.vertexes = [];
         }

         debugCreateTestData() {
           //console.log("Debug: Ran debugCreateTestData()");
           let debugVert1 = new Vertex("dv1", { x: 10, y: 20 });
           let debugVert2 = new Vertex("dv2", { x: 100, y: 100 });

           // to test our edges let's make a debug edge arbitrarily
           // that connects node 1 and node 2
           // to do that, we need to create an edge that belongs to debugVert1
           // and has a destination of debugVert2, which by our definition of our
           // edge class, is all we need to say that you go from 1 to 2

           let edge1 = new Edge(debugVert2);
           debugVert2.edges.push(edge1);
           //console.log check>>>

           this.vertexes.push(debugVert1); // TODO: Can I do comma's here?
           this.vertexes.push(debugVert2);
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
               v.value = "v" + count++; // v1, v2
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
               grid[y][x].pos = { x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0, y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0 };
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
               s = v.value + " (" + v.pos.x + "," + v.pos.y + "):";
             } else {
               s = v.value + ":";
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
           const closure = [start];
           // create an array an intialized the start vertex or node
           const hash = { [`${start.value}`]: 1 };
           // creating an object witht start initialized
           // we do this because the object is the only structure that doesn't require a loop look up it's O(1) best Big O (single operation)
           // two closures are defined and initialized with the first vertex
           let loop_extract = vertex => {
             let { edges } = vertex;
             // if the key for this value hasn't been encountered before it will not be 1
             // if 
             edges.forEach(edge => {
               if (!hash[`${edge.destination.value}`]) { // base case of not having anything new -- so no looping
                 closure.push(edge.destination); // hitting both closures and adding to que
                 hash[`${edge.destination.value}`] = 1;
                 // recurse on every offspring of the parent
                 loop_extract(edge.destination);
               }
             });
           };
           // Call and return everything above is setup
           loop_extract(start); // call the function
           return closure; // returning array with nodes visited in order
         }
         /**
          * Get the connected components
          */
         getConnectedComponents() {
           // !!! IMPLEMENT ME
         }
       }
