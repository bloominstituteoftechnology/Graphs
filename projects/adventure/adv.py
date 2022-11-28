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

def traverse(player):
    # create a dict for storage
    d = {}
    # keep track of visited rooms
    visited = []
    # get the id of the starting room 
    starting_room = world.starting_room.id
    # create a dict entry for starting room
    d[starting_room] = {}
    # get starting room exits
    exits = world.starting_room.get_exits()
    # for each exit, create a dict key for that room with '?' value
    for exit in exits:
        d[starting_room][exit] = '?'
        # choose a random direction to start in
    direction = random.choice(exits)
    # get next room id
    next_room = player.current_room.get_room_in_direction(direction).id
    # change the starting room '?' value to room id for that exit
    d[starting_room][direction] = next_room
    # add both rooms to visited
    visited.append([starting_room, next_room])
    # create a stack and queue
    stack = [[next_room, direction]]
    queue = []
    # while the dictionary does not have as many entries as rooms
    while len(d) < len(room_graph):
        # while we have a stack to go through
        while stack:
            # pop off top of stack (curr includes a room 
            # and the direction it takes to get there)
            curr = stack.pop()
            # append direction and then travel
            player.travel(curr[-1])
            traversal_path.append(curr[-1])
            # get exit rooms
            exits = player.current_room.get_exits()
            # if room not in dictionary, add it
            if player.current_room.id not in d:
                d[player.current_room.id] = {}
                for exit in exits:
                    d[player.current_room.id][exit] = '?'
            # get list of unvisited rooms (this area could be condensed)
            list_of_rooms = {}
            for exit in exits:
                list_of_rooms[exit] = player.current_room.get_room_in_direction(exit).id
            unvisited_exits = []
            unvisited_exits.append([k for k, v in list_of_rooms.items() if v not in visited])
            # if unvisited rooms
            try:
                unvisited_exits = unvisited_exits[0][0]
                # get direction for each unvisited room
                for ex in unvisited_exits:
                    direction = ex[0]
                    # add the room to visited
                    visited.append(player.current_room.get_room_in_direction(direction).id)
                    # add room and direction to stack
                    stack.append([player.current_room.id, direction])
                    # add room and direction to dictionary                
                    d[player.current_room.id][direction] = player.current_room.get_room_in_direction(direction).id
            # if no unvisited rooms (this are should be condensed), find an exit with a question mark
            except:
                # empty the stack
                stack = []
                break
        # add current room to queue
        queue.append([player.current_room.id])   
        min_path_length = 999
        # while we have a queue   
        while queue:
            # pop off top path
            path = queue.pop(0)
            # get the last node in the path
            last_in_path = path[-1]
            # if we found a room with a question mark
            if '?' in d[last_in_path].values():
                # use the path to travel to the next room and add to traversal path and visited
                for i, room in enumerate(path[:-1]):
                    direction = list(d[room].keys())[list(d[room].values()).index(path[i+1])]
                    traversal_path.append(direction)
                    player.travel(direction)
                    visited.append(room) # last one will be appended in stack
                # first, find if any unvisited rooms and get list
                exits = player.current_room.get_exits()
                list_of_rooms = {}
                for exit in exits:
                    list_of_rooms[exit] = player.current_room.get_room_in_direction(exit).id
                # see if there are unvisited rooms before choosing one with a '?'
                # get list of unvisited rooms
                unvisited_exits = []
                unvisited_exits.append([k for k, v in list_of_rooms.items() if v not in visited])
                # try getting unvisited rooms
                try:
                    unvisited_exits = unvisited_exits[0][0]
                    # if multiple unvisited rooms
                    if len(unvisited_exits) > 1:
                        # choose one at random and travel, adding to visited and stack and dict
                        random_exit = random.choice(unvisited_exits)
                        chosen_exit_room = player.current_room.get_room_in_direction(random_exit).id 
                        visited.append(chosen_exit_room)
                        d[player.current_room.id][random_exit] = chosen_exit_room
                        stack.append([chosen_exit_room, random_exit])
                        queue = []
                        break
                    # if one unvisited room
                    elif len(unvisited_exits) == 1:
                        #travel there, adding it to visited, stack and dict
                        exit_room = player.current_room.get_room_in_direction(unvisited_exits).id 
                        visited.append(exit_room)
                        d[player.current_room.id][unvisited_exits] = exit_room
                        stack.append([exit_room, unvisited_exits])
                        # empty the queue
                        queue = []
                # if no unvisited rooms
                except:
                    # find rooms whose exits have a value of '? '
                    unknown_exits = [key for (key, value) in d[player.current_room.id].items() if value == '?']
                    # choose one at random , add it to visited, dict, and stack
                    random_direction = random.choice(unknown_exits)
                    chosen = player.current_room.get_room_in_direction(random_direction).id
                    visited.append(chosen)
                    d[player.current_room.id][random_direction] = chosen
                    stack.append([chosen, random_direction])
                    # empty the queue
                    queue = []
            # if this path still contains no rooms with '?' values in its exits         
            else:
                # get exits
                exits = world.rooms[last_in_path].get_exits()
                # for each exit
                for exit in exits:
                    # create a new path, appending the room leading off the exit
                    exit_id = world.rooms[last_in_path].get_room_in_direction(exit).id
                    if exit_id not in path:
                        new_path = list(path)
                        new_path.append(exit_id)
                        queue.append(new_path)
    return traversal_path
    
traverse(player)


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
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")
