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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Go in the first listed direction as far as you can
# If all adjacent rooms have been explored, identify the nearest unexplored room and go there
reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Initialize from starting room
start = world.starting_room
first_direction = start.get_exits()[0]
visited = {start.id: {x: '?' for x in start.get_exits()}}
rooms_to_visit = [
    (start.id, first_direction, start.get_room_in_direction(first_direction))
]

while len(visited) < len(room_graph):
    prev_room, direction_moved, current_room = rooms_to_visit.pop(0)
    traversal_path.append(direction_moved)
    visited[prev_room][direction_moved] = current_room.id
    if current_room.id not in visited:
        visited[current_room.id] = {x: '?' for x in current_room.get_exits()}
        visited[current_room.id][reverse_direction[direction_moved]] = prev_room
        unvisited_directions = [dir_ for dir_,val in visited[current_room.id].items() if val == '?']
        if len(unvisited_directions) > 0:
            next_direction = random.sample(unvisited_directions,1)[0]
            rooms_to_visit.append((current_room.id, next_direction, current_room.get_room_in_direction(next_direction)))
        else:
            break


# queue = [world.starting_room]
# while len(queue) > 0:
#     current_room = queue.pop(0)
#     if current_room.id in visited:
#         continue
#     visited[current_room.id] = {x:'?' for x in current_room.get_exits()}
#     for direction in current_room.get_exits():
#         next_room = current_room.get_room_in_direction(direction)
#         if next_room is not None:
#             queue.append(next_room)
#             visited[current_room.id][direction] = next_room.id


# print(visited)
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
