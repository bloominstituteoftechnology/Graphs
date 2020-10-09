from room import Room
from player import Player
from world import World

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
dungeon_map = {player.current_room.id: {d: "?" for d in player.current_room.get_exits()}}
opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}


def ocular_patdown(id):
    exits = []
    for exit in dungeon_map[id]:
        if dungeon_map[id][exit] == '?':
            exits.append(exit)
    return exits
       

def explore(start_room):
    while len(ocular_patdown(start_room)) > 0:
        location = start_room
        direction = random.choice(ocular_patdown(start_room))

        player.travel(direction)
        traversal_path.append(direction)

        if player.current_room.id not in dungeon_map:
            dungeon_map[player.current_room.id] = {d: "?" for d in player.current_room.get_exits()}

        dungeon_map[player.current_room.id][opposite_direction[direction]] = location
        dungeon_map[location][direction] = player.current_room.id

        start_room = player.current_room.id

def nearest_room(room):
    q = [room]
    
    visited = set()

    while len(q) > 0:
        current_room = q.pop(0)
        if current_room not in visited:
            visited.add(current_room)
            if len(ocular_patdown(current_room)) > 0:
                return current_room

            for next_room in dungeon_map[current_room].values():
                q.append(next_room)
            
def nearest_room_path(target):
    start = player.current_room.id
    q = [[start]]
    visited = set()
    path_to_target = []

    while len(q) > 0:
        path = q.pop(0)
        room = path[-1]

        if room not in visited:
            visited.add(room)
            if room == target:
                path_to_target = path
                break
            for next_room in dungeon_map[room].values():
                new_path = list(path) + [next_room]
                q.append(new_path)

    final_path = []

    for i in range(len(path_to_target) - 1):
        for d in dungeon_map[path_to_target[i]]:
            if dungeon_map[path_to_target[i]][d] == path_to_target[i + 1]:
                final_path.append(d)
    return final_path


while len(dungeon_map) < 500:
    explore(player.current_room.id)
    target = nearest_room(player.current_room.id)
    target_path = nearest_room_path(target)

    for d in target_path:
        player.travel(d)
        traversal_path.append(d)


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
