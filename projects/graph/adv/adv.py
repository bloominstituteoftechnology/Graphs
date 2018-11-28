from room import Room
from player import Player
from item import Item
import random
from world import World


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
    def generateDefaultRooms(self):
        self.rooms = {
            "outside": Room(
                "Outside Cave Entrance", "North of you, the cave mount beckons"
            ),
            "foyer": Room(
                "Foyer",
                """Dim light filters in from the south. Dusty
        passages run north and east.""",
            ),
            "overlook": Room(
                    "Grand Overlook",
                    """A steep cliff appears before you, falling
            into the darkness. Ahead to the north, a light flickers in
            the distance, but there is no way across the chasm.""",
                ),
                "narrow": Room(
                    "Narrow Passage",
                    """The narrow passage bends here from west
            to north. The smell of gold permeates the air.""",
                ),
# Uncomment this to generate the default rooms from Week 1
# world.generateDefaultRooms()

# This will generate 100 rooms.
# You will be modifying this function in world.py for better
# room generation.
world.generateRooms(100)



# Add some items
junk = Item("Junk", "This is junk")
rock = Item("Rock", "This is a rock")

# Give the player junk and put the rock in the starting room
playerStartingItems = [junk]
world.startingRoom.addItem(rock)


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



