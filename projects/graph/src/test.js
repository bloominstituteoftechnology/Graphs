import { Graph, Vertex, Edge } from "./graph.js";

let mg = new Graph();
mg.randomize(10, 10);

mg.dump();

console.log(mg.bfs(mg.vertexes[0]));