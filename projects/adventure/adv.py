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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out
traversalPath = []
print(len(roomGraph), "Length")
print("EXITS", player.currentRoom.getExits())
#-----------
copy={} #Copy of the roomGraph
#-----------
#Chicken scratch stuff
# curRoom=player.currentRoom.id
# print(curRoom, "CurRoom")
# copy[curRoom]=curRoom
# print(copy, "Copy")
# copy[curRoom]=player.currentRoom.getExits()
# print("COPY EXITS", copy[curRoom])
# print(len(copy), "COPY LENGTH")
# if 'n' in copy[curRoom]:
#   print("nnn")
#   # copy[curRoom[0]]='*'
#   print(copy[curRoom] + ["n_visited"], "HERE IS NEW CURROOM")
#-----------
while len(copy) < 9:
# while len(traversalPath) < 3:
  curRoom=player.currentRoom.id
  if curRoom not in copy:
    copy[curRoom]=curRoom 
  
  exits=player.currentRoom.getExits()
  copy[curRoom]=exits
  print("LET'S SEE THIS", copy[curRoom])

  if 'n' in copy[curRoom]:
    print(copy[curRoom], "Currently")
    if "n_visited" not in copy[curRoom]:
      copy[curRoom]=copy[curRoom] + ["n_visisted"]
      player.travel("n")
      traversalPath.append("n")
      print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
      print("*****HERE IS THE COPY*****", copy)
      print("*****HERE IS COPY LENGTH*****", len(copy))
    # copy[curRoom][0]="v"
    # player.travel("n")
    # traversalPath.append("n")
    # print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
    # print("*****HERE IS THE COPY*****", copy)
    # print("*****HERE IS COPY LENGTH*****", len(copy))

  elif 's' in copy[curRoom]:
    print(copy[curRoom], "Currently")
    if "s_visited" not in copy[curRoom]:
      copy[curRoom]=copy[curRoom] + ["s_visisted"]
      player.travel("s")
      traversalPath.append("s")
      print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
      print("*****HERE IS THE COPY*****", copy)
      print("*****HERE IS COPY LENGTH*****", len(copy))
    # copy[curRoom][1]="v"
    # player.travel("s")
    # traversalPath.append("s")
    # print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
    # print("*****HERE IS THE COPY*****", copy)

  elif 'e' in copy[curRoom]:
    print(copy[curRoom], "Currently")
    if "n_visited" not in copy[curRoom]:
      copy[curRoom]=copy[curRoom] + ["e_visisted"]
      player.travel("e")
      traversalPath.append("e")
      print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
      print("*****HERE IS THE COPY*****", copy)
      print("*****HERE IS COPY LENGTH*****", len(copy))
    # copy[curRoom][3]="v"
    # player.travel("e")
    # traversalPath.append("e")
    # print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
    # print("*****HERE IS THE COPY*****", copy)

  elif 'w' in copy[curRoom]:
    print(copy[curRoom], "Currently")
    if "w_visited" not in copy[curRoom]:
      copy[curRoom]=copy[curRoom] + ["w_visisted"]
      player.travel("w")
      traversalPath.append("w")
      print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
      print("*****HERE IS THE COPY*****", copy)
      print("*****HERE IS COPY LENGTH*****", len(copy))

  else: 
    print("error")
    break
    copy[curRoom][2]="v"
    player.travel("w")
    traversalPath.append("w")
    print("*****HERE IS THE TRAVERSAL PATHS*****", traversalPath)
    print("*****HERE IS THE COPY*****", copy)






    
    


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
