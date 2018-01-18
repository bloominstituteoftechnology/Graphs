function Node(data) {
    this.data = data;
    this.parent = null;
    this.neighbors = [];
}

function Graph(data) {
    var node = new Node(data);
    this._root = node;
    this.vertices = [node]
}

const bfs = (graph, startVertex) => {
    // instantiate the queue with the starting vertex
    let q = [startVertex];

    // traverse the graph by while looping until the queue is empty
    // the queue decrements by dequeueing vertexes
    while (q.length > 0) {
        let peekVertex = q[0];
        console.log(`peeking at vertex: `, peekVertex.data);

        peekVertex.neighbors.forEach(vertex => {
            q.push(vertex);
        })

        q.shift();
    }
}

/*
list nodes_to_visit = {root};
while( nodes_to_visit isn't empty ) {
  currentnode = nodes_to_visit.take_first();
  nodes_to_visit.prepend( currentnode.children );
  //do something
}
*/
const dfs = (graph) => {
    // depth first search doesnt need a starting point
    // if startVertex is null, select a random starting point?

    // instantiate stack, toVisit, and visited array
    let stack = [];
    let toVist = graph;
    let visted = [];

    // push first element on stack
    stack.unshift(startVertex);
    // console.log(stack);

    // get latest node on call stack
    let curNode = stack[0];
    // console.log(curNode);
    // grab a random neighbor node of current node
    let randomNode = curNode.neighbors[Math.floor(Math.random() * curNode.neighbors.length)];
    // console.log(randomNode);

    while(toVist.length > 0) {

    }

}

let g = new Graph('one');

g._root.neighbors.push(new Node('two'));
g._root.neighbors[0].parent = g;

g._root.neighbors.push(new Node('three'));
g._root.neighbors[1].parent = g;

g._root.neighbors.push(new Node('four'));
g._root.neighbors[2].parent = g;

g._root.neighbors[0].neighbors.push(new Node('five'));
g._root.neighbors[0].neighbors[0].parent = g._root.neighbors[0];

g._root.neighbors[0].neighbors.push(new Node('six'));
g._root.neighbors[0].neighbors[1].parent = g._root.neighbors[0];

g._root.neighbors[2].neighbors.push(new Node('seven'));
g._root.neighbors[2].neighbors[0].parent = g._root.neighbors[2];

console.log(g);
// bfs(g, g._root);
// dfs(g, g._root);