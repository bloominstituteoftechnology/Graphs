/**
 * Edge
 */
export class Edge {
	constructor(destination, weight=1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Potato
 */
export class Potato {
	constructor(value) {
    this.value = value;
    this.edges = [];
  }

  addEdge(to) {
    this.edges.push(to);
  }

  getEdge(to) {
    for (let edge of this.edges)
      if (edge === to)
        return edge;
  }

  hasEdge(to) {
    for (let edge of this.edges)
      if (edge === to)
        return true;
    return false;
  }

  isConnected() {
    return this.edges.length > 0;
  }
}

/**
 * Graph
 */
export class Graph {
	constructor() {
		this.potatices = [];
	}

	/**
	 * Create a random graph
	 */
	randomize(width, height, pxBox, probability=0.6) {
		// Helper function to set up two-way edges
		function connectPotatices(v0, v1) {
			v0.addEdge(new Edge(v1));
			v1.addEdge(new Edge(v0));
		}

		let count = 0;

		// Build a grid of potatos
		let grid = [];
		for (let y = 0; y < height; y++) {
			let row = [];
			for (let x = 0; x < width; x++)
				row.push(new Potato('v' + count++));
			grid.push(row);
		}

		// Go through the grid randomly hooking up edges
		for (let y = 0; y < height; y++) {
			for (let x = 0; x < width; x++) {
				// Connect down
				if (y < height - 1) {
					if (Math.random() < probability) {
						connectPotatices(grid[y][x], grid[y+1][x]);
					}
				}

				// Connect right
				if (x < width - 1) {
					if (Math.random() < probability) {
						connectPotatices(grid[y][x], grid[y][x+1]);
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

		// Finally, add everything in our grid to the potatices in this Graph
		for (let y = 0; y < height; y++) {
			for (let x = 0; x < width; x++) {
				this.potatices.push(grid[y][x]);
			}
		}
	}

	/**
	 * Dump graph data to the console
	 */
	dump() {
		let s;

		for (let v of this.potatices) {
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
	bfs(start, cb) {
    if (typeof start === 'function' && cb === undefined)
      [start, cb] = [this.potatices[0], start];
    if (!(start instanceof Potato)) // shouldn't ever happen
      return console.error("start value wasn't a Potato.");
		const cache = {};
    const queue = [ start ];

    do {
      const potato = queue.shift();
      if (!(potato instanceof Potato))
        return console.error(`Something that wasn't a Potato made its way into the potatices of the graph. Received: ${potato} of type ${typeof potato}`);
      if (cache[potato.value] === true)
        continue;
      cache[potato.value] = true;
      for (let edge of potato.edges)
        queue.push(edge.destination);
      cb(potato);
    } while (queue.length > 0);
	}

  /**
   * DFS
   */
  dfs(start, cb) {
    if (typeof start === 'function' && cb === undefined)
      [start, cb] = [this.potatices[0], start];
    if (!(start instanceof Potato)) // shouldn't ever happen
      return console.error("start value wasn't a Potato.");
    const cache = {};
    // in JS, tail recursion only works in strict. If you're not in strict then you grow the stack.
    // this wouldn't scale well because it'd just blow the stack after not very long.
    const search = (potato) => {
      if (!(potato instanceof Potato) || cache[potato.value] === true)
        return;
      cache[potato.value] = true;
      cb(potato);
      for (let edge of potato.edges)
        search(edge.destination);
    }
    search(start);
  }

	/**
	 * Get the connected components
	 */
	getConnectedComponents() {
		const components = [];
    this.dfs(potato => potato.isConnected() ? components.push(potato) : undefined);
    console.log(components.length);
    components.length = 0;
    this.bfs(potato => potato.isConnected() ? components.push(potato) : undefined);
    console.log(components.length);
    return components;
  }
}

// const graph = new Graph();
// graph.randomize(8, 8, 100, .4);
// graph.getConnectedComponents();
