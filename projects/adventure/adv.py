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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
"""
Traversal:
Needs player, the world, and the room_graph
7 8 9
4 5 6
1 2 3
If player is in 5, connected rooms are 2, 4, 6, 8
Need structures for:
Path - list
Each room (for connected rooms) - stack
Visited room - stack
We need a new structure for each room, so in each function call/iteration of loop:
New queue for each room's connected rooms
Loop stops when len(visited_rooms) == len(world.rooms)
current_room goes on stack
Add current_room to visited_rooms
Add connecting_rooms to queue
Get connecting rooms with graph[current_room][1]
284: [(4, 16), {'n': 470, 's': 349, 'e': 254, 'w': 368}]
Check if they are in visited
If connecting_rooms are not in visited_rooms
Add them to queue
Set next_room to first item in queue
Add it to the stack
If next_room is in connecting_rooms: 
Set to current room and add it to path
When queue is empty, pop last item from stack and set to current room
Stack is for connected room and queue is for main room
Queue resets
Rerun until 44 is satisfied?
"""


def maze_travel(player, world, room_graph):
	path = []  # Keep path here
	room_stack = []  # Rooms
	room_stack.append(player.current_room.id)  # Add starting room to stack by id
	print(player.current_room.id)
	visited_rooms = set()
	# Need loop to end when len(visited_rooms) == len(world.rooms)
	while len(visited_rooms) != len(world.rooms):
		"""
		Loop process:
		1. Set current_room to last item on stack
		2. Add current_room to visited_rooms
		3. Find current_rooms connecting_rooms
		4. Add the unvisited rooms rooms to a queue to be traversed
		5. Set the first room in the queue to the next_room
		6. Queue now has unvisited rooms, so we get the first one and add it to the room_stack
		7. Check the current_room's connected_rooms against the next_room
		8. If there is a match, add it to the path
		9. Now the next_room is on the room_stack and will now be set to the current_room
		10. Once the queue is empty, we've traversed that section of the maze and need to go back
		11. We pop off last item from the stack and set current room to new last item on stack
		12. Check again for next_room to be in connecting room
		13. And if it is, add next_room to the path
		14. current_room will be set to next_room, as next_room is last item on stack
		"""
		current_room = room_stack[-1]  # Current room will always be top item on stack
		# print(current_room)
		visited_rooms.add(current_room)  # Add current room to visited rooms
		connecting_rooms = room_graph[current_room][1]  # Check main_maze for object clarity
		connecting_rooms_queue = []
		# for rooms: (name?, con_rooms)
		for name, con_room in connecting_rooms.items():  # .items lets us check keys with values
			if con_room not in visited_rooms:  # If we haven't been to the connected rooms
				connecting_rooms_queue.append(con_room)  # Add it to the queue
		# If there is currently a queue, we go to the first item and set it to the next_room
		if len(connecting_rooms_queue) != 0:
			next_room = connecting_rooms_queue[0]  # set next room to first item in the queue
			room_stack.append(next_room)  # and add it to the stack
		# If the queue is empty
		else:
			room_stack.pop()  # get rid of last item on room_stack
			next_room = room_stack[-1]  # Set the next_room to last item on room_stack
		for name, con_room in connecting_rooms.items():  # for each name and con_rooms in connecting_rooms
			if con_room == next_room:   # If next_room is in connecting_rooms
				path.append(name)       # Add the name of that room to the path
	return path


traversal_path = maze_travel(player, world, room_graph)

# maze_travel(player, world, room_graph)

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
# 	cmds = input("-> ").lower().split(" ")
# 	if cmds[0] in ["n", "s", "e", "w"]:
# 		player.travel(cmds[0], True)
# 	elif cmds[0] == "q":
# 		break
# 	else:
# 		print("I did not understand that command.")
