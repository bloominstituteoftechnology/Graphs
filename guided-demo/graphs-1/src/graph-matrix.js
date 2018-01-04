class Vertex {
	constructor(value) {
		this.value = value;
	}
}

class Graph {
	constructor(rows, cols) {
		this.matrix = new Array(rows);

		for (let i in rows) {
			this.matrix[i] = new Array(cols).fill(0);
		}
	}

	connectVertex(a, b) {
		this.matrix[a][b] = 1;
	}
}