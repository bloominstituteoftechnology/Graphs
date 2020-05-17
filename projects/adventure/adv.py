from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
traversal_path = []
adv_map = {}
prev_room = None

def get_next_move(player, adv_map):
    for direction, room in adv_map[player.current_room.id].items():
        if room == '?':
            return direction
    if map_complete(adv_map):
        return None
    else:
        return random.choice(player.current_room.get_exits())
    
def map_complete(adv_map):
    return not any (['?' in exits.values() for exits in adv_map.values()])

def add_new_room(room, prev_room, prev_dir, adv_map):
    adv_map[room.id] = {direction: '?' for direction in room.get_exits()}
    adv_map[room.id][opposite[prev_dir]] = prev_room
    adv_map[prev_room][prev_dir] = room.id
                                    

# Seed map with starting room.
adv_map[player.current_room.id] = {direction: '?' for direction in \
                                       player.current_room.get_exits()}

next_move = get_next_move(player, adv_map)
while next_move is not None:
    prev_room = player.current_room.id
    traversal_path.append(next_move)        
    player.travel(next_move)
    
    if player.current_room.id not in adv_map:
        if player.current_room.id not in adv_map:
            add_new_room(player.current_room,
                         prev_room,
                         traversal_path[-1],
                         adv_map)
    else:
        adv_map[prev_room][traversal_path[-1]] = player.current_room.id
                
    next_move = get_next_move(player, adv_map)
                

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
