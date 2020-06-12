from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()



# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
player_graph = {}


#, create a graph
# traverse the graph using dft
# keep track of the direction and the node you visited


visited = set()
s = Stack()
s.push(player) # [player class, ]

print("start", player.current_room)
visited_new=set()

while s.size()> 0:
    player = s.pop()
   
#     # get the directions to go to from the current room
    if player.current_room.id not in visited:
        valid_directions = player.current_room.get_exits() # [n,]
        
        directions_to_go_to = {}
        for direction in valid_directions:
            directions_to_go_to[direction] = '?'
        
    # # add the directions to move and the room id to the player_graph {n: ?}
        player_graph[player.current_room.id] = directions_to_go_to
      
        
        visited.add(player.current_room.id)
   
    

    player_direction = player_graph[player.current_room.id] 
   

  

    for key in player_direction:
        
        if player_direction[key] == '?':
            
            player_direction[key] = player.current_room.get_room_in_direction(key).id
            
            room = player.current_room.get_room_in_direction(key)
            new_player = Player(room)
           
            s.push(new_player)
            if(new_player.current_room.id, key) not in visited_new:
                traversal_path.append(key)
            visited_new.add((new_player.current_room.id, key))
         
print("visited", visited_new)
print("traversal", traversal_path)        
print(player_graph)
        
        
       

player.current_room.get_room_in_direction(key).id




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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
