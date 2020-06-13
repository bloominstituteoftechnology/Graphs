from room import Room
from player import Player
from world import World
from util import Stack
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

def reverse_exit(direction):
    if direction == 'n':
        return 's'
    elif direction == 'e':
        return 'w'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'

traversal_path = []
path = []
visited = {}
count = 0
cur_room = player.current_room
visited[player.current_room.id] = player.current_room.get_exits()
print(f'starting dict: {visited}')
print(f'length of dict: {len(visited)}')
print(f'path: {path}')
# Loop while there are rooms being passed into the stack
while len(visited) < len(room_graph) -1:
    count+=1
    moves = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    if player.current_room.id not in visited:
        # mark room as visisted
        # populate known rooms into a hash table
        visited[player.current_room.id] = player.current_room.get_exits()
        print(f'current room: {player.current_room.id}: \nexists {visited[player.current_room.id]}')
        # track previous
        prev = path[-1]
        # print(f'visited: {visited[player.current_room.id]}')
        # print(f'current room: {player.current_room.id}')
        # print(f'previous: {prev}')
        visited[player.current_room.id].remove(prev)
        # loop through room's exists

    while len(visited[player.current_room.id]) == 0:
        # back track
        prev = path.pop()
        # record the move back
        traversal_path.append(prev)
        player.travel(prev)

    next_room = visited[player.current_room.id].pop(-1)
    # add next move to our tracking path
    path.append(moves[next_room])
    print(f'adding to path: {moves[next_room]}')
    # add to the instructions path
    traversal_path.append(next_room)
    # move the player
    player.travel(next_room)

        # for exit in room.get_exits():
        #     # define the next room
        #     next_room = room.get_room_in_direction(exit)
        #     print(f'Currently Visited: {next_room}')
        #     # if the exit doesn't lead to a room, mark it as None
        #     if next_room == None:
        #         traversal_graph[room.id][exit] = None
        #     # check if the current exit has a valid room
        #     else:
        #         traversal_path.append(exit)
        #         # add the next room at current exit to our hash table
        #         print(f'picked exit: {exit}')
        #         traversal_graph[room.id][exit] = next_room.id
        #         # copy the current path and add the next room
        #         copy_path = [*cur_path, next_room]
        #         # throw the new path onto stack
        #         stack.push(copy_path)

# 	while stack isn't empty:
# 		pop the node off the top of the stack
# 		if node isn't visited:
# 			visit the node (e.g. print it out)
# 			mark it as visited
# 			push all its neighbors on the stack

# for move in traversal_path:
#     player.travel(move)
#     print(f'Current Room:{player.current_room.id} \n-------------------')


# TRAVERSAL TEST - DO NOT MODIFY
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
