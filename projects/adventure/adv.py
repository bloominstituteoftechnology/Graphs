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
        else:
            if len(backtrackStack) <= 0:
                return path
            backtrackDirection = backtrackStack.pop()
            path.append(backtrackDirection)
            player.travel(backtrackDirection)
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

# def find_path_bfs(player, world):
#     graph = {}
#     currPath = []
#     queue = deque()
#     queue.append([player.current_room.id])
#     while len(queue) > 0:
#         currPath = queue.popleft()
#         currRoomID = currPath[-1]
#         currRoom = world.rooms[currRoomID]
#         if currRoomID not in graph:
#             add_room_to_graph(currRoom, graph)
#         for exitDirection in currRoom.get_exits():
#             if graph[currRoomID][exitDirection] == '?':
#                 nextRoom = currRoom.get_room_in_direction(exitDirection)
#                 graph[currRoomID][exitDirection] = nextRoom.id
#                 newPath = list(currPath)
#                 newPath.append(nextRoom.id)
#                 queue.append(newPath)
#     return path_directions_from_room_ids(currPath, graph)
# 
# def path_directions_from_room_ids(pathIDs, graph):
#     pathDirections = []
#     currRoomID = pathIDs[0]
#     for nextRoomID in pathIDs[1:]:
#         for (direction, roomID) in graph[currRoomID].items():
#             if roomID == nextRoomID:
#                 pathDirections.append(direction)
#                 continue
#             else:
#                 print("ERROR: Could not find an exit in the current room that leads to the nextRoomID")
#     return pathDirections

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
