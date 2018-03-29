class Graph{
    constructor(){
        this.noOfvertices = 0;
        this.adjList = new Map();
    }
    addVertex(value){
        this.noOfvertices++
        this.adjList.set(value,[]);
    }

    addEdge(source,destination){
        if(!this.adjList.get(source)){
            this.addVertex(source)
        }
        if(!this.adjList.get(destination)){
            this.addVertex(destination)
        }
        this.adjList.get(source).push(destination)
    }

    bfs(src){
        let queue = [src];
        let visited = [];
        visited[src] = true;
        while(queue.length){
            let removed = queue.shift();
            console.log(removed)
            let edges = this.adjList.get(removed);
            for(let i = 0; i < edges.length; i++){
                if(!visited[edges[i]]){
                    visited[edges[i]] = true;
                    queue.push(edges[i])
                }
            }
        } 
    }
    dfs(src, visited = []){
        console.log(src)
        visited[src] = true
        let edges = this.adjList.get(src)
        for(let i = 0; i < edges.length; i++){
            if(!visited[edges[i]]){
                this.dfs(edges[i],visited)
            }
        }
    }  
}

let myGraph = new Graph()
myGraph.addEdge(0, 1);
myGraph.addEdge(0, 2);
myGraph.addEdge(1, 2);
myGraph.addEdge(2, 0);
myGraph.addEdge(2, 3);
myGraph.addEdge(3, 3);
console.log(myGraph)
console.log(myGraph.bfs(2))
console.log(myGraph.dfs(0))