from room import Room
from player import Player
from world import World
from projects.graph.util import Queue

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
traversal_path = []
total_num_rooms = len(room_graph)

#Left hand on wall rule
lhow = {'n':'e', 'w':'n', 's':'w', 'e':'s'}

# Opposing directions for future functions.
opposing_direction = {'n':'s', 'w':'e', 's':'n', 'e':'w'}

# Room map should be a dictionary where each key has a value of exits. ? denotes unexplored paths.
room_map = {}

def add_room(room):
    if room not in room_map:
        # Initialize the room. All exits are initialized as unexplored.
        room_map[room] = {'n':'?', 's':'?', 'e':'?', 'w':'?'}

        room_exits = room.get_exits()

        for direction in room_map[room]:
            if direction not in room_exits: # Not a valid exit from this room, mark as None.
                room_map[room][direction] = None
    #Else: Does nothing since room doesn't need to be initialized.

def add_path(start_room, end_room, direction):
    # Sets the path from the starting room into the ending room, and vice versa.
    room_map[start_room][direction] = end_room
    room_map[end_room][opposing_direction[direction]] = start_room


add_room(player.current_room)

prev_direction = 'n'

#Tracking number of iterations prevents the infinite loop.
iter = 0
while (len(room_map) < total_num_rooms) and iter < 3000:
    current_room = player.current_room
    # print(current_room)
    room_exits = current_room.get_exits()

    direction = prev_direction

    #Sets to true if we find a room we can go to. If it stays false, it triggers a pathback to a room with unexplored exits.
    found_exit = False

    for i in range(4):
        if room_map[current_room][direction] == '?' and direction in room_exits:
            player.travel(direction)
            next_room = player.current_room
            traversal_path.append(direction)
            found_exit = True
            if next_room in room_map:
                # Already visited this room, backtrack.
                player.travel(opposing_direction[direction])
                traversal_path.pop()
            else:
                add_room(next_room)

            # Add the path to the map
            add_path(current_room, next_room, direction)
            prev_direction = direction

            #Break the for loop
            break
        else: # Either an explored path or an invalid exit.
            #Setting direction to be the left hand rule
            direction = lhow[direction]
    iter += 1

    if not found_exit:
        # We're in a dead end and need to path back to a branching node.
        visited = set()

        queue = Queue()
        queue.enqueue((current_room, []))

        while queue.size() > 0:
            room, path = queue.dequeue()
            # print("ENQUEUED ROOM", room)
            if room in visited:
                continue
            else:
                visited.add(room)

            for direction in room_map[room]:
                if room_map[room][direction] == '?':
                    # Unexplored path, return this path.
                    traversal_path.extend(path)
                    # print(path)
                    for direction in path:
                        # print("MOVING", direction)
                        player.travel(direction)
                    #Empty the Queue. Breaking alone doesn't empty the queue so will continue to add stuff to path.
                    queue = Queue()
                    break
                elif room_map[room][direction] is not None:
                    #Anything other than '?'
                    new_path = path.copy()
                    new_path.append(direction)
                    new_room = room_map[room][direction]
                    queue.enqueue((new_room, new_path))





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
