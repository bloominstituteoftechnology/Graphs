from room import Room
from player import Player
from item import Item, LightSource, Treasure, Weapon
from monster import Monster
from world import World


world = World()

# Uncomment this to generate the default rooms from Week 1
# world.generateDefaultRooms()

# This will generate 100 rooms.
# You will be modifying this function in world.py for better
# room generation.
world.generateRooms(100)

# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied except 
# for the remains of a previous adventurer. The only exit is to the south."""),

#     'hall': Room("Hall","A simple passageway to another room. Torches hang along the wall."),

#     'throne': Room("Throne Room",
# """The room opens up immensely, wide enough to
# fit over a hundred people and a ceiling that
# reached very high. Along the top of the walls
# there are windows that light the room from the
# outside. Across from the entance on the other
# side of the room, you notice a throne.""")
# }


# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].w_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['foyer'].n_to = room['hall']
# room['hall'].n_to = room['throne']
# room['hall'].s_to = room['foyer']
# room['throne'].s_to = room['hall']
# room['overlook'].e_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# rock = Item("Rock", "This is a rock.")
# lantern = LightSource("Lantern", "A lantern that emits light.")
# coins = Treasure("Coins", "A small pile of coins.", 50)
# sword = Weapon("Sword", "A standard arming blade.", 10)
# big_rock = Item("Big Rock", "This is a big rock.")

# goblin = Monster("Goblin", 15, 5, 0)

# room['outside'].addItem(rock)
# room['outside'].addItem(big_rock)
# room['foyer'].addItem(lantern)
# room['overlook'].addItem(coins)
# room['treasure'].addItem(sword)

# room['hall'].addMonster(goblin)

# room['outside'].light = True
# room['foyer'].light = True
# room['overlook'].light = True
# room['throne'].light = True
# room['hall'].light = True



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
recent_item = []

validDirections = {"n": "n", "s": "s", "e": "e", "w": "w", "north": "n", "south": "s", "east": "e", "west": "w"}

player = Player(input("What is your name?"), world.startingRoom)
print("Enter \"h\" or \"help\" for help.")
print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] == "h" or cmds[0] == "help":
            print("Hint: Find a weapon to slay the monster.\nCommands: \nq - Quit\n\nPlayer commands:\nn or north, etc. - travels that direction\ni or inventory - checks inventory\nlook - looks in current room\nlook + direction - looks in the room in that direction\np or score - checks your score\ntake/drop [item name] - takes or removes items in inventory\nequip/unequip [item name] - equips/unequips item from your inventory.\nfight [monster name] - starts combat with named target.")
        elif cmds[0] == "m":
            world.printMap()
        elif player.killed:
            print("You are dead.")
        else:
            if cmds[0] in validDirections:
                monsters_alive = [monster for monster in player.currentRoom.monsters if not monster.killed]
                if len(monsters_alive) > 0:
                    print(f"The {''.join([monster.name for monster in player.currentRoom.monsters])} blocks your path!")
                else:
                    player.travel(validDirections[cmds[0]])
            elif cmds[0] == "look":
                player.look()
            elif cmds[0] == "i" or cmds[0] == "inventory":
                player.printInventory()
            elif cmds[0] == "p" or cmds[0] == "score":
                print(f"You have {player.score} points.")
            elif cmds[0] == "stats":
                player.printStats()
            else:
                if cmds[0] != "h":
                    print("I did not understand that command.")    
    else:
        if player.killed:
            print("You are dead.")
        else:
            if cmds[0] == "look":
                if cmds[1] in validDirections:
                    monsters_alive = [monster for monster in player.currentRoom.monsters if not monster.killed]
                    if len(monsters_alive) > 0:
                        print(f"The {''.join([monster.name for monster in player.currentRoom.monsters])} blocks your path!")
                    player.look(validDirections[cmds[1]])
            elif cmds[0] == "take":
                if cmds[1] == "it":
                    itemToTake = player.currentRoom.findItembyName(recent_item[0])
                    if itemToTake is not None:
                        player.addItem(itemToTake)
                        player.currentRoom.removeItem(itemToTake)
                        print(f"You have picked up {itemToTake.name}")
                    else:
                        print("You do not see that item.")
                else:
                    itemToTake = player.currentRoom.findItembyName(" ".join(cmds[1:]))                    
                    if itemToTake is not None:
                        player.addItem(itemToTake)
                        player.currentRoom.removeItem(itemToTake)
                        print(f"You have picked up {itemToTake.name}")
                        if len(recent_item) > 0:
                            recent_item.pop()
                        recent_item.append(" ".join(cmds[1:]))
                    else:
                        print("You do not see that item.")
            elif cmds[0] == "drop":
                if cmds[1] == "it":
                    itemToDrop = player.findItembyName(recent_item[0])
                    if itemToDrop is not None:
                        player.removeItem(itemToDrop)
                        player.currentRoom.addItem(itemToDrop)
                        print(f"You have dropped {itemToDrop.name}")
                    else:
                        print("You are not holding that item.")
                else:
                    itemToDrop = player.findItembyName(" ".join(cmds[1:]))
                    if itemToDrop is not None:
                        player.removeItem(itemToDrop)
                        player.currentRoom.addItem(itemToDrop)
                        print(f"You have dropped {itemToDrop.name}")
                        if len(recent_item) > 0:
                            recent_item.pop()
                        recent_item.append(" ".join(cmds[1:]))                    
                    else:
                        print("You are not holding that item.")
            elif cmds[0] == "equip":
                if cmds[1] == "it":
                    itemToEquip = player.findItembyName(recent_item[0])
                    if itemToEquip is not None:
                        if hasattr(itemToEquip,'equippable'):
                            player.equipItem(itemToEquip)
                            player.removeItem(itemToEquip)
                            print(f"You have equipped {itemToEquip.name}")
                        else:
                            print("You cannot equip this item.")
                    else:
                        print("You are not holding that item.")
                else:
                    itemToEquip = player.findItembyName(" ".join(cmds[1:]))            
                    if itemToEquip is not None:
                        if hasattr(itemToEquip,'equippable'):
                            player.equipItem(itemToEquip)
                            player.removeItem(itemToEquip)
                            print(f"You have equipped {itemToEquip.name}")
                            if len(recent_item) > 0:
                                recent_item.pop()
                            recent_item.append(" ".join(cmds[1:]))
                        else:
                            print("You cannot equip this item.")
                    else:
                        print("You are not holding that item.") 
            elif cmds[0] == "unequip":
                if cmds[1] == "it":
                    itemToUnequip = player.findItembyName(recent_item[0])
                    if itemToUnequip is not None:
                        player.unequipItem(itemToUnequip)
                        player.addItem(itemToUnequip)
                        print(f"You have unequipped {itemToUnequip.name}")
                    else:
                        print("You are not holding that item.")
                else:
                    itemToUnequip = player.findItembyName(" ".join(cmds[1:]))
                    if itemToUnequip is not None:
                        player.unequipItem(itemToUnequip)
                        player.addItem(itemToUnequip)
                        print(f"You have unequipped {itemToUnequip.name}")
                        if len(recent_item) > 0:
                            recent_item.pop()
                        recent_item.append(" ".join(cmds[1:]))
                    else:
                        print("You are not holding that item.") 
            elif cmds[0] == "fight":
                monsterToFight = player.currentRoom.findMonsterbyName(" ".join(cmds[1:]))
                if monsterToFight is not None:
                    while monsterToFight.killed != True and player.killed != True:
                        player.attack(monsterToFight)
                        print(f"You delt {player.attack_power}dmg to {monsterToFight.name}!")
                        if monsterToFight.health <= 0:
                            monsterToFight.killed = True
                            print(f"You have slain the {monsterToFight.name}!")
                        if monsterToFight.killed != True:
                            monsterToFight.attack(player)
                            print(f"{monsterToFight.name} delt {monsterToFight.attack_power}dmg to you!")
                            if player.health <= 0:
                                player.killed = True
                                print("You have died!")
                else:
                    print("There is nothing here to fight.")    
            else:
                print("I did not understand that command.")  