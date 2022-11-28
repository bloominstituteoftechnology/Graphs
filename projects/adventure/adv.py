from room import Room
from player import Player
from world import World
import collections
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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

direction_to_move_in = []
visited = {}
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def traverese_to_next_room(next_direction):
    # Travel in the next direction
    # print("CURRENT ROOM (BEFORE)", player.current_room.id)
    traversal_path.append(next_direction)
    player.travel(next_direction)
    # print("CURRENT ROOM (AFTER)", player.current_room.id)

def traverse_graph():
    visited[player.current_room.id] = player.current_room.get_exits()

    while len(visited) + 1 != len(room_graph):
        next_direction = 0

        # If room is not in visited
        if player.current_room.id not in visited:
            # print("NEVER VISITED")
            # Add it to visited with its exits
            visited[player.current_room.id] = player.current_room.get_exits()
            # Get last direction
            next_direction = direction_to_move_in[-1]

        if (next_direction != 0):
            # If it exists, remove it from list of directions
            directions = visited[player.current_room.id]
            directions.remove(next_direction)
            visited[player.current_room.id] = directions

        while len(visited[player.current_room.id]) < 1:
            # Find and move to the next room until there are none (dead end)
            next_direction = direction_to_move_in.pop()

            # Travel there
            traverese_to_next_room(next_direction)
            # if len(visited[player.current_room.id]) < 1:
            #     print("DEAD END FOUND. BREAKING FROM WHILE")

        # Find the next direction
        next_direction = visited[player.current_room.id].pop()
        # Reverse it. Append that path
        direction_to_move_in.append(reverse[next_direction])
        # Travel there
        traverese_to_next_room(next_direction)

traverse_graph()

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
