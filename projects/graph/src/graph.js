/**
 * Edge
 */
// export class Edge {
class Edge {
	constructor(destination, weight=1) {
		this.destination = destination;
		this.weight = weight;
	}


}

/**
 * Vertex
 */
// export class Vertex {
class Vertex {
	constructor(value) {
		this.value = value;
		this.edges = [];
	}
}

/**
 * Graph
 */
// export class Graph {
class Graph {
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
	bfs(start) {
		// set all vertieces to white
		for (let v of this.vertexes) {
			v.color = 'white';
		}

		// set start vertex color to gray
		start.color = 'gray';
		start.parent = null;
		// instantiate the queue with the start vertex
		let comp = [];
		let q = [start];
		// let visited = [start.value]

		while (q.length > 0) {
			let peekVertex = q[0];

			// console.log(`peeking at ${peekVertex.value}`);

			peekVertex.edges.forEach(edge => {
				const v = edge.destination;
				if (v.color === 'white') {
					v.parent = peekVertex;
					v.color = 'gray';
					q.push(v);
				}
				// console.log(edge.destination);
				// if (!(visited.filter(v => v === edge.destination.value).length > 0)) {
				// 	// console.log(edge.destination.value);
				// 	visited.push(edge.destination.value)
				// 	q.push(edge.destination);
				// }
				// q.push(edge.destination);
			})

			q.shift();
			peekVertex.color = 'black';
			// console.log(peekVertex);
			comp.push(peekVertex);
		}
		return comp;
	}

	/**
	 * Get the connected components
	 */
	getConnectedComponents() {
		// keep calling bfs with different starting points until there is no more vertexes left
		let unusedVertexes = this.vertexes;
		let components = [];
		// console.log(unusedVertexes)

		while(unusedVertexes.length > 0) {
			let randomVertex = unusedVertexes[Math.floor(Math.random() * unusedVertexes.length)];
			// console.log(randomVertex);
			const component = this.bfs(randomVertex);
			// console.log(component);
			components.push(component);
			// remove get difference of unusedVertexs and the vertexes in component just found.
			component.forEach(v => {
				// console.log(v)
				if (unusedVertexes.filter(v1 => v1.value === v.value).length > 0) {
					// remove object
					const removeIndex = unusedVertexes.map((i) => { return i.value; }).indexOf(v.value);
					unusedVertexes.splice(removeIndex, 1);
				}
			})
		}
		// console.log(components);
		return components;
	}
}

// let g = new Graph();

// g.randomize(3, 3, 2);
// g.randomize();
// g.dump();
// g.getConnectedComponents().forEach(comp => console.log(comp));
// g.bfs(g.vertexes[0]);
// g.vertexes.forEach(v => {
// 	console.log(`vertex ${v}`)
// 	v.edges.forEach(e => console.log(e.destination))
// });

module.exports = {Edge, Vertex, Graph}