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
#MY_CODE###############################################################################################################################################################################################################
'''
roomDirections....keeps track of visited rooms and their none traveld directions

rooms.............temporarily holds a given nodes directions

opposite..........dictionary used to get the oposite of a given direction
'''
roomDirections = {}
rooms = {}
opposite = {'n':'s', 's':'n', 'e':'w', 'w': 'e'}

#less wordy 
currRoomExits = player.current_room.get_exits()  
curRoomId =   player.current_room.id 

#adds starting room to rooms dictionary
for i in currRoomExits:
    roomDirections[i] = player.current_room.get_room_in_direction(i).id   
rooms[player.current_room.id] = roomDirections

#until all 500 rooms have been visited
while len(rooms) != 500:
    '''
    bug... it was traveling twice in one loop and I was tired 
    so this was just the quickest solution at the time. It's fine.
    '''
    bug = 0

    #updates less wordy varibles
    currRoomExits = player.current_room.get_exits()  
    curRoomId =   player.current_room.id

    #resets roomDirections and travel direction for new room 
    roomDirections = {}
    travelDirection = 0

    if curRoomId not in rooms:
        #adds current rooms original directions to roomDirections
        for direction in currRoomExits:
            roomDirections[direction] = player.current_room.get_room_in_direction(direction).id

        #adds roomDirections to it's room in rooms
        rooms[curRoomId] = roomDirections

        #sets the opposite direction of the last known direction on the current node to 'origin'
        rooms[curRoomId][opposite[traversal_path[-1]]] = 'origin'


    #if there is more than one direction
    if len(rooms[curRoomId]) != 1:
        #if you've already traveled the road or it's your way back then try the next travel direction
        while currRoomExits[travelDirection] not in rooms[curRoomId] or rooms[curRoomId][currRoomExits[travelDirection]] == 'origin':
            '''
            travelDirection...a number used to access the original directions list of the current node.
            if rooms says you can't travel a road you just up the number to change directions.
            '''
            travelDirection = travelDirection +1

        
        #makes sure the road you want to travel to has not been traveled in this direction and is not an origin road so you don't cut yourself off
        if currRoomExits[travelDirection] in rooms[curRoomId] and rooms[curRoomId][currRoomExits[travelDirection]] != 'origin':
            #before you travel remove this road from currentRoom so you can't travel it again
            rooms[curRoomId].pop(currRoomExits[travelDirection])

            #traveling...
            player.travel(currRoomExits[travelDirection])
            traversal_path.append(currRoomExits[travelDirection])

            #here that bug from earlier lol this let's us know traveling has already happened this loop
            bug += 1

    #This checks if all that's left is to go back then it goes back to the last known node with more than one exit
    if len(rooms[curRoomId]) == 1 and bug == 0:

        #same princible as line 88
        while currRoomExits[travelDirection] not in rooms[curRoomId]:
            travelDirection +=1

        #traveling...
        rooms[curRoomId].pop(currRoomExits[travelDirection])
        player.travel(currRoomExits[travelDirection])
        traversal_path.append(currRoomExits[travelDirection])

#resets for test
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
######################################################################################################################################################################################################################

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(traversal_path)

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


#original testing code####################################################################
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



