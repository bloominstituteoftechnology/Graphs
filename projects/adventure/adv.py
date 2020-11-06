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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
############################################################################################################################################################################################################################
roomDirections = {}
rooms = {}
opposite = {'n':'s', 's':'n', 'e':'w', 'w': 'e'}
#less wordy
currRoomExits = player.current_room.get_exits()  
curRoomId =   player.current_room.id 
#adds starting room to rooms
for i in currRoomExits:
    roomDirections[i] = player.current_room.get_room_in_direction(i).id   
rooms[player.current_room.id] = roomDirections
  
def visitRoom():
    currRoomExits = player.current_room.get_exits()  
    curRoomId =   player.current_room.id 
    roomDirections = {}
    travelDirection = 0
    print('starting room',curRoomId)
    if len(rooms) != 20:

        if curRoomId not in rooms:
            #adds to roomDirections
            for direction in currRoomExits:
                roomDirections[direction] = player.current_room.get_room_in_direction(direction).id

            rooms[curRoomId] = roomDirections
            visited_rooms.add(curRoomId)
            rooms[curRoomId][opposite[traversal_path[-1]]] = 'origin'


        if len(rooms[curRoomId]) != 1:
            while currRoomExits[travelDirection] not in rooms[curRoomId] or rooms[curRoomId][currRoomExits[travelDirection]] == 'origin':
                travelDirection = travelDirection +1

            
            #makes sure the road you want to travel to has not been traveled in this direction and is not an origin road so you don't cut yourself off
            if currRoomExits[travelDirection] in rooms[curRoomId] and rooms[curRoomId][currRoomExits[travelDirection]] != 'origin':
                #before you travel make sure you remove this road from currentRoom so you can't travel it again
                rooms[curRoomId].pop(currRoomExits[travelDirection])

                player.travel(currRoomExits[travelDirection])
                traversal_path.append(currRoomExits[travelDirection])
                visitRoom()


        if len(rooms[curRoomId]) == 1:

            #one lenth is one that means all that is left is the origin so just go back
            if rooms[curRoomId][currRoomExits[travelDirection]] != 'origin':
                while currRoomExits[travelDirection] not in rooms[curRoomId]:
                    travelDirection +=1

            rooms[curRoomId].pop(currRoomExits[travelDirection])

            player.travel(currRoomExits[travelDirection])
            traversal_path.append(currRoomExits[travelDirection])


            visitRoom()
    print(len(traversal_path), len(visited_rooms),'lenoftraversalpath............................................................................................................................................')

    print('EndingRooms',  rooms)



visitRoom()
print(len(traversal_path))

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


'''
#######
# UNCOMMENT TO WALK AROUND
#######
roomDirections = {}
rooms = {}
opposite = {'n':'s', 's':'n', 'e':'w', 'w': 'e'}

#prints current room basic info
player.current_room.print_room_description(player)

#adds starting room to rooms
if player.current_room.id not in rooms:
    for i in player.current_room.get_exits():
        roomDirections[i] = player.current_room.get_room_in_direction(i).id   
    rooms[player.current_room.id] = roomDirections

while True:
    #resets roomDirections
    roomDirections = {}

    #takes input direction      (not important)
    cmds = input("-> ").lower().split(" ")


    if cmds[0] in ["n", "s", "e", "w"] and cmds[0] in rooms[player.current_room.id]:
        #travels
        rooms[player.current_room.id].pop(cmds[0])

        player.travel(cmds[0], True)


        #addes to rooms
        if player.current_room.id not in rooms:
            #adds to roomDirections
            for i in player.current_room.get_exits():
                roomDirections[i] = player.current_room.get_room_in_direction(i).id

            rooms[player.current_room.id] = roomDirections

            rooms[player.current_room.id][opposite[cmds[0]]] = 'origin'



    #quits game                (not important)
    elif cmds[0] == "q":
        break
    #make sure its nsew        (not important)
    else:
        print("I did not understand that command.")



    #TEST PRINTS
    print('current',roomDirections)
    for i in rooms:
        print(i, rooms[i])
    print(player.current_room.get_exits()[0])  
'''



