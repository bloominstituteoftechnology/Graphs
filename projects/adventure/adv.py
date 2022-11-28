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
map_file = "maps/test_loop.txt"
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
traversal_path = []
travel_plans = []
unexplored_exits = []

# directions
directions = {}
opposite_lookup = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# update rooms in map
def update_map(room, next_room):
    if next_room is not None:
        for i in range(len(room.get_exits())):
            for j in range(len(next_room.get_exits())):
                if next_room.id not in directions:
                    directions[next_room.id] = {next_room.get_exits()[j]: '?' for j in range(len(next_room.get_exits()))}
                if room.get_room_in_direction(room.get_exits()[i]) == next_room:
                    directions[room.id].update({room.get_exits()[i]: next_room.id})
                    directions[next_room.id].update({opposite_lookup.get(room.get_exits()[i]): room.id})
    else:
        directions[room.id] = {room.get_exits()[i]: '?' for i in range(len(room.get_exits()))}

# update player starting room
update_map(world.starting_room, next_room=None)

def walk_in_straight_line(direction):
    travel_plans.append(direction)
    while directions[player.current_room.id][direction] == '?':
        update_map(player.current_room, player.current_room.get_room_in_direction(direction))
        if directions[player.current_room.get_room_in_direction(direction).id][direction] == '?':
            travel_plans.append(direction)
            for i in range(len(travel_plans)):
                travel_plans.append(opposite_lookup.get(direction))

def find_nearest_unmapped_exit():
    travel_plans.append

for i in range(len(player.current_room.get_exits())):
    if directions[player.current_room.id][player.current_room.get_exits()[i]] == '?':
        unexplored_exits.append(player.current_room.get_exits()[i])
        
for j in unexplored_exits:
    walk_in_straight_line(player.current_room.get_exits()[i])
            # walk_in_straight_line(travel_plans[j])
            # traversal_path.extend(travel_plans)
            # print(travel_plans)

print(travel_plans)

# if directions[player.current_room.id]['n'] == '?':
#     walk_in_straight_line('n')
#     traversal_path.extend(travel_plans)
#     travel_plans = []
# if directions[player.current_room.id]['s'] == '?':
#     walk_in_straight_line('s')
#     traversal_path.extend(travel_plans)
#     travel_plans = []
# if directions[player.current_room.id]['w'] == '?':
#     walk_in_straight_line('w')
#     traversal_path.extend(travel_plans)
#     travel_plans = []
# if directions[player.current_room.id]['e'] == '?':
#     walk_in_straight_line('e')
#     traversal_path.extend(travel_plans)
#     travel_plans = []


# for i in range(len(player.current_room.get_exits())):
#     if directions[player.current_room.id].get(player.current_room.get_exits()[i]) == '?':
#         traversal_path.append(player.current_room.get_exits()[i])
#         update_map(player.current_room, player.current_room.get_room_in_direction(player.current_room.get_exits()[i]))

# for direction in directions:
#     traversal_path.append(directions.get(player.current_room.id)[0])

# print(directions)
# update_map(player.current_room, player.current_room.n_to)
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
