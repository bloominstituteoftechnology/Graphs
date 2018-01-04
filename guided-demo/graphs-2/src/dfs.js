/**
 * Edge class
 */
class Edge {
	constructor(destination, weight=1) {
		this.destination = destination;
		this.weight = weight;
	}
}

/**
 * Vertex class
 */
class Vertex {
	constructor(value='vertex') {
		this.value = value;
		this.edges = [];
	}
}

/**
 * Graph class
 */
class Graph {
	constructor() {
		this.vertexes = [];
	}

	dfs(start) {
		function visit(v) {
			v.color = gray;

			for (e of v.edges) {
				const neighbor = e.destination;
				if (neighbor.color === 'white') {
					neighbor.parent = v;
					visit(neighbor);
				}
			}

			v.color = 'black';
		}

		for (v of this.vertexes) {
			v.color = 'white';
			v.parent = null;
		}

		for (v of this.vertexes) {
			if (v.color === 'white') {
				visit(v);
			}
		}
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

// Build graph
const graph = new Graph();
const vertA = new Vertex('A');
const vertB = new Vertex('B');
const vertC = new Vertex('C');
const vertD = new Vertex('D');
const vertE = new Vertex('E');
const vertF = new Vertex('F');
const vertG = new Vertex('G');
const vertH = new Vertex('H');

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
