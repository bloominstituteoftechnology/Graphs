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

#coding start ********
#   bring in the stack and queue


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


# use stack to traverse
stack = Stack()
# make a set()
visited = set()

# setup back tracking directions in case a dead end is reached,


def go_back(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"


# a loop to drive the room pathing, while there are still rooms to explore
# while the length of visited rooms is less than the amount of rooms in the world
while len(visited) < len(world.rooms):

    exits = player.current_room.get_exits()
    path = []
    # refers to the room.py file
    for exit in exits:
        # a check to make sure room move is valid, there is an exit and the room is not visited
        if exit is not None and player.current_room.get_room_in_direction(exit) not in visited:
            # append the exit to the path
            path.append(exit)
            # add the room to the visited rooms list
    visited.add(player.current_room)
    # an if check to make sure the path is over 0
    if len(path) > 0:
        # an if check to make sure there are still ways to travel
        # defining the move, it will use a random integer to randomly choose its next possible direction, making the range of moves each test different,
        #  -1 to grab the end of the list because its a stack,
        move = random.randint(0, len(path) - 1)
        # insert the element to the top of the stack
        stack.push(path[move])
        # player  moves along the path
        player.travel(path[move])

        #

# def travel(self, direction, show_rooms = False):
#         next_room = self.current_room.get_room_in_direction(direction)
#         if next_room is not None:
#             self.current_room = next_room
#             if (show_rooms):
#                 next_room.print_room_description(self)
#         else:
#             print("You cannot move in that direction.")

        # append the path move to the traversal path
        traversal_path.append(path[move])

    else:

        # implement the back tracking if the room leads to a dead end
        deadEnd = stack.pop()
        # pop and remove the top item from the stack
        player.travel(go_back(deadEnd))
        # will travel in opposite direction, as per go_back
        traversal_path.append(go_back(deadEnd))
        # append the path with the direction










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
