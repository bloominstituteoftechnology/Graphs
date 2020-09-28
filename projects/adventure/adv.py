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
import os.path
map_file = "maps/main_maze.txt"
map_file = os.path.join(os.path.dirname(__file__), map_file)

# Read in all the words in one go

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
from collections import deque

def find_path(player, world):
    graph = {}
    path = []
    backtrackStack = deque()
    while len(graph) < len(world.rooms):
        currRoom = player.current_room
        if currRoom.id not in graph:
            add_room_to_graph(currRoom, graph)
        unexploredDirections = unexplored_directions(currRoom, graph)
        if len(unexploredDirections) > 0:
            newDirection = random.choice(unexploredDirections)
            backtrackStack.append(opposite(newDirection))
            path.append(newDirection)
            player.travel(newDirection)
            nextRoom = player.current_room
            graph[currRoom.id][newDirection] = nextRoom.id
            if nextRoom.id not in graph:
                add_room_to_graph(nextRoom, graph)
            graph[nextRoom.id][opposite(newDirection)] = currRoom.id
        else:
            if len(backtrackStack) <= 0:
                return path
            backtrackDirection = backtrackStack.pop()
            path.append(backtrackDirection)
            player.travel(backtrackDirection)
            nextRoom = player.current_room
            graph[currRoom.id][backtrackDirection] = nextRoom.id
    path.append(opposite(path[-1]))
    return path

def add_room_to_graph(room, graph):
    if room.id in graph:
        return
    exits = {}
    for exit_direction in room.get_exits():
        exits[exit_direction] = '?'
    graph[room.id] = exits

def opposite(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        return None

def unexplored_directions(room, graph):
    unexploredDirections = []
    for (direction, roomID) in graph[room.id].items():
        if roomID == '?':
            unexploredDirections.append(direction)
    return unexploredDirections

traversal_path = find_path(player, world)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path[:-1]:
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
