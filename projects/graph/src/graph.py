"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
from termcolor import colored
import heapq # saves writing a heap

# super really basic vec2 class
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # add
    def add(self, other):
        self.x += other.x
        self.y += other.y

    # subtract
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y

    # multiply
    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y

    # divide (integer)
    def divide(self, other):
        self.x //= other.x
        self.y //= other.y

## decided to add a 3d vector class too you never know when things might get crazy :)
class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # add
    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    # subtract
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    # multiply
    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z

    # divide (integer)
    def divide(self, other):
        self.x //= other.x
        self.y //= other.y
        self.z //= other.z

# Queue for BFS
class Queue:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop(0) if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)


# Stack for DFS (copied my queue class and removed the argument from pop)
class Stack:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop() if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)

# helper class for the a star search with bfs etc
class HeapQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


# implement the basics of a vertex class
class Vertex:
    def __init__(self, id, pos = None, colour = None, data = None):
        self.id = int(id)
        self.pos = Vec2(0, 0) if pos is None else pos
        self.colour = "white" if colour is None else colour
        self.data = F"v{self.id}" if data is None else data
        self.edges = set() # refactored vertex to hold its connecting edges

    def __str__(self):
        return F"Vertex( id: {self.id}, x: {self.pos.x}, y: {self.pos.y}, edge_connections: {self.edges}, data: {self.data})"




class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = None):
        self.vertices = {} if vertices is None else vertices

    # add_vertex method
    def add_vertex(self, id, pos, data):
        self.vertices[id] = Vertex(id, pos, data = data)

    # add_edge method (bi directional as default to start with)
    def add_edge(self, vertex_a, vertex_b, bidir = True):
        self.vertices[vertex_a].edges.add(vertex_b)
        if bidir:
            self.vertices[vertex_b].edges.add(vertex_a)

    # Traversals

    # Depth first Traversal
    def dft(self, start_vert, visited=[]):
        visited.append(start_vert)
        print(self.vertices[start_vert].id, ': ', self.vertices[start_vert].data)

        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                self.dft(child_vert, visited)

    # Breadth first Traversal
    def bft(self, start_vert_id):
        queue = Queue()
        queue.enqueue(start_vert_id)
        visited = []

        while queue.size() > 0:
            vert = queue.dequeue()
            
            if vert not in visited:
                print(self.vertices[vert].id, ": ", self.vertices[vert].data)
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    queue.enqueue(next_vert)

    # Searches

    # Depth first search (leveraging off the DFT method)
    def dfs(self, start_vert_id, target_data, visited=[]):
        visited.append(start_vert_id)
        if start_vert_id == target_data:
            return True

        for child_vert in self.vertices[start_vert_id].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_data, visited):
                    return True

        return False

    # Breadth first search 
    def bfs(self, start_vert_id, target_data):
        queue = Queue()
        queue.enqueue(start_vert_id)
        visited = []
        while queue.size() > 0:
            vert = queue.dequeue()
            if vert not in visited:
                if self.vertices[vert].data == target_data:
                    return True
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    queue.enqueue(next_vert)
        return False

    # paths

    # Path for DFS (Recursive Search)
    def path_d(self, start_vert_id, target_data, visited=[], path=[]):
        visited.append(start_vert_id)
        path = path + [start_vert_id]
        if self.vertices[start_vert_id].data == target_data:
            return path
        for child_vert in self.vertices[start_vert_id].edges:
            if child_vert not in visited:
                new_path = self.path_d(child_vert, target_data, visited, path)
                if new_path:
                    return new_path

        return None

    # Path for BFS (Recursive Search)
    def path_b(self, start_vert_id, target_data):
        queue = Queue()
        queue.enqueue([start_vert_id])
        visited = []
        while queue.size() > 0:
            path = queue.dequeue()
            vert = path[-1]
            if vert not in visited:
                if self.vertices[vert].data == target_data:
                    return path
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        return None

# Hashing out some graph to grid ideas


## helper function for the grid maze (calculation of width bias to make square)
def width_bias(id, width):
    return (id % width, id // width)

# draw a block to the console in ascii with a specific style dependant on grid data
def draw_block(graph, tres, id, style, width):
    block = "."
    if 'number' in style and id in style['number']: block = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: block = ">"
        if x2 == x1 - 1: block = "<"
        if y2 == y1 + 1: block = "v"
        if y2 == y1 - 1: block = "^"
    if 'start' in style and id == style['start']: block = "T"
    if 'goal' in style and id == style['goal']: block = "Z"
    if 'path' in style and id in style['path']: block = "@"
    if id in graph.walls: block = "#" * width
    if id not in graph.walls and random.randint(1, 101) > 99: block = 'T' ## tried to do colored blocks but it messes with the data ## colored('T', 'green')
    return block

# draw a maze to the console utilizing the draw block helper function
def draw_maze(maze, tres, width=2, **style):
    for y in range(maze.height):
        for x in range(maze.width):
            print("%%-%ds" % width % draw_block(maze, tres, (x, y), style, width), end="")
        print()

# data
WALLS = [width_bias(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]
TREASURE = [width_bias(tres, width=30) for tres in [30, 70]]

## Grid Maze Generator
class GridMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.treasure = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def solid(self, id):
        return id in self.walls

    def is_passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.is_passable, results)
        return results


### Adding some more traversal and path finding code
class MazeWithWeights(GridMaze):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    ## added a costings
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

##  add a heuristic method to do some best guess algorithm
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

## added helper function path_fixer
def path_fixer(source_pos, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = source_pos[current]
    path.append(start)
    path.reverse()
    return path

## more complexity for the algorithm to make for some elegant code
## dijkstra search ## referenced : https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def dijkstra_search(graph, start, goal):
    front_bias = HeapQueue()
    front_bias.put(start, 0)
    source_pos = {}
    current_cost = {}
    source_pos[start] = None
    current_cost[start] = 0
    
    while not front_bias.empty():
        current = front_bias.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = current_cost[current] + graph.cost(current, next)
            if next not in current_cost or new_cost < current_cost[next]:
                current_cost[next] = new_cost
                priority = new_cost
                front_bias.put(next, priority)
                source_pos[next] = current
    
    return source_pos, current_cost

## and now for A-STAR (this one i ported over some of my ideas from my JAVA and C++ A-STAR algorithm implementations)
## similar look for this as the J search
def a_star_search(graph, start, goal):
    front_bias = HeapQueue()
    front_bias.put(start, 0)
    source_pos = {}
    current_cost = {}
    source_pos[start] = None
    current_cost[start] = 0
    
    while not front_bias.empty():
        current = front_bias.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = current_cost[current] + graph.cost(current, next)
            if next not in current_cost or new_cost < current_cost[next]:
                current_cost[next] = new_cost
                ## Using my Heuristic helper function
                priority = new_cost + heuristic(goal, next)
                front_bias.put(next, priority)
                source_pos[next] = current
    
    return source_pos, current_cost

# some basic tests for the vertex class

#constructor test
v0 = Vertex(0, Vec2(3, 4))
v1 = Vertex(1, Vec2(1, 3), colour = "orange")
v2 = Vertex(2, Vec2(3, 5))

# raw positional data manipulation test
v0.pos.x = 23

# vector add test
v0.pos.add(Vec2(10, 10))

# vertex print test
print(v0)
print(v1)
g0 = Graph()
g0.add_vertex(v0.id, v0.pos, "Node0")
g0.add_vertex(v1.id, v1.pos, "Node1")
g0.add_vertex(v2.id, v2.pos, "Node2")
g0.add_vertex(3, v2.pos, "Node3")
g0.add_vertex(4, v2.pos, "Node4")
g0.add_vertex(5, v2.pos, "Node5")
g0.add_vertex(6, v2.pos, "Node6")
g0.add_vertex(7, v2.pos, "Node7")
g0.add_vertex(8, v2.pos, "Node8")
g0.add_vertex(9, v2.pos, "Node9")
g0.add_vertex(10, v2.pos, "Node10")
g0.add_vertex(11, v2.pos, "Node11")
g0.add_edge(0, 1)
g0.add_edge(0, 2)
g0.add_edge(1, 3)
g0.add_edge(2, 7)
g0.add_edge(3, 6)
g0.add_edge(1, 4)
g0.add_edge(1, 5)
g0.add_edge(4, 9)
g0.add_edge(4, 8)

print(g0.vertices[0])
print(g0.vertices[1])
print("BFT")
g0.dft(1)
print("DFT")
g0.bft(1)

print(g0.dfs(2, 4))

# loop over the vertices
for vertex, vert in g0.vertices.items():
    print(vertex, ": ", vert.data, ", connections ", vert.edges)

print("\nRecursive DFS with path to destination mapping \n[0 to Node9]")
print(g0.path_d(0, "Node9"))

print("\nRecursive BFS with path to destination mapping \n[7 to Node1]")
print(g0.path_b(7, "Node1"))

## lTODO: lets draw a maze
maze = GridMaze(30, 15)
maze.walls = WALLS
maze.treasure = TREASURE
## print the maze object
print(maze.walls)
print("\n\n\n\n")
draw_maze(maze, tres=[20, 10])
print("\n\n\n\n")


## Maze with weights tests
maze2 = MazeWithWeights(10, 10)
maze2.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
maze2.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 3), (7, 4), (7, 5)]}
# draw_maze(maze2, tres=[])
came_from, cost_so_far = dijkstra_search(maze2, (1, 4), (7, 8))

## draw_maze(maze2, width=3, point_to=came_from, start=(1, 4), goal=(7, 8), tres=[])
draw_maze(maze2, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8), tres=[])
draw_maze(maze2, width=3, path=path_fixer(came_from, start=(1, 4), goal=(7, 8)), tres=[])

start, goal = (1, 4), (7, 8)
came_from, cost_so_far = a_star_search(maze2, start, goal)
draw_maze(maze2, width=3, point_to=came_from, start=start, goal=goal, tres=[])
print()
draw_maze(maze2, width=3, number=cost_so_far, start=start, goal=goal, tres=[])