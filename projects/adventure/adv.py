from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "/Users/chrisgonzales/Documents/LambdaCS/LambdaCS/Unit II/Graphs/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "/Users/chrisgonzales/Documents/LambdaCS/LambdaCS/Unit II/Graphs/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print(f'{world.starting_room}')
# print(f'{world.room_grid[13][15]}')
# print(f'{world.room_grid[13][14]}')

''' 
To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

Your solution **must** generate the solution by using graph traversal algorithms. Hardcoding a solution is not acceptable.

'''
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
world_map = {}

#   world_map = {
#   0: {'n': '?', 's': 8, 'w': 3, 'e': '?'}
#   8: {n: 0, 'w': '?'}
#   3: {'s': '?', 'w': '?', 'e': 0}
# }

def master_explorer(player: Player, dungeon: World):

    # Create a current path queue
    current_room_path = Stack()
    current_directional_path = Stack()

    mapping = []

    # Create a room counter
    room_count = 0

    # Create a current room
    current_room = player.current_room

    # Create a previous room
    previous_room = None

    # Check if the map is filled
    def map_filled():
        # Check if the room_count is 500 (all the rooms)
        if room_count == 500:
            # Check if there are any ?'s in the direction values for each room
            for key, value in world_map.items():
                # If there is a ? return false
                if value == '?':
                    return False
            # If there are no ?'s in any rooms, return false
            return True
        # If the count is not 500, return false
        return False

    def add_room_to_world_map(room_count):
        # Get the exits of the current room
        exits = current_room.get_exits()
        # Create a list of dictionaries for exits, pre-populated with a ?
        exits_dictionary = {direction : '?' for direction in exits}
        # Add the current room to the world_map
        world_map[current_room.id] = exits_dictionary
        # Add the current room to the current room path stack
        current_room_path.push(current_room)
        # Increment the room counter
        room_count += 1
        # Connect the current room to the previous room (if not the first room)
        if previous_room:
            # Grab the last directional move taken.
            last_direction = current_directional_path[-1]
            # Set the previous room's selected direction to the current room, and vice versa
            if last_direction == 'n':
                previous_room.n_to = current_room.id
                current_room.s_to = previous_room.id
            if last_direction == 's':
                previous_room.s_to = current_room.id
                current_room.n_to = previous_room.id
            if last_direction == 'e':
                previous_room.e_to = current_room.id
                current_room.w_to = previous_room.id
            if last_direction == 'w':
                previous_room.w_to = current_room.id
                current_room.e_to = previous_room.id
    
    def room_has_unexplored_exits(room: Room):
        exits = room.get_exits()
        if len(exits) > 0:
            return True
        return False

            ## MOVE METHOD ##

    def move():
        # Check the exits in the current room
        current_exits = current_Room.get_exits # ['n', 'w']
        # Grab the ID for the current room
        room_id = current_room.id
        
        # Attempt to move in order
        for direction in current_exits:
            # Grab the value for the room id and direction
            explored_value = world_map[room_id][direction]
            if explored_value == '?':
                # Create a temp current room
                temp_room = current_room
                # Move to the next room in the current direction
                player.travel(direction)
                # Log the direction in traversal_path
                mapping += direction
                # Log the direction in current_directional_path
                current_directional_track += direction
                # Reassign current room to player's current room
                current_room = player.current_room
                # Reassign previous room to the temp room
                previous_room = temp_room

    def find_nearest_mystery_room():
        # Create storage for a retrace path
        retrace_path = Stack()
        # Create temp target room
        target_room = current_room
        # Create temp previous room
        temp_previous_room = previous_room
        # Grab the last direction in the current track
        last_direction = current_directoinal_path[-1]

        # Check if the temp target room has any mystery doors
        while not room_has_unexplored_exits(target_room) and len(current_directional_path) > 0:
            # Pop the last element off of current track 
            current_directional_path.pop()
            # Pop the last room
            current_room_path.pop()
            # Check the last direction 
            if last_direction == 'n':
                # Move in the opposite direction
                retrace_path.enqueue('s')
                # Reassign the target room to the 
                target_room = current_room_path[-1]
                # Reassign the last direction
                last_direction = current_directional_path[-1]
            if last_direction == 's':
                retrace_path.enqueue('n')
                target_room = current_room_path[-1]
                last_direction = current_directional_path[-1]
            if last_direction == 'e':
                retrace_path.enqueue('w')
                target_room = current_room_path[-1]
                last_direction = current_directional_path[-1]
            if last_direction == 'w':
                retrace_path.enqueue('e')
                target_room = current_room_path[-1]
                last_direction = current_directional_path[-1]
        
        # Once a room with a ? is found
        # Move the player to the current room
        for direction in retrace_path:
            player.travel(direction)
            # Add the retrace path to the mapping
            mapping += direction
        # Verify the player's current room matches the target room
        # if player.current_room is not target_room:
            
        # Reset the current directional path
        current_directional_path = Stack()
        # Reset the current room path
        current_room_path = Stack()

    # Add the starting room to the world map
    add_room_to_world_map()
    ## Repeat while the counter is less than 500 and no ?'s in world_map
    while not map_filled:
        add_room_to_world_map(room_count)
        if room_has_unexplored_exits(current_room):
            move()
        else:
            find_nearest_mystery_room()
    print(f'{mapping}')
    traversal_path = mapping


    



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
