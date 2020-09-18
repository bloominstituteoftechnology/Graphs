from room import Room
from player import Player
from world import World
import time 
import sys
import random
import pprint
from ast import literal_eval

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
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)

# Given a direction: n, s, e, or w; return the opposite direction.
backtrack = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def need_to_explore(object):
    if object == None:
        return False 
    if isinstance(object, int):
        #object is an int ( a room ID)
        return False 
    return True 

# Load world
world = World()

import os

dirpath = os.path.dirname(os.path.abspath(__file__))
map_file = dirpath + "/maps/main_maze.txt"
# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open("maps/main_maze.txt", "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

trail = Stack()
traversal_graph = {}

# this is a depth first traversal implementation
def traverse(player, path, trail, map):
    room = player.current_room
    if room.id not in map:
        # Create map entry based on current room object
        map[room.id] = {'n': room.n_to, 's': room.s_to, 'w': room.w_to, 'e': room.e_to}

        # we're in this room for the first time, get exits
        exits = room.get_exits()
        
        if trail.size() > 0:
            # now that we know where the trail leads, update current current rroom with prior room id
            prior_direction, prior_room_id = trail.peek()
            map[room.id][backtrack[prior_direction]] = prior_room_id

        for direction in exits:
            if need_to_explore(map[room.id][direction]):
                trail.push((direction, room.id)) # direction of where we're going next and Room ID of where from
                path.append(direction) # Since we're going there, add it to our path.
                player.travel(direction) # Go there
                traverse(player, path, trail, map)

    # time to backtrack to
    try: 
        direction, _ = trail.pop() # room id not needed here
    except TypeError: # Lands here when trail is enmpty
        direction = None # this fires once whnen we get back to the starting room
        return 

    opposite_direction = backtrack[direction]

    # Go back from whence we came
    player.travel(opposite_direction)
    path.append(opposite_direction)

    # we've return to the room, record the room id of where 'direction goes there 
    traversal_graph[player.current_room.id][direction] = room.id # room id still contains prior room id
    # continue to unwrap

start_time = time.time()
traverse(player, traversal_path, trail, traversal_graph)
end_time = time.time()
print(f"runtime: {end_time - start_time}")

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
