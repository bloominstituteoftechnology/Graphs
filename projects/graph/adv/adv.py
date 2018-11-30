from room import Room
from item import Item
from world import World
from player import Player

world = World()
# Uncomment this to generate the default rooms from Week 1
# world.generateDefaultRooms()

# This will generate 100 rooms.
# You will be modifying this function in world.py for better
# room generation.
world.generateRooms(100)



# Add some items
torch = Item("A Torch", "You have discovered fire, your new name is Promethius")
junk = Item("Piece of Junk", "Unless your having a garage sale, leave it")
phone = Item("A Cell Phone", "A powerful device from the future! All you need is a charger and an outlet. oh right, nevermind")
rock = Item("A Rock", "You discovered a rock, call the Nobel Committee...Seriously, call them")

# Give the player junk and put the rock in the starting room
playerStartingItems = [junk]
world.startingRoom.addItem(rock)


#################################
#
# Below is the adventure REPL code.
#
#################################

valid_directions = {"n": "n", "N": "N", "s": "s", "S": "S", "E": "E", "w": "w", "W": "W", "a": "a", "d": "d",
                    "North": "N", "East": "E", "South": "S", "West": "W",
                    "Backwards": "s", "Right": "d", "Left": "a", "Forward": "w"}

player = Player(input("How do we address you young adventurer? "), world.startingRoom, playerStartingItems)

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
            print("Your command makes no sense.")
    else:
        if cmds[0] == "l" or cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You took {itemToTake.name}")
            else:
                print("Blind to that item")
        elif cmds[0] == "dropped":
            player.dropItem(cmds[1:])
        else:
            print("Your command makes no sense.")
