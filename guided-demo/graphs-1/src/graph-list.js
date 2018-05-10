class Edge {
	constructor(destination) {
		this.destination = destination;
	}
}

class Vertex {
	constructor(value) {
		this.value = value;
		this.edges = [];
	}
}

class Graph {
	constructor() {
		this.vertexes = [];
	}
}