from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue
import random
from ast import literal_eval



# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
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


# , create a graph
# traverse the graph using dft
# keep track of the direction and the node you visited

visited = set()
# s = Stack()
# s.push(player.current_room.id)  
room_visit_path = []

visited = set()
test =[]
def dft(player, direction=None):
    room_id = player.current_room.id
    room_visit_path.append(room_id)
        
    if room_id not in visited:
        
        visited.add(room_id)
        
        room = room_graph[room_id]
        exits = player.current_room.get_exits()

        for exit in exits: # [n, s, w, e]
            
            new_room = player.current_room.get_room_in_direction(exit)
            new_player = Player(new_room)

            if new_room.id not in visited:
                #recursion
                dft(new_player,exit)
        
                room_visit_path.append(room_id)

                
           
              
               
                # if direction == 'n':
                #     traversal_path.append('s')
                   

                # elif direction=='s':
                #     traversal_path.append('n')
                #     test.append((room_id, 'n'))
                # elif direction=='e':
                #     traversal_path.append('w')
                    
                # elif direction=='w':
                #     traversal_path.append('e')
                
                # print("traversal", room_visit_path)
                # print("traversal", traversal_path)
            
def take_a_walk(player):
    dft(player)             
    for i in range(len(room_visit_path)-1):
        current_room =  room_visit_path[i]
        next_room = room_visit_path[i+1]

        for key, value in room_graph[current_room][1].items():
            if value == next_room:
                traversal_path.append(key)
        

take_a_walk(player)

print('roomvisited', room_visit_path)
# while s.size() > 0:
#     current_room_id = s.pop()
#     print("id", current_room_id)
#     rooms_travelled.append(current_room_id)
    
#     if current_room_id not in visited:
#         visited.add(current_room_id)
#         room = room_graph[current_room_id]
#         print("room", room)
#         exits = random.
#         neighbor = random.choice(room[1][]
            
#             s.push(room[1][neighbor])
           


           
        
    
            
            



            



# visited_new = set()

# while s.size() > 0:
#     player = s.pop()

# #     # get the directions to go to from the current room

#     valid_directions = player.current_room.get_exits()
    
#     for direction in valid_directions:

#         if room_graph[player[1] 

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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")




print("diretions", valid_directions)
#     for direction in valid_directions:

#     if player.current_room.id not in visited:
#         visited.add(player.current_room.id)
#         directions_to_go_to = {}
#         for direction in valid_directions:
#             directions_to_go_to[direction] = '?'
#     # {0: n: ?}
#     # # add the directions to move and the room id to the player_graph {n: ?}
#         player_graph[player.current_room.id] = directions_to_go_to
#     # {0:{n:1, s, e, w}, 1:{n:?, s:0}}

#     player_direction = player_graph[player.current_room.id]

#     # {n: 1, s: ?, e: ?, w: ?}

#     unexplored_routes = [
#         key for key in player_direction if player_direction[key] == '?']
#     #['n', 's']

#     if len(unexplored_routes) > 0:
#         key = random.choice(unexplored_routes)
#         # key = 'n'
#         print(
#             f'key for room {player.current_room.id} is {key} with value {player_direction[key]}')
#         if player_direction[key] == '?':

#             player_direction[key] = player.current_room.get_room_in_direction(
#                 key).id
#             traversal_path.append(key)
#             # [n,]

#             room = player.current_room.get_room_in_direction(key)
#             new_player = Player(room)  # player class (1) which is n

#             s.push(new_player)
#             # [player-room 1]
#             # {0: n:1, s, e , w}
  
        


# # print("visited", visited)
# print("traversal", traversal_path)
# print(player_graph)


# player.current_room.get_room_in_direction(key).id