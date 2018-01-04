class Edge {
	constructor(destination, weight=1) {
		this.destination = destination;
		this.weight = weight;
	}
}

class Vertex {
	constructor(value='vertex') {
		this.value = value;
		this.edges = [];
	}
}

class Graph {
	constructor() {
		this.vertexes = [];
	}

	bfs(start) {
		const queue = [];

		for (let v of this.vertexes) {
			v.color = 'white';
			v.parent = null;
		}

		start.color = 'gray';

		queue.push(start);

		while (queue.length > 0) {
			const u = queue[0];

			for (let e of u.edges) {
				const v = e.destination;
				if (v.color === 'white') {
					v.color = 'gray';
					v.parent = u;
					queue.push(v);
				}
			}

			queue.shift(); // de-queue
			u.color = 'black';
		}
	}

	findVertex(value) {
		for (let v of this.vertexes) {
			if (v.value == value) {
				return v;
			}
		}

		return null;
	}

	route(start) {
		let p = start;
		let s = '';

		while (p != null) {
			s += p.value;

			if (p.parent !== null) {
				s += ' --> ';
			}

			p = p.parent;
		}

		console.log(s);
	}
}

/**
 * Helper function to add bidirectional edges
 */
function addEdge(v0, v1) {
	v0.edges.push(new Edge(v1));
	v1.edges.push(new Edge(v0));
}

/**
 * Main
 */

// Test for valid command line
const args = process.argv.slice(2);

if (args.length != 2) {
	console.error('usage: routing hostA hostB');
	process.exit(1);
}

// Build the entire Internet
// (it's only a model)
const graph = new Graph();
const vertA = new Vertex('HostA');
const vertB = new Vertex('HostB');
const vertC = new Vertex('HostC');
const vertD = new Vertex('HostD');
const vertE = new Vertex('HostE');
const vertF = new Vertex('HostF');
const vertG = new Vertex('HostG');
const vertH = new Vertex('HostH');

addEdge(vertA, vertB);
addEdge(vertB, vertD);
addEdge(vertA, vertC);
addEdge(vertC, vertD);
addEdge(vertC, vertF);
addEdge(vertG, vertF);
addEdge(vertE, vertF);
addEdge(vertH, vertF);
addEdge(vertH, vertE);

graph.vertexes.push(vertA);
graph.vertexes.push(vertB);
graph.vertexes.push(vertC);
graph.vertexes.push(vertD);
graph.vertexes.push(vertE);
graph.vertexes.push(vertF);
graph.vertexes.push(vertG);
graph.vertexes.push(vertH);

// Look up the hosts passed on the command line by name to see if we can
// find them.

const hostAVert = graph.findVertex(args[0]);

if (hostAVert === null) {
	console.error('routing: could not find host: ' + args[0]);
	process.exit(2);
}

const hostBVert = graph.findVertex(args[1]);

if (hostBVert === null) {
	console.error('routing: could not find host: ' + args[1]);
	process.exit(2);
}

// Route from one host to another

graph.bfs(hostBVert);
graph.route(hostAVert);
