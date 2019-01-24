from room import Room
from player import Player
from item import Item

from world import World


world = World()

# Uncomment this to generate the default rooms from Week 1
# world.generateDefaultRooms()

# This will generate 100 rooms.
# You will be modifying this function in world.py for better
# room generation.
world.generateRooms(5)

print("print initial coordinates of all rooms: ")
for id in range(0, len(world.rooms)):
    print(world.rooms[id].xy)

# Add some items
junk = Item("Junk", "This is junk")
rock = Item("Rock", "This is a rock")

# Give the player junk and put the rock in the starting room
playerStartingItems = [junk]

world.startingRoom.addItem(rock)

# ***********************
# Day 7 MVP 
# ***********************

diamond = Item('Diamond', "This is a diamond")
# drop a rock item in a random room
diamond_rm = world.random_treasure_drop(diamond)
print("Diamond in room: ", diamond_rm.xy)
print("Diamond room has items: ", diamond_rm.items[0].name)
# call a method to return the shortest path (through breath first search) from starting room to room with the randomly-dropped rock
bfs_path = world.find_path_to_item(diamond)
# print out bfs_path
if not bfs_path:
    print("No path is found")
else:
    print("Path to diamond: ")
    print(bfs_path[0].xy)
    for room in bfs_path[1:]:
        print("   |")
        print("   v")
        print(room.xy)
        


#################################
#
# Below is the adventure REPL code.
#
#################################

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "north": "n", "south": "s", "east": "e", "west": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), world.startingRoom, playerStartingItems)

print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "l" or cmds[0] == "look":
            player.look()
        elif cmds[0] == 'pm':
            world.printMap()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "l" or cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have picked up {itemToTake.name}")
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            player.dropItem(cmds[1:])
        else:
            print("I did not understand that command.")



