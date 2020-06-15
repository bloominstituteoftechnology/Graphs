from room import Room
from player import Player
from world import World
from util import Stack, Queue

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
traversal_path_for_test = []

path = Stack()

path.push(0)

visited = set()

while len(visited) < len(room_graph):
    nextMove = Stack()

    curr = path.stack[-1]

    visited.add(curr)

    future_moves = room_graph[curr][1]

    for move, next_room in future_moves.items():
        if next_room not in visited:
            nextMove.push(next_room)

    if nextMove.size() > 0:
        room = nextMove.stack[0]
        path.push(room)
    else:
        room = path.stack[-2]
        path.pop()

    for move, next_room in future_moves.items():
        if next_room ==  room:
            traversal_path_for_test.append(move)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

for move in traversal_path_for_test:
    player.travel(move)
    visited_rooms.add(player.current_room.id)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path_for_test)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")