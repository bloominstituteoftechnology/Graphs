/**
 * Edge
 */
export class Edge {
	constructor(vertex, weight = 1) {
		this.destination = vertex;
		this.weight = weight
	}
}

/**
 * Vertex
 */
export class Vertex {
	constructor(edges = []) {
		this.edges = edges
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
			const weight = Math.floor(Math.random() * 11)
			v0.edges.push(new Edge(v1, weight));
			v1.edges.push(new Edge(v0, weight));
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
		let queue = []
		start.color = 'gray'
  
		queue.push(start)
  
		while (queue.length > 0) {
			let u = queue[0]
			if (!u.edges) {
				return
			}
			for (let v = 0; v < u.edges.length; v++) {
				if (u.edges[v].destination.color === 'white') {
				u.edges[v].destination.color = 'gray'
				queue.push(u.edges[v].destination)
				}
			}
			queue.shift()
			u.color = 'black'
		  
		}
		return 
	}

	dfs(start) {
		let stack = []
		start.color = 'gray'
  
		stack.push(start)
  
		
		  for (let v = 0; v < start.edges.length; v++) {
			if (start.edges[v].destination.color === 'white') {
			  start.edges[v].destination.parent = start
			  this.dfs(start.edges[v].destination)
			}
		  }
		  start.color = 'black'
		  
		return 
	}

	/**
	 * Get the connected components
	 */
	getConnectedComponents() {
		let connectedGraph = []
		let usedVerts = []
		for (let v = 0; v < this.vertexes.length; v++) {
				this.vertexes[v].color = 'white'
		}
		for (let b = 0; b < this.vertexes.length; b++) {
			let used = false;
			for (let v = 0; v < usedVerts.length; v++) {
				if (this.vertexes[b] === usedVerts[v]) {
					used = true;
				}
			}
			if (used) {
				continue
			}
			for (let v = 0; v < this.vertexes.length; v++) {
				this.vertexes[v].color = 'white'
			}
			this.dfs(this.vertexes[b]);
			let arr = []
			for (let c = 0; c < this.vertexes.length; c++) {
				if (this.vertexes[c].color === 'black') {
					arr.push(this.vertexes[c])
					usedVerts.push(this.vertexes[c])
				}
			}
			connectedGraph.push(arr)
		}
		return connectedGraph
	}
}
