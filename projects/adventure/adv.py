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
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create an empty dictionary to save all the visited rooms
visited = {}
# Create an empty list that will save your reverse path, allowing you to backtrack when neccesary
backtrackPath = []
# Save all possible movement options as keys, with their opposite directions as values
movementOptions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
# Saves the current room (Room Number) in visited as a key, with each possible exit DIRECTION as values
visited[player.current_room.id] = player.current_room.get_exits()

# While not every room has been explored...
while len(visited) < len(room_graph):

    # If the current room has not been visited...
    # Save it as visited, check off where you came from, and see where you can go now
    if player.current_room.id not in visited:
        # Saves the current room in visited as a key (ROOM NUMBER), with each possible exit as values (DIRECTIONS)
        visited[player.current_room.id] = player.current_room.get_exits()
        # Saves the last direction in backtrackPath as the previousRoom
        previousRoom = backtrackPath[-1]
        print("previousRoom(Checking Rooms Case): ", previousRoom)
        print("backtrackPath: ", backtrackPath)
        print("Currently in: ", player.current_room.id)
        # Remove the direction you just came from as a possible exit
        visited[player.current_room.id].remove(previousRoom)

    # elif player.current_room.id is not 0 and len(visited[player.current_room.id]) > 1:
    #     # Save the direction you just came from as the previous room
    #     previousRoom = backtrackPath[-1]
    #     print("previousRoom(Backtracking Case): ", previousRoom)
    #     print("backtrackPath: ", backtrackPath)
    #     print("Currently in: ", player.current_room.id)
    #     # Remove that direction from the backtrackPath
    #     backtrackPath.pop()
    #     # Add that to the answer path
    #     traversal_path.append(previousRoom)
    #     # Go back to the previous room
    #     player.travel(previousRoom)
    #     print("Walking BACK to:", previousRoom)

    # If the current room has unused exits
    # Go through one of the exits and check it off
    elif len(visited[player.current_room.id]) > 0:
        # Save the last of the current rooms exits as a variable
        nextRoom = visited[player.current_room.id][-1]
        print("nextRoom: ", nextRoom)
        print("backtrackPath: ", backtrackPath)
        print("Currently in: ", player.current_room.id)
        # Remove that nextRoom from the current rooms exits
        visited[player.current_room.id].pop()
        # Add that to the answer path
        traversal_path.append(nextRoom)
        # Add the reverse movement to backtrackPath to keep track of where you're going!
        backtrackPath.append(movementOptions[nextRoom])
        # Go into that next room
        player.travel(nextRoom)
        print("Walking to:", nextRoom)

    # If there are no more exits for the current room
    # Backtrack to the previous room
    elif len(visited[player.current_room.id]) == 0:
        # Save the direction you just came from as the previous room
        previousRoom = backtrackPath[-1]
        print("previousRoom(Backtracking Case): ", previousRoom)
        print("backtrackPath: ", backtrackPath)
        print("Currently in: ", player.current_room.id)
        # Remove that direction from the backtrackPath
        backtrackPath.pop()
        # Add that to the answer path
        traversal_path.append(previousRoom)
        # Go back to the previous room
        player.travel(previousRoom)
        print("Walking BACK to:", previousRoom)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
