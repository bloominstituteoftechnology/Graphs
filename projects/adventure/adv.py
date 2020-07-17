from room import Room
from player import Player
from world import World

import random
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
def backtrack(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

# Pass in a directon object
# Returns whether to explore that direction or not
def need_to_explore(object):
    if object == None:
        return False 
    if isinstance(object, int):
        # object is an int (a room ID)
        return False
    # Object is a Class (an unexplored room)
    return True

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
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

# My Code Starts Here ======================================================
trail = Stack()
traversal_graph = {}

# This is a depth first traversal implementation
def traverse(player, path, trail, map):

    room = player.current_room

    if room.id not in map:
        # We're in this room for the first time, get exits
        exits = room.get_exits()

        # Create map entry based on current room object
        map[room.id] = {'n': room.n_to, 's': room.s_to, 'w': room.w_to, 'e': room.e_to}

        if trail.size() > 0:
            # Now that we know where the trail leads, update current room with prior room's ID
            prior_direction, prior_room_id = trail.peek()
            map[room.id][backtrack(prior_direction)] = prior_room_id

        for direction in exits:
            if need_to_explore(map[room.id][direction]):
                trail.push((direction, room.id)) # direction of where we're going next and Room ID of where from
                path.append(direction) # Since we're going there, add it to our path
                player.travel(direction) # Go there
                traverse(player, path, trail, map)

    # Time to backtrack to...
    try:
        direction, _ = trail.pop() # Room ID not needed here
    except TypeError: # Lands here when trail is empty
        direction = None # This fires once when we get back to the starting room
        return 

    opposite_direction = backtrack(direction)

    # Go back from whence we came
    player.travel(opposite_direction)
    path.append(opposite_direction)

    # We've returned to the room, record the Room ID of where 'direction' goes to
    traversal_graph[player.current_room.id][direction] = room.id # room.id still contains prior room ID

    # Continue to unwrap


traverse(player, traversal_path, trail, traversal_graph)
# ==========================================================================

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
