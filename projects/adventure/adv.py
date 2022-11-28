from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue
from util import Graph
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
# traversal_path = ['n', 'n','s','s' , 's', 's','n', 'n','w']
traversal_path = [ ]

backtrack = []
reversed_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# instantiate a set to keep track of visited rooms
visited = set()

while len(visited)<len(room_graph):
     
      next_room = None
      
      
      for ex in player.current_room.get_exits():
             
          if  player.current_room.get_room_in_direction(ex) not in visited:
              next_room = ex
          break
      
      
      if next_room is not None:
          traversal_path.append(next_room)
          backtrack.append(reversed_directions [next_room])
          print("V" ,visited)
          player.travel(next_room)
          visited.add(player.current_room)
          print(backtrack)

      else:
           next_room = backtrack.pop() 
           traversal_path.append(next_room)  
            
           player.travel(next_room)    
 
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
