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
traversal_path = [] 
visited = set()
stack = Stack()
# Add starting room to stack
stack.push([player.current_room])

while stack.size() > 0:
    cur_path = stack.pop()
    # current room
    room = cur_path[-1]
    # populate unvisisted neighbors
    neighbors = [(direction, room.get_room_in_direction(direction)) for direction in room.get_exits()]
    if room not in visited:
        # mark room as visisted
        visited.add(room)
        # find the next room to go to
        print(f'\n $$$ current room: {room} $$$ \n')
        # print(f'visisted rooms: {visited} ')
        # print(f'Neighbors: {[(n[0], n[1].id) for n in neighbors]}')
        if len(neighbors) > 0:
            # choose a neighboring room to explore
            # This sets the cardinal direction to direction and the actual room object to next_room
            next_room = random.choice(neighbors)
            # print(f'direction chosen: {direction}')
            print(f'direction chosen: {next_room[0]}')
            # append the cardinal direction chosen
            traversal_path.append(next_room[0])
            stack.push([*cur_path, next_room[1]])
            # print(f'current path: {[node[]]}')
# Room Directions
# self.n_to = None
# self.s_to = None
# self.e_to = None
# self.w_to = None
# Push starting node on stack

# 	while stack isn't empty:
# 		pop the node off the top of the stack
# 		if node isn't visited:
# 			visit the node (e.g. print it out)
# 			mark it as visited
# 			push all its neighbors on the stack

for move in traversal_path:
    player.travel(move)
    # print(f'Current Room:{player.current_room} \n-------------------')



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
