from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



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

# default traversal path
traversal_path = []

reverse = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w',
}

# create function to track paths
def traverse(current_room, visited = None):
    # path for moves while movingr rooms
    path = []
    
    # 1st loop to init a visited set
    if visited == None:
        visited = set()
    
    # find all exits for the current room 
    for move in player.current_room.get_exits():
        # move in selected direction
        player.travel(move)
    
        # if room is visisted already, move to previous room and find unvisited path
        if player.current_room in visited:
            player.travel(reverse[move])
        # if room is unvisited, add to visite
        else:
            visited.add(player.current_room)
            # add the move to the path
            path.append(move)
            # recursive call to repeat the loop above and add to path
            path = path + \
                traverse(player.current_room, visited)
            # move to the previous room
            player.travel(reverse[move])
            # adds reversing to the path
            path.append(reverse[move])
    return path


traversal_path = traverse(player.current_room)
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
