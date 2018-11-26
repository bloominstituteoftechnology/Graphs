# Travelling Salesman Problem

First thoughts:
- If we weren't limited by computing power, we could look at all permutations, all costs,
and then return the minimum cost
- Obviously that would be horrible, implemented well would lead to O(n!).

Implementation:
- We can represent the cities as vertices, and the routes to each city from city as edges.
We can represent this as a weighted undirected graph, where edges will have weights, according
to the distance.
- I think the best way to approach this would be similar to Dijkstra's algorithm, where
we need to find shortest paths, and then cache those values to be used to reduce amounts
of computation. A dynamic programming approach with memoization that works bottom up
to compute the shortest paths between cities and then use those values to ultimately
find the shortest path to visit all cities?