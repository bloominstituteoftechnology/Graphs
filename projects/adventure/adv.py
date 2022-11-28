from room import Room
from player import Player
from world import World

import queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Set variables for data structures
traversal_graph = {}
rev_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}


def bfs(starting_room, traversal_graph):
    q = queue.Queue()
    q.put([starting_room])
    visit = set()
    
    while q.empty() is False:
        path = q.get()
        room = path[-1]

        if room not in visit:
            visit.add(room)
            for ex in traversal_graph[room]:
                if traversal_graph[room][ex] == '?':
                    return path
                else:
                    next_room = traversal_graph[room][ex]
                    new_path = path + [next_room]
                    q.put(new_path)
        
    return None 

while len(traversal_graph) < len(room_graph):
    current = player.current_room.id
    if current not in traversal_graph:
        traversal_graph[current] = {ex: '?' for ex in player.current_room.get_exits()}

    room_exit = None
    for ex in traversal_graph[current]:
        if traversal_graph[current][ex] == '?':
            room_exit = ex
            if room_exit is not None:
                traversal_path.append(room_exit)
                player.travel(room_exit)
                new_room = player.current_room.id

            if new_room not in traversal_graph:
                traversal_graph[new_room] = {ex: '?' for ex in player.current_room.get_exits()}

            traversal_graph[current][room_exit] = new_room
            traversal_graph[new_room][rev_dir[room_exit]] = current
            current = new_room
            break

    rooms = bfs(player.current_room.id, traversal_graph)
    if rooms is not None:
        for room in rooms:
            for ex in traversal_graph[current]:
                if traversal_graph[current][ex] == room:
                    traversal_path.append(ex)
                    player.travel(ex)
            current = player.current_room.id

            
    

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
