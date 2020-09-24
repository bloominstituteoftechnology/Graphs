from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Fill this out with directions to walk
directions = ['n','s', 'e', 'w']
traversal_path = []

# build a graph with room id as key and dic of directions with what rooms are those directions

player = Player(world.starting_room)

# def transverse(starting_room):
#     queue = Queue()

#     visted = set()
#     # put current room in the queue
#     queue.enqueue([starting_room])
#     # set starting_room
#     while queue.size() > 0:
#         path = queue.dequeue()
#         room = path[-1]
#         if room not in visted:
#             visted.add(room)
#             print(visted)
#             # if room is unexplored

#             # get neighbors of the rooms

possible_exits = player.current_room.get_exits()

room_graph = {}

player.travel(directions[0])

def buildGraph(possible_exits, room):
    for exits in possible_exits:
        if player.current_room.id not in room_graph:
            room_graph[player.current_room.id] = {exits : '?'}

buildGraph(possible_exits, player.current_room.id)
print(f'The room graph is', room_graph)
# transverse(room)
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
