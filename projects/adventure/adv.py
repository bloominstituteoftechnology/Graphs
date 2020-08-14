from room import Room
from player import Player
from world import World
from util import Queue

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

player = Player(world.starting_room)

visited_rooms = set()
visited_rooms.add(player.current_room)

def room_bft(current_room):
    q = Queue()
    q.enqueue([(current_room.id, "w")])

    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        last_room = path[-1]
        curr_room = world.rooms[last_room[0]]
        exits = curr_room.get_exits()

        for direction in exits:
            next_room = curr_room.get_room_in_direction(direction)

            if next_room not in visited_rooms:
                path.append((next_room.id, direction))
                return path

            if next_room.id not in visited:
                new_path = list(path)
                new_path.append((next_room.id, direction))
                visited.add(next_room.id)
                q.enqueue(new_path)

def travel(path):
    for i in range(1, len(path)):
        direction = path[i][1]
        player.travel(direction)
        traversal_path.append(direction)

while(len(visited_rooms) < len(room_graph)):
    path = room_bft(player.current_room)
    travel(path)
    visited_rooms.add(player.current_room)

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