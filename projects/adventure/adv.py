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
traversal_path = []

def make_traversal_path():
    # result array
    path = []
    # dict holding visited rooms info
    # key is room.id, value is available exits
    visited = {}
    # current room player is in
    current_room = player.current_room

    # function that takes current room to go to next room
    def going_to(current_id):
        # initialize Queue
        q = Queue()
        q.enqueue(([current_id],[]))
        # track of what room has already been already done
        already_done = set()

        while q.size() > 0:
            current = q.dequeue()
            room = current[0][-1]
            # available exits in room
            exits = room_graph[room][1]

            # check room not counted for
            if room not in already_done:
                # check room not visited yet
                if room not in visited:
                    # that is the next room
                    return [room, current[1]]
                # add room to set of already done rooms
                already_done.add(room)
                # randomize find exits
                shuffled_exits = list(exits.keys())
                random.shuffle(shuffled_exits)
                # take all exits is in available exits
                for e in shuffled_exits:
                    # current[0] + exits[e]: adds current room id plus all exits ids
                    # current[1] + [e]: adds current room exits plus avaiable exits
                    # add exits info to queue
                    q.enqueue((current[0] + [exits[e]], current[1] + [e]))

    # Do algorithm until all rooms visited
    while len(visited) < len(world.rooms): #changes based on map selection
        # get current_room id for the key
        room_id = current_room.id
        # get available exits for the value
        exits = room_graph[room_id][1]
        # check room has not been visited
        if room_id not in visited:
            # add info to visited dict
            visited[room_id] = exits
            # use helper function to go from current room to the next room
        next_room = going_to(room_id)
        # check there if there's a room
        if next_room is not None:
            # add room to path. When dead end, adds path back
            path += next_room[1]
            # update current room
            current_room = world.rooms[next_room[0]]

    return path

traversal_path = make_traversal_path()



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
