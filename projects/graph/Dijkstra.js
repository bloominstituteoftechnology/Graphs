
function minDistance(dist,sptSet){
    //Note that length of dist and sptSet is same
    let min = Number.MAX_SAFE_INTEGER;
    let minIndex;
    for(let i = 0; i < sptSet.length; i++){
        if(!sptSet[i] && dist[i] < min){
            min = dist[i]
            minIndex= i;
        }
    }
    return minIndex;    
}

function dijkstra(graph,src){
    //Declare a set of distances which will contain the distances 
    //each vertex from the source. Have INT_MAX for each dist initially
    let dist = new Array(graph.length);
    dist.fill(Number.MAX_SAFE_INTEGER);
    //Declare second set of which will contain boolean values
    //to represent if a vertex is chosen in shortest path tree
    //Fill intially with false;
    let sptSet=new Array(graph.length);
    sptSet.fill(false);
    //Distance of source vertex from itself is zero
    dist[src] = 0;

    // Find shortest path for all vertices
    for(let i = 0; i < sptSet.length; i++){
        let u = minDistance(dist,sptSet)
        sptSet[u] = true;
        // Update dist value of the adjacent vertices of the picked vertex.
        for(let v = 0; v<dist.length; v++){
         // Update dist[v] only if is not in sptSet, there is an edge from 
         // u to v, and total weight of path from src to  v through u is 
         // smaller than current value of dist[v]
            if(!sptSet[v] && graph[u][v] && dist[u] !== Number.MAX_SAFE_INTEGER && dist[u]+graph[u][v] < dist[v]){
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
    return dist
}

let myGraph = 
[
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
];
console.log(dijkstra(myGraph,0))