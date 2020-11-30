from room import Room
from player import Player
from world import World
from collections import deque
import random
from ast import literal_eval

# Load world
world = World()

#construct a  traversal graph
#do dft for finding all the possible  room player can move
#do bfs for finding unexplored direction

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
player.current_room = world.starting_room

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

backtrack = {
    'n': 's',
    'e': 'w',
    'w': 'e',
    's': 'n'}

def bfs(curr_room):
    visited = set()
    queue = deque()
    queue.append((curr_room,[]))

    while len(queue)>0:
        (room,path) = queue.popleft()
        if room in visited:
            continue
        visited.add(room)
        for direction in visited_room[room]:
            if visited_room[room][direction] == '?':
                return [path,direction]
            else:
                newPath = path.copy()
                newPath.append(direction)
                next_room = visited_room[room][direction]
                queue.append((next_room,newPath))

def dft(unexplored_diection):
    stack = deque()
    stack.append(unexplored_diection)

    while len(stack)>0:
        curr_exit = stack.pop()
        move_direction = curr_exit[-1]
        if move_direction not in visited_room[player.current_room.id]:
            continue
        elif visited_room[player.current_room.id][move_direction] == '?':
            prev_room = player.current_room.id
            player.travel(move_direction)
            traversal_path.append(move_direction)

            visited_room[prev_room][move_direction] = player.current_room.id
            opposite_val = backtrack[move_direction]

            if player.current_room.id not in visited_room:
                visited_room[player.current_room.id] = {opposite_val:prev_room}
            else:
                visited_room[player.current_room.id][opposite_val] = prev_room

            for direction in player.current_room.get_exits():
                if direction not in visited_room[player.current_room.id]:
                    visited_room[player.current_room.id][direction] = '?'
                    new_dir = []
                    new_dir.append(direction)
                    stack.append(new_dir)

    unexplored_diection = bfs(player.current_room.id)

    if unexplored_diection != None:
        for direction in unexplored_diection[0]:
            player.travel(direction)
            traversal_path.append(direction)
        dft([unexplored_diection[1]])


starting_dir = random.choice(player.current_room.get_exits())

visited_room = {player.current_room.id:{}}
for direction in player.current_room.get_exits():
    visited_room[player.current_room.id][direction] = '?'

dft(starting_dir)

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

# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
