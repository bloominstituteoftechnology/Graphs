import { Graph, Vertex, Edge} from "./graph.js";

let mg = new Graph();
mg.randomize(10, 10);
let test = mg.bfs(mg.vertexes[0]);
mg.dump();
