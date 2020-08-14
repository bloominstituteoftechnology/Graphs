from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

visited = {} # we can use a dictionary here with
            # keys being rooms we visited, values being a dictionary of exits

reverse_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Let's start with a modified BFT  function to explore the graph
def breadth_f_t(graph, starting_room):
    """
    Takes a graph of visited rooms and finds a route after a dead end
    Seek a room with ? exits
    """
    q = Queue()

    visited = set()  

    path_to_unexplored = []
    q.enqueue([starting_room])
    
    while q.size() > 0:
        
        path = q.dequeue()
        
        current_room = path[-1]
        if current_room not in visited:
            visited.add(current_room)
            # check each direction to see if you have unexplored options
            for room in graph[current_room]:
                if graph[current_room][room] == "?":
                    return path
            # get the directions you can travel and queue it up to explore back
            for room_exit in graph[current_room]:
                path_to_unexplored.append(room_exit)
                next_room = graph[current_room][room_exit]

                # use a copy of paths so we can explore alt routes
                path_copy = path.copy()
                path_copy.append(next_room)
                q.enqueue(path_copy)




while len(visited) < len(room_graph):
    current_room = player.current_room.id
   
    if current_room not in visited:
        # Initialize
        visited[current_room] = {}

        for direction in player.current_room.get_exits():
            # initialize
            visited[current_room][direction] = "?"
    for path in visited[current_room]:
        if path not in visited[current_room]:
            break
        if visited[current_room][path] == "?":
            exit_path = path
            if exit_path is not None:
                traversal_path.append(exit_path)
                player.travel(exit_path)
                new_roomID = player.current_room.id
                if new_roomID not in visited:
                    visited[new_roomID] = {}
                    for direction in player.current_room.get_exits():
                        visited[player.current_room.id][direction] = "?"
            visited[current_room][exit_path] = new_roomID
            # set the reverse path as known
            visited[new_roomID][reverse_direction[exit_path]] = current_room
            current_room = new_roomID
    # Now that we explored all ?s
    paths = breadth_f_t(visited, current_room)
    if paths is not None:
        for room_number in paths:
            for room in visited[current_room]:
                if visited[current_room][room] == room_number:
                    traversal_path.append(room)
                    player.travel(room)
    current_room = player.current_room.id

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

