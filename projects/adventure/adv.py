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

# TODO: HOW ARE WE SUPPOSED TO BUILD THE GRAPH
def buildGraph(starting_room, current_room, directions):
    dict = {},
    if starting_room not in dict:
        dict[starting_room] = starting_room
    
    return dict

# Fill this out with directions to walk
directions = ['n','s', 'e', 'w']
traversal_path = []

# build a graph with room id as key and dic of directions with what rooms are those directions

player = Player(world.starting_room)

# When traveling update the direction in room traveled from with the room traveled to 
def update_graph(room):
    for k, v in room_graph.items():
        print(k, v)
        for k, v in v.items():
            if k == 'n':
                print('here')
                print(k, v)
                v = player.current_room.id
                print(k, v)

queue = Queue()
# put current room in the queue
# set starting_room
starting_room = player.current_room.id
queue.enqueue([starting_room])

visited = set()
# get the exits of the current room
room_exits = player.current_room.get_exits()
while queue.size() > 0:
    print(queue)
    current_path = queue.dequeue()
    print(f'\nthe currrent_path is {current_path}')
    current_node = current_path[- 1]
    print(f'\nthe current_node is {current_node}')
    # loop through room's exits
    for exit in room_exits:
        # go to the exits that exists in the current room
        print(f'{exit}')
        print(f'current room is {player.current_room.id}')
        player.travel(exit, True)
        # when you travel update the room that you traveled from direction


        room_graph = buildGraph(starting_room, player.current_room.id, directions)
        print(f'{room_graph}')


# def transverse():

#         if current_node not in visited:
#             visited.add(current_node)
#             print(f'visited: {visited}')
#             for neighbor in room_graph[player.current_room]:
#                 newPath = list(current_path)
#                 # [1, 2, 4,6]
#                 newPath.append(neighbor)
#                 # [6]
#                 print(f'the new path is: {newPath}')
#                 queue.enqueue(newPath)


#     print(f'\ncurrent room graph is {room_graph}\n')

#     player.travel('n')
#     print('player is in room,', player.current_room.id)
    # if there is a room n, s, e, w change corresponding value from ? to room ID 
    # update graph at previous room, change direction value to room traveled to
    # print(room_graph)
    # add new room to graph
    # room_graph[player.current_room.id] = 

# loop through rooms:
    # if there is a room in that direction:
        # BFT 
    # if there is no room in that direction:
        # DFT - find the ? than transverse again
    # travel to each direction:


    # if the room has exits transverse

    # Tranverse rooms with BFT
    # if player.current_room.get_exits() is false:
        # use DFT to search for question marks

# transverse()
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
