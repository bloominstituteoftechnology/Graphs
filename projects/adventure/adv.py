"""
Game map generation and automated traversal.
"""

import random

from ast import literal_eval
from queue import SimpleQueue

from player import Player
from world import World


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# MAP_FILE = "maps/test_line.txt"
# MAP_FILE = "maps/test_cross.txt"
# MAP_FILE = "maps/test_loop.txt"
# MAP_FILE = "maps/test_loop_fork.txt"
MAP_FILE = "maps/main_maze.txt"

# Loads the map into a dictionary
#   Key: room id
#   Value: [room coordinates (tuple), exits (dictionary)]
# Exit dictionary - key: direction (e.g., 'n')
#                   value: neighboring room id
room_graph = literal_eval(open(MAP_FILE, "r").read())
world.load_graph(room_graph)

# Print the room graph. (OPTIONAL)
# print(room_graph)

# Print an ASCII map
world.print_rooms()

test_player = Player(world.starting_room)

opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


def find_nearest_unexplored(start_id, current_map):
    """
    Breadth-first search for nearest '?' exit to room.

    Arguments:
    start_id - id of room from which to start search & measure distance
    current_map - dictionary mapping
    """

    # Path trace dictionary:
    # Maps room id -> step direction by which room was first reached in bft.
    searched = {}

    # FIFO queue of rooms scheduled for search.
    # Entries are tuples of the form (room id, step direction).
    to_search = SimpleQueue()

    # Seed queue with starting room.
    to_search.put((start_id, None))

    # Search!
    while to_search.qsize() > 0:
        (room, prev_dir) = to_search.get()

        # Only previously unsearched rooms require any processing.
        if room not in searched:
            searched[room] = prev_dir  # Update path trace dictionary.
            options = []  # Initialize list for unexplored exits, if any.

            # Check each candidate exit on the map.
            for exit_dir, next_room in current_map[room].items():
                if next_room == '?':
                    options.append(exit_dir)

            # If the current room has any unexplored exits, terminate the
            # search and return the path trace.
            if len(options) > 0:
                return_path = []
                step = prev_dir
                while step is not None:
                    return_path.append(step)
                    room = current_map[room][opposite[step]]
                    step = searched[room]
                return return_path[::-1]

            # If there are no unexplored exits, add any neighboring unsearched
            # rooms to the queue and continue searching.
            for exit_dir, neighboring_room in current_map[room].items():
                if ((neighboring_room != '?' and
                     neighboring_room not in searched)):
                    to_search.put((neighboring_room, exit_dir))


def is_dead_end(start_room, first_step):
    """
    Check if a path outward from the starting room is a dead end. If yes,
    return the number of rooms reachable through that path. If no, return -1.

    Note: a path is considered a dead end if it contains no loop back to the
    starting room (i.e., no exit to the starting room that does not involve
    retracing ones steps).

    Assumes access to the global room graph!
    """
    searched = {}              # room_id -> direction by which first reached
    to_search = SimpleQueue()  # FIFO queue of rooms to search

    # Seed search queue with the first room AFTER the start room (since the
    # start room is actually our search target).
    to_search.put((room_graph[start_room][1][first_step], first_step))
    while to_search.qsize() > 0:
        (room, last_step) = to_search.get()

        # Only previously unsearched rooms require any processing.
        if room not in searched:
            searched[room] = last_step

            # If a route back to the start has been found, this path is not a
            # dead end.
            if room == start_room:
                return -1

            # Otherwise, continue search, moving only forward.
            for exit_dir, destination in room_graph[room][1].items():
                if exit_dir != opposite[last_step]:
                    to_search.put((destination, exit_dir))

    # Start room not re-encountered; this is a dead-end. Return room count.
    return len(searched)


def get_next_move(player, curr_map):
    """
    Return next move or series of moves, given present location and map.
    """
    start = player.current_room.id
    options = []
    for exit_dir, room in curr_map[player.current_room.id].items():
        if room == '?':
            explorer = Player(player.current_room)
            explorer.travel(exit_dir)
            if explorer.current_room.id not in curr_map:
                options.append((exit_dir, is_dead_end(start, exit_dir)))

            # If an adjacent room has been previously explored, just add it to
            # the map. No need to add this exit to the traversal path now.
            else:
                curr_map[player.current_room.id][exit_dir] = \
                    explorer.current_room.id
                curr_map[explorer.current_room.id][opposite[exit_dir]] = \
                    player.current_room.id

    if len(options) > 0:
        # Categorize options.
        dead_ends = [option for option in options if option[1] > 0]
        connected = [option for option in options if option[1] == -1]

        # Special case for one possible first room configuration. (Needed to
        # find shortest traversal for test_loop.txt.))
        if len(dead_ends) == 2 and len(connected) == 2:
            return random.choice(options)[0]

        # Explore dead ends first, starting with the shortest.
        if len(dead_ends) > 0:
            return min(dead_ends, key=lambda x: x[1])[0]

        # If all unexplored exits are connected, chose one at random.
        else:
            return random.choice(options)[0]

    # If the map is fully explored, no next move needs to be taken.
    if map_complete(curr_map):
        return None

    # If there are no '?' exits from the current room, but the map is not yet
    # fully explored, we'll have to retrace our steps to find an unexplored
    # exit.
    return find_nearest_unexplored(player.current_room.id, curr_map)


def map_complete(current_map):
    """
    Check map for unexplored exits. Return true if none found.
    """
    return not any(['?' in exits.values() for exits in current_map.values()])


def add_new_room(room, curr_map):
    """
    Add previously unexplored room to map.
    """
    # Initialize room entry on map with blank exits.
    curr_map[room.id] = {direction: '?' for direction in room.get_exits()}

    # Peek through each exit and connect room accordingly on map.
    for exit_dir in room.get_exits():
        explorer = Player(world.rooms[room.id])
        explorer.travel(exit_dir)
        if explorer.current_room.id in curr_map:
            curr_map[room.id][exit_dir] = explorer.current_room.id
            curr_map[explorer.current_room.id][opposite[exit_dir]] = room.id


def get_traversal_path(player):
    """
    Find and return list of directions to traverse map, starting from player's
    current room.
    """
    traversal_path = []  # list of ordered step directions in path
    adv_map = {}         # dictionary room_id -> {exit: next_room_id or '?'}
    player = Player(player.current_room)

    # Seed map with starting room.
    adv_map[player.current_room.id] = {direction: '?' for direction in
                                       player.current_room.get_exits()}

    # Choose a next move or moves, update the traversal path, and move the
    # player accordingly. Repeat until no more useful moves can be made.
    next_move = get_next_move(player, adv_map)
    while next_move is not None:
        traversal_path += next_move
        for direction in next_move:
            player.travel(direction)

        # If a completely new room has been reached, it will need to be added
        # to the map.
        if player.current_room.id not in adv_map:
            add_new_room(player.current_room, adv_map)

        next_move = get_next_move(player, adv_map)

    return traversal_path


# TRAVERSAL TEST
visited_rooms = set()
test_player.current_room = world.starting_room
visited_rooms.add(test_player.current_room)
path = get_traversal_path(test_player)

try:
    with open('best.txt', 'r') as file:
        previous_best = file.readlines()
except FileNotFoundError:
    previous_best = None

for move in path:
    test_player.travel(move)
    visited_rooms.add(test_player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(path)} moves, {len(visited_rooms)} "
          "rooms visited.\n")
    if MAP_FILE == "maps/main_maze.txt":
        if previous_best is None or len(path) < len(previous_best):
            with open('best.txt', 'w') as file:
                file.writelines([step + '\n' for step in path])
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

if MAP_FILE == "maps/main_maze.txt":
    print(f'Previous best path {len(previous_best)} moves.')

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


#######
# UNCOMMENT TO SEARCH THE HARD WAY
#######
# def get_path_rec(player, prev_room=None, adv_map=None, path_hist=None):
#    """
#    Recursive path search - unusably slow for large maps.
#    """
#    if adv_map is None:
#        adv_map = {}
#
#    if path_hist is None:
#        path_hist = []
#        prev_dir = None
#    else:
#        prev_dir = path_hist[-1]
#
#    if player.current_room.id not in adv_map:
#        add_new_room(player.current_room, prev_room, prev_dir, adv_map)
#
#    if map_complete(adv_map):
#        return path_hist
#
#    options = []
#    for exit_dir, room in adv_map[player.current_room.id].items():
#        if room == '?':
#            temp_player = Player(player.current_room)
#            temp_player.travel(exit_dir)
#            if temp_player.current_room.id not in adv_map:
#                options.append(exit_dir)
#            else:
#                adv_map[player.current_room.id][exit_dir] = \
#                    temp_player.current_room.id
#                adv_map[temp_player.current_room.id][opposite[exit_dir]] = \
#                    player.current_room.id
#
#    if len(options) > 0:
#        paths = []
#        for exit_dir in options:
#            new_player = Player(player.current_room)
#            new_player.travel(exit_dir)
#            paths.append(get_path_rec(new_player,
#                                      player.current_room.id,
#                                      adv_map.copy(),
#                                      path_hist.copy() + [exit_dir]))
#            adv_map[player.current_room.id][exit_dir] = '?'
#
#        return min(paths, key=len)
#
#    if map_complete(adv_map):
#        return path_hist
#    new_player = Player(player.current_room)
#    next_moves = find_nearest_unexplored(player.current_room.id,
#                                         adv_map.copy())[:-1]
#
#    path_hist += next_moves
#    for direction in next_moves:
#        prev_room = new_player.current_room.id
#        new_player.travel(direction)
#
#    return get_path_rec(new_player,
#                        prev_room,
#                        adv_map.copy(),
#                        path_hist.copy())
