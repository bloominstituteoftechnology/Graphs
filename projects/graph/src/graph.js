/**
 * Edge
 */
export class Edge {
  // !!! IMPLEMENT ME
  constructor(vertex) {
    this.destination = vertex
  }
}

/**
 * Vertex
 */
export class Vertex {
  // !!! IMPLEMENT ME
  constructor() {
    this.edges = []
    this.value = 0
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = []
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v1))
      v1.edges.push(new Edge(v0))
    }

    let count = 0

    // Build a grid of verts
    let grid = []
    for (let y = 0; y < height; y++) {
      let row = []
      for (let x = 0; x < width; x++) {
        let v = new Vertex()
        //v.value = 'v' + x + ',' + y;
        v.value = 'v' + count++
        row.push(v)
      }
      grid.push(row)
    }

    // Go through the grid randomly hooking up edges
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        // Connect down
        if (y < height - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y + 1][x])
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x + 1])
          }
        }
      }
    }

    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.8
    const boxInner = pxBox * boxBuffer
    const boxInnerOffset = (pxBox - boxInner) / 2

    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        grid[y][x].pos = {
          x: (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          y: (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
        }
      }
    }

    // Finally, add everything in our grid to the vertexes in this Graph
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        this.vertexes.push(grid[y][x])
      }
    }
  }

  /**
   * Dump graph data to the console
   */
  dump() {
    let s

    for (let v of this.vertexes) {
      if (v.pos) {
        s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):'
      } else {
        s = v.value + ':'
      }

      for (let e of v.edges) {
        s += ` ${e.destination.value}`
      }
      console.log(s)
    }
  }

  /**
   * BFS
   */
  bfs(start) {
    // !!! IMPLEMENT ME
    const queue = [start]
    const component = []
    while (queue.length > 0) {
      applyBfs(queue, component)
    }
    return component
  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    // !!! IMPLEMENT ME
    // hello from app.js
    const graphInstance = this,
      connectedComponents = []

    this.vertexes.map(resetState)
    this.vertexes.map(
      conditionallyAddVertices(connectedComponents, graphInstance)
    )
    return connectedComponents
  }
}

/**
 *
 * @param {Edge} edge
 */
const resetState = edge => {
  edge.state = 0
  return edge
}

/**
 *
 * @param {Array} toReturn empty array the will get connected
 * @param {Graph} graphInstance the graph where the vertices originate
 */
const conditionallyAddVertices = (toReturn, graphInstance) =>
  /**
   * @param {Vertex} vertex
   */
  vertex => {
    0 === vertex.state && toReturn.push(graphInstance.bfs(vertex))
  }

/**
 *
 * @param {Array} queue Represents current edges being applied
 * @param {Array} component
 */
function applyBfs(queue, component) {
  const vertex = queue.shift()
  vertex.state = 1
  component.push(vertex)
  vertex.edges.map(edge => {
    const vert = edge.destination
    if (vert.state == 0) {
      vert.state = 1
      queue.push(vert)
    }
  })
}
