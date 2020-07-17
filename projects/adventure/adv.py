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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# My own variables
NORTH = "n"
SOUTH = "s"
WEST = "w"
EAST = "e"

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


# Map to be built
built_map = {}

def dft(starting_room):
    visited_rooms.add(starting_room.id)
    built_map[starting_room.id] = {}

    for room in starting_room.get_exits():
        built_map[starting_room.id][room] = starting_room.get_room_in_direction(room).id
        if starting_room.get_room_in_direction(room).id not in visited_rooms:
            dft(starting_room.get_room_in_direction(room))

dft(player.current_room)
edited = built_map.copy()
for key in edited.keys():
    edited[key] = set(edited[key].values())
# print("THIS IS THE BUILT MAP")
# for item in built_map.items():
#     print(item)

# Traverse the map like a headless chicken
test_map = {}
depth = []
prev = None
current = player.current_room
finished = False

def explored(current, map):
    unexplored = [direction for direction in current.get_exits() if map[current.id][direction] == "?"]
    if len(unexplored) > 0:
        return False
    return True

# DFT Method to find first room with unexplored nodes
first_nonexplored_visited = set()
def dft_empty(starting_room):
    first_nonexplored_visited.add(starting_room.id)
    options3 = [option2 for option2 in starting_room.get_exits() if test_map[starting_room.id][option2] == "?"]
    if len(options3):
        return starting_room

    for room in starting_room.get_exits():
        if starting_room.get_room_in_direction(room).id not in first_nonexplored_visited:
            return dft_empty(starting_room.get_room_in_direction(room))

def bfs(starting_room, destination_room, map):

    queue = [starting_room.id]
    path = []
    visited = set(queue)

    out = queue.pop(0)
    while out is not None:
        path.append(out)
        visited.add(out)
        next = [value for value in map[out].values()]
        print(next)
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
    print(f"Shortest path from room {starting_room.id} to {destination_room.id} is:")
    print(reconstructed)
    # return reconstructed

while not finished:
    exits = current.get_exits()
    if current not in test_map:
        test_map[current.id] = {cardinal: "?" for cardinal in exits}
    # Previous will hold a tuple
    # Index 0 holds the room
    # Index 1 holds the direction we took to get here
    if prev is not None:
        # Connect room object
        prev[0].connect_rooms(prev[1], current)
        current.connect_rooms(returns[prev[1]], prev[0])
        # Fill out our map
        test_map[prev[0].id][prev[1]] = current.id
        test_map[current.id][returns[prev[1]]] = prev[0].id

    # Check that we have an unexplored path
    options = [option for option in exits if test_map[current.id][option] == "?"]

    # If we have an unexplored path, do your thing
    if len(options):
        # Pick a random direction
        direction = options[random.randint(0, len(options) - 1)]

        # Store current room into previous plus the direction we're going to move in as a tuple
        prev = (player.current_room, direction)
        traversal_path.append(direction)
        print(f"Moving towards: {direction}" )
        # Move player into this direction
        player.travel(direction)

        # Store new current into current
        current = player.current_room
        print(f"Current room now is: {current.id}")
    else:
        print(f"Hit a deadend at {current.id}")

        # Check if we explored the entire map
        found = False
        for item in test_map.keys():
            if "?" in test_map[item].values():
                found = True
                break
        if not found:
            print("We done")
            exit()


        # Find the first room with no traversed path
        print(f"Travel path {traversal_path}")
        first_empty2 = dft_empty(current)
        print(f"First room with empty rooms from dft {first_empty2.id}")
        bfs(current, first_empty2, test_map)
        break
        # step = len(traversal_path) - 1
        # backtrack = returns[traversal_path[step]]
        # traversal_path.append(backtrack)
        # step -= 1
        # backtrack = returns[traversal_path[step]]
        # player.travel(backtrack)
        # first_empty = player.current_room
        #
        # while explored(first_empty, test_map):
        #     step -= 1
        #     backtrack = returns[traversal_path[step]]
        #     traversal_path.append(backtrack)
        #     step -= 1
        #     backtrack = returns[traversal_path[step]]
        #     player.travel(backtrack)
        #     first_empty = player.current_room

        print(f"Travel path {traversal_path}")
        print(f"First room with empty rooms from dft {first_empty2.id}")
        # print(f"First room with empty rooms from while loop {first_empty.id}")


for item in test_map.items():
    print(item)

# TRAVERSAL TEST
#
# for move in traversal_path:`
#     player.travel(move)
#     visited_rooms.add(player.current_room)
#
# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
