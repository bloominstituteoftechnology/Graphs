from room import Room
from player import Player
from world import World
from projects.ancestor.ancestor import earliest_ancestor_path

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

# My own variables
returns = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}




traversal_path = []


visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


# FOR MY FIRST EXPLORATION OF THE PROJECT, I USED THE DATA
# AS IT WAS GIVEN TO US TO POPULATE A GRAPH
# CAN UNCOMMENT TO SEE IT WORK, KINDA COOL

# Map to be built
# built_map = {}
#
# def dft(starting_room):
#     visited_rooms.add(starting_room.id)
#     built_map[starting_room.id] = {}
#
#     for room in starting_room.get_exits():
#         built_map[starting_room.id][room] = starting_room.get_room_in_direction(room).id
#         if starting_room.get_room_in_direction(room).id not in visited_rooms:
#             dft(starting_room.get_room_in_direction(room))
#
# dft(player.current_room)
# edited = built_map.copy()
# for key in edited.keys():
#     edited[key] = set(edited[key].values())
# print("THIS IS THE BUILT MAP")
# for item in built_map.items():
#     print(item)

# Traverse the map like a headless chicken
player_map = {}
prev = None
current = player.current_room
finished = False

# Quick method that will tell us if the room we're in has been fully explored
def explored(current, map):
    unexplored = [direction for direction in current.get_exits() if map[current.id][direction] == "?"]
    if len(unexplored) > 0:
        return False
    return True

# DFT Method to find first room with unexplored nodes
first_nonexplored_visited = set()
def dft_empty(starting_room, map):
    first_nonexplored_visited.add(starting_room.id)
    unexplored_paths = [path for path in starting_room.get_exits() if map[starting_room.id][path] == "?"]
    if len(unexplored_paths) > 0:
        return starting_room
    found = None
    rooms = []
    for direction in starting_room.get_exits():
        rooms.append(starting_room.get_room_in_direction(direction))
    for room in rooms:
        if room.id not in first_nonexplored_visited:
            found = dft_empty(room, map)
            if found:
                return found

# BFS will find optimal path from current dead end, to closest unexplored room
def bfs(starting_room, destination_room, map):

    queue = [starting_room.id]
    path = []
    visited = set(queue)

    out = queue.pop(0)
    while out is not None:
        path.append(out)
        visited.add(out)
        next = [value for value in map[out].values() if value != "?" and value not in visited]
        if destination_room.id in next:
            path.append(destination_room.id)
            break
        else:
            for child in next:
                queue.append(child)
        if len(queue):
            out = queue.pop(0)
        else:
            out = None

    reconstructed = [path.pop()]
    while len(path):
        fout = path.pop()
        rooms = [room for room in map[fout].values()]
        if reconstructed[-1] in rooms:
            reconstructed.append(fout)

    reconstructed.reverse()
    # print(f"Shortest path from room {starting_room.id} to {destination_room.id} is:")
    # print(reconstructed)

    translated = []
    for i in range(0, len(reconstructed) - 1):
        directions = [key for key in map[reconstructed[i]].keys()]
        for direction in directions:
            if reconstructed[i+1] is map[reconstructed[i]][direction]:
                translated.append(direction)

    # print("Shortest path translated to instructions")
    # print(translated)
    return translated

# Game loop
while not finished:
    exits = current.get_exits()

    # Populate map entry if it's a new room
    if current.id not in player_map:
        player_map[current.id] = {cardinal: "?" for cardinal in exits}

    # Previous will hold a tuple
    # Index 0 holds the room
    # Index 1 holds the direction we took to get here
    if prev is not None:
        player_map[current.id][returns[prev[1]]] = prev[0].id

    # Check that we have an unexplored path
    options = [option for option in exits if player_map[current.id][option] == "?"]

    # If we have an unexplored path, do your thing
    if len(options):

        # Pick a random direction
        direction = options[random.randint(0, len(options) - 1)]

        # Store current room into previous plus the direction we're going to move in as a tuple
        prev = (player.current_room, direction)
        traversal_path.append(direction)
        # print(f"Moving towards: {direction}" )

        # Move player into this direction
        player.travel(direction)

        # Store new current into current
        current = player.current_room

        # Connect room objects
        prev[0].connect_rooms(prev[1], current)
        current.connect_rooms(returns[prev[1]], prev[0])

        # Fill out our map
        player_map[prev[0].id][prev[1]] = current.id
        # test_map[current.id][returns[prev[1]]] = prev[0].id


        # print(f"Current room now is: {current.id}")
    else:
        # print()
        # print("--------------------------------")
        # print(f"Hit a deadend at {current.id}")
        # print("Current map:")
        # for item in test_map.items():
        #     print(item)

        # Check if we explored the entire map
        found = False
        for item in player_map.keys():
            # If we find a "?" in our map, it means we're not done.
            # Otherwise, we're finished
            if "?" in player_map[item].values():
                found = True
                break
        if not found:
            print("We done")
            # print("Our map:")
            # print(test_map)
            # print("Travel path:")
            # print(traversal_path)
            # print("length of travel path:")
            # print(len(traversal_path))
            break

        # Find the first room with no traversed path
        # print(f"Travel path {traversal_path}")

        # Reset the visited set used by our dft function
        first_nonexplored_visited = set()
        first_empty2 = dft_empty(current, player_map)

        # print(f"Shortest path from room {current.id} to {first_empty2.id} is:")

        # Get the shortest path from current dead end to closest
        # unexplored room in an array with directions
        backtrack = bfs(current, first_empty2, player_map)

        # For each direction returned, move our player
        # and add our movement to our path
        for direction in backtrack:
            # print(f"Traveling towards: {direction}")
            traversal_path.append(direction)
            player.travel(direction)
            current = player.current_room
            # print(f"Current room now is: {current.id}")

        # Reset previous if we have backtracked.
        prev = None
        # print()

#
# TRAVERSAL TEST
#

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
#         print("Name before")
#         print(player.current_room.name)
#         player.travel(cmds[0], True)
#         print("Name after")
#         print(player.current_room.name)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
