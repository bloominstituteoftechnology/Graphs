from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "/Users/chrisgonzales/Documents/LambdaCS/LambdaCS/Unit II/Graphs/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/Users/chrisgonzales/Documents/LambdaCS/LambdaCS/Unit II/Graphs/Graphs/projects/adventure/maps/main_maze.txt"

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
    def last(self):
        if self.size() >0:
            return self.stack[-1]
world_map = {}

#   world_map = {
#   0: {'n': '?', 's': 8, 'w': 3, 'e': '?'}
#   8: {n: 0, 'w': '?'}
#   3: {'s': '?', 'w': '?', 'e': 0}
# }

class master_explorer:

    def __init__(self, player: Player, starting_room: Room):
        # Create a current path queue
        self.current_room_path = Stack()
        self.current_directional_path = Stack()
        self.mapping = []
        # Create a room counter
        self.room_count = 0
        # Create a current room
        self.current_room = starting_room
        # Create a previous room
        self.previous_room = None
        self.player = player

    # Check if the map is filled
    def map_filled(self):
        # Check if the room_count is 500 (all the rooms)
        if self.room_count == 500:
            # Check if there are any ?'s in the direction values for each room
            for key, value in world_map.items():
                # If there is a ? return false
                if value == '?':
                    return False
            # If there are no ?'s in any rooms, return false
            return True
        # If the count is not 500, return false
        return False

    def add_room_to_world_map(self):
        # Get the exits of the current room
        exits = self.current_room.get_exits()
        # Create a list of dictionaries for exits, pre-populated with a ?
        exits_dictionary = {direction : '?' for direction in exits}
        # Add the current room to the world_map
        world_map[self.current_room.id] = exits_dictionary
        # Add the current room to the current room path stack
        self.current_room_path.push(self.current_room)
        # Increment the room counter
        self.room_count += 1
        # Connect the current room to the previous room (if not the first room)
        if self.previous_room:
            # Grab the last directional move taken.
            last_direction = self.current_directional_path.last()
            # Set the previous room's selected direction to the current room, and vice versa
            if last_direction == 'n':
                self.previous_room.n_to = self.current_room.id
                self.current_room.s_to = self.previous_room.id
            if last_direction == 's':
                self.previous_room.s_to = self.current_room.id
                self.current_room.n_to = self.previous_room.id
            if last_direction == 'e':
                self.previous_room.e_to = self.current_room.id
                self.current_room.w_to = self.previous_room.id
            if last_direction == 'w':
                self.previous_room.w_to = self.current_room.id
                self.current_room.e_to = self.previous_room.id
    
    def room_has_unexplored_exits(self, room: Room):
        exits = room.get_exits()
        if len(exits) > 0:
            return True
        return False

            ## MOVE METHOD ##

    def move(self):
        # Check the exits in the current room
        current_exits = self.current_room.get_exits() # ['n', 'w']
        # Grab the ID for the current room
        room_id = self.current_room.id
        
        # Attempt to move in order
        for direction in current_exits:
            # Grab the value for the room id and direction
            explored_value = world_map[room_id][direction]
            if explored_value == '?':
                # Create a temp current room
                temp_room = self.current_room
                # Move to the next room in the current direction
                self.player.travel(direction)
                # Log the direction in traversal_path
                self.mapping += direction
                # Log the direction in current_directional_path
                self.current_directional_path.push(direction)
                # Reassign current room to player's current room
                self.current_room = player.current_room
                # Reassign previous room to the temp room
                self.previous_room = temp_room

    def find_nearest_mystery_room(self):
        # Create storage for a retrace path
        retrace_path = Stack()
        # Create temp target room
        target_room = self.current_room
        # Create temp previous room
        temp_previous_room = self.previous_room
        # Grab the last direction in the current track
        last_direction = self.current_directoinal_path[-1]

        # Check if the temp target room has any mystery doors
        while not self.room_has_unexplored_exits(target_room) and len(self.current_directional_path) > 0:
            # Pop the last element off of current track 
            self.current_directional_path.pop()
            # Pop the last room
            self.current_room_path.pop()
            # Check the last direction 
            if last_direction == 'n':
                # Move in the opposite direction
                retrace_path.enqueue('s')
                # Reassign the target room to the 
                target_room = current_room_path[-1]
                # Reassign the last direction
                last_direction = self.current_directional_path.last()
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
            self.player.travel(direction)
            # Add the retrace path to the mapping
            self.mapping += direction
        # Verify the player's current room matches the target room
        # if player.current_room is not target_room:
            
        # Reset the current directional path
        self.current_directional_path = Stack()
        # Reset the current room path
        self.current_room_path = Stack()

    def map(self):
        # Add the starting room to the world map
        self.add_room_to_world_map()
        ## Repeat while the counter is less than 500 and no ?'s in world_map
        while not self.map_filled():
            self.add_room_to_world_map()
            if self.room_has_unexplored_exits(self.current_room):
                self.move()
            else:
                self.find_nearest_mystery_room()
        print(f'{self.mapping}')
        return self.mapping

# explorer = Master_Explorer(player, player.current_room)
# explorer.fill_map()
# print(f'{explorer.mapping}')
# traversal_path = explorer.mapping

class Master_Explorer:
    def __init__(self, starting_room):
        self.mapping = []
        self.current_direction_stack = Stack()
        self.visited = set()
        self.starting_room = starting_room
        self.player = Player(starting_room)
        self.current_room = self.starting_room

    def get_complete_map(self):
        return self.mapping

    def move(self, direction):
        new_room = self.current_room.get_room_in_direction(direction)
        self.current_room = new_room
        player.travel(direction)
        self.mapping.append(direction)

    def build_path(self):
        exits = self.starting_room.get_exits()
        
        for current_exit in exits:
            self.current_direction_stack.push((current_exit, "Forward"))
        self.visited.add(self.current_room)

        while self.current_direction_stack.size() > 0:
            if len(self.visited) == len(world.rooms):
                return
            direction_info = self.current_direction_stack.pop()
            last_move = direction_info[1]
            last_direction = direction_info[0]

            if last_move is "Forward":
                if self.current_room.get_room_in_direction(direction_info[0]) not in self.visited:
                    self.move(last_direction)
                    self.visited.add(self.current_room)
                    self.add_directions(last_direction)
            elif last_move is "Back":
                self.move(last_direction)

    def add_directions(self, last_direction):
        reversed_direction = self.reverse(last_direction)
        self.current_direction_stack.push((reversed_direction, "Back"))
        available_directions = self.current_room.get_exits()

        for available_direction in available_directions:
            room = self.current_room.get_room_in_direction(available_direction)
            if room not in self.visited:
                self.current_direction_stack.push((available_direction, "Forward"))

    def reverse(self, direction):
        if direction == "n":
            return "s"
        elif direction == "s":
            return "n"
        elif direction == "e":
            return "w"
        elif direction == "w":
            return "e"
        else:
            return None

explorer = Master_Explorer(world.starting_room)
explorer.build_path()
traversal_path = explorer.get_complete_map()

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
