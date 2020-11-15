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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
print("this is my grid", len(world.rooms))

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
inverse_path = {"n": "s", "s": "n", "e": "w", "w": "e"}


def return_home(path, completely=True):
    """returns a complete path to end and back home, unless completely is false, then only the inverse is printed"""
    invert_path = [inverse_path[path[i]] for i in range(len(path))[::-1]]
    path.extend(invert_path)
    if completely:
        return path
    else:
        return invert_path


def traverse_rooms(current_room, path=None, visited=None):
    if path == None:
        path = []
    if visited == None:
        visited = set()
    visited.add(current_room.name)
    current_movements = current_room.get_exits()
    for direction in current_movements:  # every direction I can move in
        next_room = current_room.get_room_in_direction(
            direction)  # grab the room that I can go to
        if len(current_movements) >= 3:
            path = []
        if len(current_movements) == 1 and current_room.get_room_in_direction(direction).name in visited:
            traversal_path.extend(return_home(path))
            return
        elif len(current_movements) == 2 and current_room.rooms_visited(visited):
            traversal_path.extend(return_home(path))
            return
        elif next_room.name not in visited:  # If I haven't been here, let's proceed
            path.append(direction)
            movements = next_room.get_exits()  # Now depending on where I can go
            # If go either proceed or move back, let's carry the path
            if len(movements) == 2:
                traverse_rooms(next_room, [*path], visited)
            # if there are more than 3 places to go
            elif len(movements) > 2:
                traversal_path.extend(path)
                traverse_rooms(next_room, visited=visited)
                traversal_path.extend(return_home(path, False))
            else:
                traverse_rooms(next_room, path, visited=visited)


traverse_rooms(world.starting_room)
# print("this is all that matters now ",traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
