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
  constructor(value = "default", pos = { x: -1, y: -1 }) {
    this.edges = [];
    this.value = value;
    this.pos = pos;
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
    console.log("called debugging");
    let debugVertex1 = new Vertex("t1", { x: 20, y: 40 });
    let debugVertex2 = new Vertex("t2", { x: 60, y: 60 });
    let debugVertex3 = new Vertex("t3", { x: 100, y: 100 });

    debugVertex1.edges.push(new Edge(debugVertex2));
    debugVertex1.edges.push(new Edge(debugVertex3));

    this.vertexes.push(debugVertex1);
    this.vertexes.push(debugVertex2);
    this.vertexes.push(debugVertex3);
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      let randomNum = Math.ceil(Math.random() * 10);
      v0.edges.push(new Edge(v1, randomNum));
      v1.edges.push(new Edge(v0, randomNum));
    }

    let count = 0;

    // Build a grid of verts
    let grid = [];
    for (let y = 0; y < height; y++) {
      let row = [];
      for (let x = 0; x < width; x++) {
        let v = new Vertex();
        //v.value = 'v' + x + ',' + y;
        v.value = "v" + count++;
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
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
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
    // !!! IMPLEMENT ME
    // 0. Pick a random color
    // 1. Take start and add it to our found list and to the queue
    //2.
    var CSS_COLOR_NAMES = [
      "AliceBlue",
      "Aqua",
      "Aquamarine",
      "Bisque",
      "Blue",
      "BlueViolet",
      "Brown",
      "CadetBlue",
      "Chartreuse",
      "Chocolate",
      "Coral",
      "CornflowerBlue",
      "Crimson",
      "Cyan",
      "DarkBlue",
      "DarkCyan",
      "DarkGoldenRod",
      "DarkGrey",
      "DarkGreen",
      "DarkMagenta",
      "DarkOliveGreen",
      "Darkorange",
      "DarkOrchid",
      "DarkRed",
      "DarkSalmon",
      "DarkSeaGreen",
      "DarkSlateBlue",
      "DarkSlateGrey",
      "DarkTurquoise",
      "DarkViolet",
      "DeepPink",
      "DeepSkyBlue",
      "DimGrey",
      "DodgerBlue",
      "FireBrick",
      "ForestGreen",
      "Fuchsia",
      "Gold",
      "GoldenRod",
      "Green",
      "GreenYellow",
      "HotPink",
      "IndianRed",
      "Indigo",
      "Khaki",
      "Lavender",
      "LavenderBlush",
      "LawnGreen",
      "LightBlue",
      "LightCoral",
      "LightCyan",
      "LightGreen",
      "LightPink",
      "LightSalmon",
      "LightSeaGreen",
      "LightSkyBlue",
      "LightSteelBlue",
      "Lime",
      "LimeGreen",
      "Magenta",
      "Maroon",
      "MediumAquaMarine",
      "MediumBlue",
      "MediumOrchid",
      "MediumPurple",
      "MediumSeaGreen",
      "MediumSlateBlue",
      "MediumSpringGreen",
      "MediumTurquoise",
      "MediumVioletRed",
      "MidnightBlue",
      "MistyRose",
      "Navy",
      "Olive",
      "OliveDrab",
      "Orange",
      "OrangeRed",
      "Orchid",
      "PaleGoldenRod",
      "PaleGreen",
      "PaleTurquoise",
      "PaleVioletRed",
      "PeachPuff",
      "Pink",
      "Plum",
      "PowderBlue",
      "Purple",
      "Red",
      "RosyBrown",
      "RoyalBlue",
      "Salmon",
      "SandyBrown",
      "SeaGreen",
      "SkyBlue",
      "SlateBlue",
      "SpringGreen",
      "SteelBlue",
      "Teal",
      "Thistle",
      "Tomato",
      "Turquoise",
      "Violet",
      "Yellow",
      "YellowGreen"
    ];
    let color =
      CSS_COLOR_NAMES[Math.floor(Math.random() * CSS_COLOR_NAMES.length)];
    let found = [start];
    let queue = [start];
    console.log("Color: ", color);
    queue[0].color = color;
    while (queue.length > 0) {
      for (let i = 0; i < queue[0].edges.length; i++) {
        queue[0].color = color;
        if (!found.includes(queue[0].edges[i].destination)) {
          found.push(queue[0].edges[i].destination);
          queue.push(queue[0].edges[i].destination);
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
    let searched = [];
    for (let vertex of this.vertexes) {
      if (!searched.includes(vertex)) {
        searched = searched.concat(this.bfs(vertex));
      }
      console.log("Searched: ", searched);
    }
  }

  highlightShortestPath(start, end) {
    console.log("Calling highlight shortest path.");
  }
}
