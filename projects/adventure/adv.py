from ast import literal_eval
from queue import SimpleQueue

from player import Player
from world import World


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
opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
traversal_path = []
adv_map = {}
prev_room = None

def find_nearest_unexplored(room_id, adv_map):
    searched = {}
    to_search = SimpleQueue()
    to_search.put((room_id, None))
    while to_search.qsize() > 0:
        (room, direction) = to_search.get()
        if room not in searched:
            searched[room] = direction
            for exit_dir, next_room in adv_map[room].items():
                if next_room == '?':
                    path = [exit_dir]
                    step = direction
                    while step is not None:
                        path.append(step)
                        room = adv_map[room][opposite[step]]
                        step = searched[room]
                    return path[::-1]
                        
            for direction, neighboring_room in adv_map[room].items():
                if neighboring_room != '?' and neighboring_room not in searched:
                    to_search.put((neighboring_room, direction))

def get_next_move(player, adv_map):
    for direction, room in adv_map[player.current_room.id].items():
        if room == '?':
            return [direction]
    if map_complete(adv_map):
        return None
    else:
        return find_nearest_unexplored(player.current_room.id, adv_map)
    
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
    traversal_path += next_move
    for direction in next_move:
        prev_room = player.current_room.id
        player.travel(direction)
    
    if player.current_room.id not in adv_map:
        add_new_room(player.current_room,
                     prev_room,
                     traversal_path[-1],
                     adv_map)
    else:
        adv_map[prev_room][traversal_path[-1]] = player.current_room.id
        adv_map[player.current_room.id][opposite[traversal_path[-1]]] = \
            prev_room
                
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
