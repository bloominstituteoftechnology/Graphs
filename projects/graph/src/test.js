import { Graph, Vertex, Edge} from "./graph.js";

let mg = new Graph();
mg.randomize(2, 2);
let test = mg.bfs(mg.vertexes[0]);
console.log(test);
