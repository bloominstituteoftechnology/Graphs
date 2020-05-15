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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Set variables for data structures
traversal_graph = {}
intersections = {}
stack = []
rev_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Start in first room
room_id = player.current_room.id

exits = player.current_room.get_exits()
traversal_graph[room_id] = {}
# Set up pointer to track intersections
last_split = None
# Check if start is intersection
if len(exits) > 1:
    # Set pointer to track start of stack
    last_split = room_id
    # Begin path stack
    for ex in exits:
        traversal_graph[room_id][ex] = None
else:
    traversal_graph[room_id][exits[0]] = None   
random.shuffle(exits)
path = [exits[0]]


# While # of rooms in traversal graph is less than # of rooms do
while len(traversal_graph) < len(room_graph):
    # If room zero is not first intersection
    print(traversal_graph)
    print(traversal_path)
    print(stack)
    # while last_split is None:
    #    # move player until you find intersection and start stack
    #     direction = path[-1]
    #     reverse = rev_dir[direction]
    #     prev_room = room_id
    #     player.travel(direction)
    #     room_id = player.current_room.id
    #     exits = player.current_room.get_exits()
    #     traversal_graph[room_id] = {}
    #     traversal_graph[prev_room][direction] = room_id
    #     traversal_graph[room_id][reverse] = prev_room
    #     exits.remove(reverse)
    #     if len(exits) > 1:
    #         random.shuffle(exits)
    #         last_split = room_id
    #         traversal_path = traversal_path + path
    #         path = [exits[0]]
    #     else:
    #         path = path + [exits[0]]
    print(path)
    direction = path[-1]
    reverse = rev_dir[direction]
    prev_room = room_id
    player.travel(direction)
    room_id = player.current_room.id
    exits = player.current_room.get_exits()
    
    if room_id not in traversal_graph:
        traversal_graph[room_id] = {}
        for ex in exits:
            traversal_graph[room_id][ex] = None
        traversal_graph[prev_room][direction] = room_id
        traversal_graph[room_id][reverse] = prev_room
        exits.remove(reverse)
        print(f'possible directions {exits}')
        # If unexplored intesection is found 
       
        if len(exits) < 1:
            rev_path = []
            print(f'dead end: {path}')
            for move in path:
                traversal_path.append(move)
                rev_path.append(rev_dir[move])
            rev_path.reverse()
            print(rev_path)
            for move in rev_path:
                traversal_path.append(move)
                player.travel(move)
            room_id = player.current_room.id
            exits = player.current_room.get_exits()
            unexplored = []
            for ex in exits:
                if traversal_graph[room_id][ex] is None:
                    unexplored.append(ex)
            print(room_id, len(unexplored))
            if len(unexplored) < 1:
                # return to last intersection
                while len(unexplored) < 1:
                    if len(stack) > 0:
                        ret_path = stack.pop()
                        print(ret_path)
                        ret_path.reverse()
                        for move in ret_path:
                            player.travel(rev_dir[move])
                            traversal_path.append(rev_dir[move])
                        room_id = player.current_room.id
                        exits = player.current_room.get_exits()
                        unexplored = []
                        for ex in exits:
                            if traversal_graph[room_id][ex] is None:
                                unexplored.append(ex)
                        if len(unexplored):
                            random.shuffle(unexplored)
                            path = [unexplored[0]]
                            last_split = room_id
                        else:
                            pass
                    else:
                        pass
            else:
                random.shuffle(unexplored)
                path = [unexplored[0]]
        elif len(exits) > 1:
            # Record path to last intersection
            stack.append(path)
            traversal_path = traversal_path + path
            random.shuffle(exits)
            path = [exits[0]]
            last_split = room_id
        # If dead end
        else:
            print(path)
            path = path + [exits[0]]
            print(f'continuing {path}') 

    elif room_id in traversal_graph and room_id == last_split:
        # Found Loop 
        traversal_path = traversal_path + path
        traversal_graph[prev_room][direction] = room_id
        traversal_graph[room_id][reverse] = prev_room
        # Get unexplored exits
        unexplored = []
        for ex in exits:
            if traversal_graph[room_id][ex] is None:
                unexplored.append(ex)
        # If all paths explored return to last intersection
        if len(unexplored) < 1:
            ret_path = stack.pop()
            ret_path.reverse()
            for move in ret_path:
                player.travel(rev_dir[move])
                room_id = player.current_room.id
                exits = player.current_room.get_exits()
                unexplored = []
                random.shuffle(unexplored)
                path = [unexplored[0]]
                last_split = room_id
        else: # Keep exploring intersection
            random.shuffle(unexplored)
            path = [unexplored[0]]
    elif room_id in traversal_graph and room_id != last_split:
        unexplored = []
        for ex in traversal_graph[last_split]:
            if traversal_graph[last_split][ex] == None:
                unexplored.append(ex)
        if len(unexplored) > 1 and len(set(path)) > 3:
            # Loop back to intersection to make sure no path is unexplored
            traversal_graph[prev_room][direction] = room_id
            traversal_graph[room_id][reverse] = prev_room
            rev_path = []
            for move in path:
                rev_path.append(move)
            rev_path.reverse()
            for move in rev_path:
                prev_room = room_id
                player.travel(move)
                traversal_graph[prev_room][move] = None
                traversal_graph[room_id][path.pop()] = None  
            random.shuffle(unexplored)
            path = [unexplored[0]]
        else:
            # found loop
            traversal_path = traversal_path + path
            #remove return path
            if len(stack) > 0:
                stack.pop()
            for ex in exits:
                if traversal_graph[room_id][ex] is not None:
                    exits.remove(ex)
            random.shuffle(exits)
            if len(exits) > 0:
                path = [exits[0]]
        
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
